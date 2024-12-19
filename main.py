import json
import PyPDF2

def find_ids_in_pdf(pdf_path, json_data):
    found = []
    not_found = []

    # Read the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # Extract all text from the PDF
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()

    # Check for each ID in the PDF text
    for entry in json_data:
        id_to_search = entry["id"]
        if id_to_search in full_text:
            found.append(entry)
        else:
            not_found.append(entry)

    return {"found": found, "not_found": not_found}


# Example usage
pdf_path = "source/source.pdf"  # Replace with the path to your PDF file
json_file_path = "source/data.json"  # Replace with the path to your JSON file

# Load JSON data
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

result = find_ids_in_pdf(pdf_path, json_data)

print("IDs not found in PDF:", result["not_found"])