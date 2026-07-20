import re

INPUT = "reports/extracted_text.txt"
OUTPUT = "reports/cleaned_text.txt"

with open(INPUT, "r", encoding="utf-8") as file:
    text = file.read()

# Remove carriage returns
text = text.replace("\r", "")

# Remove repeated "Reprint"
text = re.sub(r"Reprint\s+\d{4}-\d{2}", "", text)

# Remove standalone page numbers
text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

lines = text.split("\n")

cleaned = []

paragraph = ""

for line in lines:

    line = line.strip()

    if not line:
        continue

    # Keep headings separate
    if (
        line.isupper()
        or re.match(r"^\d+\.\d+", line)
    ):

        if paragraph:
            cleaned.append(paragraph.strip())
            paragraph = ""

        cleaned.append(line)
        continue

    # Merge wrapped lines
    if paragraph:
        paragraph += " " + line
    else:
        paragraph = line

if paragraph:
    cleaned.append(paragraph)

with open(OUTPUT, "w", encoding="utf-8") as file:

    file.write("\n\n".join(cleaned))

print("Cleaning completed.")