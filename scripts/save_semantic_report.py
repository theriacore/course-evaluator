import os
from datetime import datetime


# -----------------------------
# Output location
# -----------------------------

REPORT_FOLDER = "reports/evaluation"

REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "semantic_evaluation_results.txt"
)



# -----------------------------
# Create folder
# -----------------------------

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)



# -----------------------------
# Ask for result
# -----------------------------

score = input(
    "Enter semantic score: "
)


score = float(score)



# -----------------------------
# Decide evaluation
# -----------------------------

if score >= 80:

    evaluation = "High Coverage"


elif score >= 50:

    evaluation = "Moderate Coverage"


else:

    evaluation = "Low Coverage"



# -----------------------------
# Save report
# -----------------------------

with open(
    REPORT_FILE,
    "w",
    encoding="utf-8"
) as file:


    file.write(
        "AI SEMANTIC COURSE EVALUATION REPORT\n"
    )


    file.write(
        "====================================\n\n"
    )


    file.write(
        f"Date: {datetime.now()}\n\n"
    )


    file.write(
        f"Semantic Score: {score}%\n"
    )


    file.write(
        f"Evaluation: {evaluation}\n"
    )



print("\nReport saved:")
print(REPORT_FILE)