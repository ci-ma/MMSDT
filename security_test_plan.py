import pandas as pd
import sys
import os
import json
from utils import  get_threats_ids, get_attacks

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python security_test_plan.py <file_path> <xlsx_file_path_capec> <xlsx_file_path_attack>")
    sys.exit(1)

# Specify the path to your XLSX files
file_path             = sys.argv[1]
xlsx_file_path_capec  = sys.argv[2]
xlsx_file_path_attack = sys.argv[3]

threat_ids      = get_threats_ids(file_path)
attacks_catalog = get_attacks(xlsx_file_path_attack)

# Read the XLSX file into a DataFrame
df = pd.read_excel(xlsx_file_path_capec)
capec_id_column  = df['CAPEC ID']
threat_id_column = df['THREAT ID'].to_numpy()
capec_id_column_attack = df['CAPEC ID'].to_numpy()

capec_ids = []

# Matching threat ids
matching_threat_ids = []
for id in threat_ids:
    if id in threat_id_column:
        matching_threat_ids.append(id)

# Identifying capec ids 
for index, row in df.iterrows():
    if row['THREAT ID'] in matching_threat_ids:
        capec_ids.append(row['CAPEC ID'])

attack_ids = []

for capec_id in capec_ids:
    if capec_id in attacks_catalog:
        attack_ids.append(attacks_catalog[capec_id])

# Specify the file path where you want to save the JSON data
file_path = file_path.split("/")
file_path = file_path[len(file_path)-1].split('.')[0]
outputfile_path = "security_test_plan/" + file_path + "_test_plan.json"

if not os.path.exists("security_test_plan"):
    os.makedirs("security_test_plan")

with open(outputfile_path, 'w') as json_file:
    json.dump(attack_ids, json_file, indent=4)

print(f'Security test plan has been written to {outputfile_path}')
