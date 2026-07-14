import re


# Read extracted text
with open("reports/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Remove extra spaces between letters
# Example: P y t h o n → Python
text = re.sub(r'(?<=\b[A-Za-z])\s(?=[A-Za-z]\b)', '', text)


# Remove multiple spaces but keep line breaks
text = re.sub(r'[ ]+', ' ', text)


# Remove extra empty lines
text = re.sub(r'\n\s*\n+', '\n\n', text)


# Remove PDF header information
text = re.sub(
    r'Document Author:.*?Page \d+ of \d+',
    '',
    text,
    flags=re.IGNORECASE
)


# Save cleaned text
with open("reports/cleaned_text.txt", "w", encoding="utf-8") as file:
    file.write(text.strip())


print("Text cleaning completed!")
print("Saved at: reports/cleaned_text.txt")