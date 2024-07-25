# ai_file_reader/views.py
import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ai_file_reader.storage import TemporaryFileStorage
from .event_handler import EventHandler
from .form_data_type import FormDataType, prompt
import openai
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

open_ai_key = settings.OPENAI_API_KEY



temp_storage = TemporaryFileStorage()

@csrf_exempt
def process_file(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file provided'}, status=400)
        
        uploaded_file = request.FILES['file']
        file_name = temp_storage.save(uploaded_file.name, uploaded_file)
        file_path = temp_storage.path(file_name)

        try:
            client = openai.OpenAI(api_key=open_ai_key)
            vector_store = client.beta.vector_stores.create(name="Chemical Review")

            with open(file_path, 'rb') as file_stream:
                file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
                    vector_store_id=vector_store.id, files=[file_stream]
                )

            message_file = client.files.create(
                file=open(file_path, "rb"), purpose="assistants"
            )

            prompt_content = (
                "using the attached information and any other files available to you fill the a chemical "
                "intake form with the following columns chemNo, chemDesc, chemGrade, commodity, testing, "
                "testProps, companyName, brandName, outsourced_only, composition, WPSID, sdsSaved, sdsFile, "
                "coaSaved, coaFile, sds_date, hazardous, oxidizer, form, color, odor, appearance, flashPoint, "
                "freezePoint, spg, pH_neat, vaporPressure, meltingPoint, pH_1percent, blkDens, corrosive, "
                "solubility, pictograms, ppe, respiratorRequired, respiratorType, respiratorNo, maskType, "
                "catridgeType, storageLocation, container, tsca, sara313Reportable, sara313CasNo, "
                "prop65, water_reaction, contains_cl, one_4_dioxane, propConc,"
                "readilyBiodegradable, bioMethod, bioAmount, "
                "marinePollutant, canadian_DSL_NDSL, voc, percentVoc, percentLVPVOC, derivedFromNaturalSrc, "
                "percentNaturallyDerived, bioBased, percentBiobased, tier_II_reportable, tier_II_amount, "
                "tier_II_EHS, tier_II_hazard_composition, tier_II_hazard_form, tier_II_hazard_class, "
                "containsBacteria, containsPalm_PalmKernelOil, otherOils, palmOil_Other_certified, "
                "certifications, notes, otherFiles. convert filled form into "
                "a json object to be easily consumed by front end react-hook-form as initial values. If data "
                "for a field is not specified use and empty string, for fields whose responses are boolean use "
                "Yes,No. For composition and propConc fields, "
                "it is likely to be a list of multiple components create appropriate array with chemicalName, "
                "casNo and percentage. Where percentage is given as a range calculate the average. "
                "Similarly for other fields where a range is give use average values. "
                "For container in [Drum, Tote, Super Sack, Bag] and certifications in [Safer Choice, "
                "Kosher, NSF, Green Seal, Whole Foods, EPA, FDA, Halal], break into a list with the most relevant match "
                "The dataTypes used for the form is {} be aware of units and convert to "
                "Imperial where appropriate as user is based in USA, chemNo field is reserved so leave empty"
            ).format(FormDataType)

            assistant = client.beta.assistants.create(
                name='R&D Scientist and Product Developer',
                instructions="You are an expert product developer for household, institutional and healthcare products. "
                             "Use your knowledge to review chemical documents such as Safety Data Sheets (SDS) and "
                             "Technical Data Sheets (TDS) and provide insights for developing sustainable and performant products "
                             "as well as generating sound specifications",
                model='gpt-4o',
                tools=[{"type": "file_search"}]
            )

            assistant = client.beta.assistants.update(
                assistant_id=assistant.id,
                tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
            )

            thread = client.beta.threads.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt_content,
                        "attachments": [
                            {
                                "file_id": message_file.id, "tools": [{"type": "file_search"}]
                            }
                        ]
                    }
                ]
            )

            event_handler = EventHandler()
            with client.beta.threads.runs.stream(
                    thread_id=thread.id,
                    assistant_id=assistant.id,
                    instructions="Please address the user as John Smith. The user is a chemist",
                    event_handler=event_handler
            ) as stream:
                stream.until_done()

            # Clean up the temporary file after processing
            temp_storage.delete(file_name)

            if event_handler.output_json:
                print("Output JSON from EventHandler:", event_handler.output_json)
                return JsonResponse(json.loads(event_handler.output_json), safe=False)
            else:
                print("No data returned from assistant")
                return JsonResponse({'error': 'No data returned from assistant'}, status=500)

        except Exception as e:
            # Clean up the temporary file if an error occurs
            temp_storage.delete(file_name)
            print("Error occurred:", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)