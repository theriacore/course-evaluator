from pypdf import PdfReader

pdf = PdfReader("data/class9_pythontextbook.pdf")

print("Number of pages:", len(pdf.pages))

all_text = ""

for page in pdf.pages:
    text = page.extract_text()

    if text:
        all_text += text + "\n\n"

with open("reports/extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("Text extraction completed!")
print("Saved file: reports/extracted_text.txt")