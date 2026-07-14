import sys
import os


# Allow importing config.py from project root
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from config import (
    EVALUATION_FILE,
    FINAL_REPORT
)



# -----------------------------
# Read evaluation results
# -----------------------------

with open(
    EVALUATION_FILE,
    "r",
    encoding="utf-8"
) as file:

    evaluation_data = file.read()



# -----------------------------
# Generate final report
# -----------------------------

with open(
    FINAL_REPORT,
    "w",
    encoding="utf-8"
) as report:


    report.write(
        "COURSE EVALUATION REPORT\n"
    )

    report.write(
        "========================\n\n"
    )


    report.write(
        evaluation_data
    )



print(
    "Final report generated successfully!"
)


print(
    FINAL_REPORT
)