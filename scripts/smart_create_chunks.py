import os

INPUT_FILE = "reports/cleaned_text.txt"
OUTPUT_DIR = "reports/processed/chunks"

CHUNK_PARAGRAPHS = 5
OVERLAP = 1

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------
# Remove old chunks
# ---------------------------------------

for file in os.listdir(OUTPUT_DIR):
    if file.endswith(".txt"):
        os.remove(os.path.join(OUTPUT_DIR, file))

# ---------------------------------------
# Read cleaned text
# ---------------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    text = file.read()

# Paragraphs are separated by blank lines
paragraphs = [
    p.strip()
    for p in text.split("\n\n")
    if p.strip()
]

chunks = []

i = 0

while i < len(paragraphs):

    chunk = "\n\n".join(
        paragraphs[i:i + CHUNK_PARAGRAPHS]
    )

    chunks.append(chunk)

    i += CHUNK_PARAGRAPHS - OVERLAP

# ---------------------------------------
# Save chunks
# ---------------------------------------

for index, chunk in enumerate(chunks, start=1):

    filename = os.path.join(
        OUTPUT_DIR,
        f"chunk_{index}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:
        file.write(chunk)

    print("Created:", filename)

print("\n========================")
print("Total chunks:", len(chunks))
print("========================")