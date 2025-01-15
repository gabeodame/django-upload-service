import pandas as pd
import os
# Define the data as a list of dictionaries
data = [
    {"category": "acute_toxicity", "option": "Category 1", "score": 1},
    {"category": "acute_toxicity", "option": "Category 2", "score": 2},
    {"category": "acute_toxicity", "option": "Category 3 or Higher", "score": 3},
    {"category": "aquatic_toxicity", "option": "Category 1", "score": 1},
    {"category": "aquatic_toxicity", "option": "Category 2", "score": 2},
    {"category": "aquatic_toxicity", "option": "Category 3 or Higher", "score": 3},
    {"category": "sensitization_skin", "option": "Yes", "score": 1},
    {"category": "sensitization_skin", "option": "No", "score": 3},
    {"category": "mutagenicity", "option": "Yes", "score": 1},
    {"category": "mutagenicity", "option": "No", "score": 3},
    {"category": "carcinogenicity", "option": "Yes", "score": 1},
    {"category": "carcinogenicity", "option": "No", "score": 3},
    {"category": "reproductive_toxicity", "option": "Yes", "score": 1},
    {"category": "reproductive_toxicity", "option": "No", "score": 3},
    {"category": "ca_sb_258", "option": "Yes", "score": 1},
    {"category": "ca_sb_258", "option": "No", "score": 3},
    {"category": "reach_svh", "option": "Yes", "score": 1},
    {"category": "reach_svh", "option": "No", "score": 3},
    {"category": "readily_biodegradable", "option": "Yes", "score": 3},
    {"category": "readily_biodegradable", "option": "No", "score": 1},
    {"category": "readily_biodegradable", "option": "N/A", "score": 2},
    {"category": "voc", "option": "Yes", "score": 1},
    {"category": "voc", "option": "No", "score": 3},
    {"category": "palm_kernel_oil_derived", "option": "Not RSPO certified", "score": 1},
    {"category": "palm_kernel_oil_derived", "option": "RSPO certified", "score": 2},
    {"category": "palm_kernel_oil_derived", "option": "No", "score": 3},
    {"category": "palm_kernel_oil_derived", "option": "N/A", "score": 3},
    {"category": "biobased", "option": "NA or 0-33%", "score": 1},
    {"category": "biobased", "option": "34-66%", "score": 2},
    {"category": "biobased", "option": "67-100%", "score": 3},
    {"category": "biobased", "option": "Inorganic", "score": 3},
    {"category": "from_renewable_sources", "option": "Yes", "score": 3},
    {"category": "from_renewable_sources", "option": "No", "score": 1},
    {"category": "safer_choice_or_clean_gredients", "option": "Yes", "score": 3},
    {"category": "safer_choice_or_clean_gredients", "option": "No", "score": 1},
    {"category": "safer_choice_or_clean_gredients", "option": "N/A", "score": 2},
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path = os.path.join('./', 'score_mapping.csv')
df.to_csv(file_path, index=False)

file_path

