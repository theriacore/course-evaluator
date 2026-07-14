import os
import re


INPUT_FILE = "reports/cleaned_text.txt"
OUTPUT_DIR = "reports/processed/chunks"


os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# Read file

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as file:

    text = file.read()



# Normalize spaces

text = re.sub(
    r"\s+",
    " ",
    text
).strip()



# Remove heading

for heading in [
    "Class IX",
    "Python Programming Language",
    "Theoretical Questions"
]:

    text = text.replace(
        heading,
        ""
    )



# Fix OCR numbers

text = text.replace(
    "1 0 .",
    "10."
)

text = text.replace(
    "1 1 .",
    "11."
)

text = text.replace(
    "1 2 .",
    "12."
)



# Exact question markers

markers = [
    "1 .",
    "2 .",
    "3 .",
    "4 .",
    "5 .",
    "6 .",
    "7 .",
    "8 .",
    "9 .",
    "10.",
    "11.",
    "12."
]



positions = []


for marker in markers:

    position = text.find(marker)

    if position != -1:

        positions.append(position)



positions.sort()



chunks = []


for i in range(len(positions)):

    start = positions[i]


    if i + 1 < len(positions):

        end = positions[i + 1]

    else:

        end = len(text)



    chunk = text[start:end].strip()


    chunks.append(chunk)



# Delete old chunks

for file_name in os.listdir(OUTPUT_DIR):

    if file_name.endswith(".txt"):

        os.remove(
            os.path.join(
                OUTPUT_DIR,
                file_name
            )
        )



# Save chunks

for index, chunk in enumerate(
    chunks,
    start=1
):

    path = os.path.join(
        OUTPUT_DIR,
        f"chunk_{index}.txt"
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(chunk)


    print(
        "Created:",
        path
    )



print("\n================")
print(
    "Total chunks:",
    len(chunks)
)
print("================")