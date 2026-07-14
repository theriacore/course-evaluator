from rapidfuzz import fuzz


with open("reports/cleaned_text.txt", "r", encoding="utf-8") as file:
    text1 = file.read()


with open("reports/ai_generated_text.txt", "r", encoding="utf-8") as file:
    text2 = file.read()


score = fuzz.token_set_ratio(text1, text2)


if score >= 80:
    evaluation = "Excellent Match"

elif score >= 60:
    evaluation = "Good Match"

elif score >= 40:
    evaluation = "Moderate Match"

else:
    evaluation = "Low Match"


print("Similarity Score:", score)
print("Evaluation:", evaluation)