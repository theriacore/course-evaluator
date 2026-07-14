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


import matplotlib.pyplot as plt


from config import (
    EVALUATION_FILE,
    CHART_OUTPUT
)



# -----------------------------
# Read evaluation scores
# -----------------------------

topics = []
scores = []


with open(
    EVALUATION_FILE,
    "r",
    encoding="utf-8"
) as file:


    for line in file:


        if "%" in line and "|" in line:


            parts = line.split("|")


            if len(parts) >= 3:


                topic = parts[1].strip()


                score_text = (
                    parts[2]
                    .strip()
                    .replace("%", "")
                )


                try:

                    score = float(score_text)


                    topics.append(
                        topic
                    )

                    scores.append(
                        score
                    )


                except ValueError:

                    continue




# -----------------------------
# Create chart folder
# -----------------------------

chart_folder = os.path.dirname(
    CHART_OUTPUT
)


if not os.path.exists(
    chart_folder
):

    os.makedirs(
        chart_folder
    )




# -----------------------------
# Create bar chart
# -----------------------------

plt.figure(
    figsize=(10,6)
)


plt.bar(
    topics,
    scores
)


plt.xlabel(
    "Topics"
)


plt.ylabel(
    "Similarity Score (%)"
)


plt.title(
    "Course Evaluation - Chunk Similarity Scores"
)


plt.xticks(
    rotation=45,
    ha="right"
)


plt.tight_layout()



# Save chart

plt.savefig(
    CHART_OUTPUT
)


plt.close()



print(
    "Chart created successfully!"
)


print(
    CHART_OUTPUT
)