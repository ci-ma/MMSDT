import re
import openpyxl
from collections import defaultdict

def get_threats_ids(file_name):
    # Read the input text file
    with open(file_name, 'r') as file:
        content = file.read()

    # Split the content into sections based on "Id: T" using regex
    sections = re.split(r'Id: T\d+\n', content)
    sections = [section.strip() for section in sections if section.strip()]

    # Initialize a list to store the dictionaries for each entry
    entries = []

    # Find the IDs using regex
    ids = re.findall(r'T\d+', content)

    # Loop through sections and extract information
    entries = []
    for i, section in enumerate(sections):
        entries.append(ids[i])

    return entries

def get_attacks(file_path):
    
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select a specific worksheet, or use the active sheet if needed
    worksheet = workbook.active

    # Define the column name you want to extract hyperlinks from
    target_column  = "ATT&CK TECHNIQUE"
    id_column_name = "ATT&CK ID"
    id_capec       = "CAPEC ID"

    # Find the index (column number) of the target column
    column_index = None
    id_column_index = None

    for cell in worksheet[1]:  # Assuming the column names are in the first row
        if cell.value == target_column:
            column_index = cell.column
        elif cell.value == id_column_name:
            id_column_index = cell.column
        elif cell.value == id_capec:
            id_capec_index = cell.column 

    if column_index is not None and id_column_index is not None and id_capec_index is not None:
        # Create a dictionary to store the data
        data = defaultdict(dict)

        # Iterate through the rows and extract hyperlinks from the target column
        for row in worksheet.iter_rows(min_col=id_capec_index, max_col=column_index):
            
            capec_id = row[0].value
            id_cell  = row[2]
            target_cell = row[3]

            if target_cell.hyperlink:
                target_cell_value_cleaned = re.sub(r'[\t\n]', '', target_cell.value)
                data[capec_id][target_cell_value_cleaned] = target_cell.hyperlink.target
        

    else:
        print(f"Column '{target_column}' not found in the worksheet.")

    workbook.close()

    return data



