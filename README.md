# PDF ID Finder

A Python script that searches for specific IDs/strings within a PDF file by comparing them against a JSON data source. The script identifies which IDs from the JSON file are present in the PDF document and which ones are missing.

## Features

- Reads and processes PDF files using PyPDF2
- Compares IDs from JSON data against PDF content
- Returns two lists: found and not found IDs
- Simple and efficient text searching implementation

## Requirements

- Python 3.x
- PyPDF2
- json (built-in Python library)

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
```

2. Install required dependencies:
```bash
pip install PyPDF2
```

## Usage

1. Place your PDF file in the `source` directory as `source.pdf`
2. Place your JSON data file in the `source` directory as `data.json`
3. Run the script:
```bash
python pdf_id_finder.py
```

### JSON Data Format

Your JSON file should contain an array of objects with an "id" field:

```json
[
    {"id": "123", ...},
    {"id": "456", ...}
]
```

### Example Code

```python
import json
import PyPDF2

def find_ids_in_pdf(pdf_path, json_data):
    found = []
    not_found = []

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()

    for entry in json_data:
        id_to_search = entry["id"]
        if id_to_search in full_text:
            found.append(entry)
        else:
            not_found.append(entry)

    return {"found": found, "not_found": not_found}
```

## Output

The script will print all IDs that were not found in the PDF file. The output format will be a list of JSON objects that weren't found in the PDF content.

## Directory Structure

```
.
├── source/
│   ├── source.pdf
│   └── data.json
└── pdf_id_finder.py
```

## Limitations

- The script performs simple text matching and may not handle complex PDF layouts
- Large PDF files may require significant memory resources
- PDF files must be text-searchable (not scanned images)

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License
