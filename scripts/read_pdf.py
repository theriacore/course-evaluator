from pypdf import PdfReader

PDF_FILE = "data/class9_pythontextbook.pdf"

# Number of front pages to skip
START_PAGE = 12

pdf = PdfReader(PDF_FILE)

print("Number of pages:", len(pdf.pages))
print("Reading from page:", START_PAGE + 1)

all_text = ""

for page in pdf.pages[START_PAGE:]:

    text = page.extract_text()

    if text:
        all_text += text + "\n\n"

with open(
    "reports/extracted_text.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(all_text)

print("Text extraction completed!")
print("Saved file: reports/extracted_text.txt")