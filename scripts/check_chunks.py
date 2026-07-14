import os


folder = "reports/chunks"

files = os.listdir(folder)

for file in files:
    if file.endswith(".txt"):
        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        print(file, ":", len(text), "characters")
        