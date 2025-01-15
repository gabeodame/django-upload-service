from ai_file_reader import initial_values
from ai_file_reader.form_data_type import FormDataType


def get_chemical_intake_prompt():
    return (
                "Using the attached information and any other files available to you, fill the chemical intake form with "
                "the following fields: chemNo, chemDesc, chemGrade, commodity, testing, testProps, companyName, brandName, "
                "outsourced_only, composition, WPSID, sdsSaved, sdsFile, coaSaved, coaFile, sds_date, hazardous, oxidizer, "
                "form, color, odor, appearance, flashPoint, freezePoint, spg, pH_neat, vaporPressure, meltingPoint, "
                "pH_1percent, blkDens, corrosive, solubility, pictograms, ppe, respiratorRequired, respiratorType, respiratorNo, maskType, "
                "catridgeType, storageLocation, container, tsca, sara313Reportable, sara313CasNo, prop65, water_reaction, "
                "contain_cl, one_4_dioxane, propConc, readilyBiodegradable, bioMethod, bioAmount, marinePollutant, canadian_DSL_NDSL, "
                "voc, percentVoc, percentLVPVOC, derivedFromNaturalSrc, percentNaturallyDerived, bioBased, percentBiobased, "
                "tier_II_reportable, tier_II_amount, tier_II_EHS, tier_II_hazard_composition, tier_II_hazard_form, tier_II_hazard_class, "
                "containsBacteria, containsPalm_PalmKernelOil, otherOils, palmOil_Other_certified, certifications, notes, otherFiles. "
                
                "Convert the filled form into a JSON object to be easily consumed by the front-end react-hook-form as initial values. "
                
                "Instructions:\n"
                "1. For any field not specified in the provided data, use the initial values specified in the external file.\n"
                "2. If data for a field is not specified, use an empty string ('').\n"
                "3. For fields with boolean responses, use 'Yes' or 'No'.\n"
                "4. For 'composition' and 'propConc', create an array of objects with 'chemicalName', 'casNo', and 'percentage'. "
                "   - If 'percentage' is given as a range, calculate the average.\n"
                "5. For fields with a range, use the average value.\n"
                "6. For 'container', use the most relevant match from [Drum, Tote, Super Sack, Bag]. and it should be an array of matched strings\n"
                "7. For 'certifications', use the most relevant match from [Safer Choice, Kosher, NSF, Green Seal, Whole Foods, EPA, FDA, Halal].\n"
                "8. For 'pictograms', match the extracted text with the closest options from the provided list: 'Exclamation', 'Corrosive', 'Toxic', 'Flammable', 'Oxidizer', 'Environmental', 'Explosive', 'Compressed', 'Hazmat'. "
                "   - If a pictogram description matches a hazard code, convert it using the provided mapping.\n"
                "9. For 'ppe', use the extracted text to determine the closest and best match with the descriptions in the list of available options: 'Safety Glasses', 'Safety Glasses, Gloves', 'Safety Glasses, Gloves, Apron', "
                "'Face Shield, Gloves, Apron', 'Safety Glasses, Gloves, Dust Respirator', 'Safety Glasses, Gloves, Apron, Dust Respirator', "
                "'Safety Glasses, Gloves, Vapor Respirator', 'Splash Goggles, Gloves, Apron, Vapor Respirator', 'Safety Glasses, Gloves, Dust & Vapor Respirator', "
                "'Splash Goggles, Gloves, Apron, Dust & Vapor Respirator', 'Air Line Hood or Mask, Gloves, Full Suit, Boots', 'Ask Supervisor'. "
                "   - Ensure the matched description is used to select the correct option on form initialization.\n"
                "10. Be aware of units and convert to Imperial where appropriate, as the user is based in the USA.\n"
                "11. Leave the 'chemNo' field empty as it is reserved.\n"
                "12. For form, the options are either 'Liquid' or 'Powder'. If 'Solid' is found, use 'Powder'.\n"
                "13. For whether or not the chemical contains chlorine or dioxane, check section 3 as well as other sections pertaining to regulatory fields (contain_cl, dioxane respectively). If none are found, select 'No'.\n"
                "14. For tier_II_hazard_class format as list of strings"
                "Your response should be a JSON object with the specified fields to initialize the form."
            ).format(FormDataType=FormDataType, initial_values=initial_values)