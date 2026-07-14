import os


with open("reports/cleaned_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


chunks = text.split("?")


os.makedirs("reports/chunks", exist_ok=True)


for i, chunk in enumerate(chunks):
    with open(f"reports/chunks/chunk_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(chunk)


print("Chunks created:", len(chunks))