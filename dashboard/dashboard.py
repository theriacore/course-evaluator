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


from config import EVALUATION_FILE, FINAL_REPORT



print("=" * 45)
print("        COURSE EVALUATOR DASHBOARD")
print("=" * 45)



average_score = "Not available"
final_evaluation = "Not available"

weak_topics = []

total_chunks = 0



# Store all report lines

lines = []



# Read evaluation file

try:

    with open(
        EVALUATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        lines.extend(
            file.readlines()
        )

except FileNotFoundError:

    print("Evaluation file not found")



# Read final report

try:

    with open(
        FINAL_REPORT,
        "r",
        encoding="utf-8"
    ) as file:

        lines.extend(
            file.readlines()
        )

except FileNotFoundError:

    print("Final report not found")





# Analyze report data

for line in lines:

    clean_line = line.strip()



    # Count chunks

    if "Chunk" in clean_line or "|" in clean_line:

        total_chunks += 1




    # Find score

    if (
        "Average Similarity Score" in clean_line
        or "Average Score" in clean_line
        or "%" in clean_line
    ):

        parts = clean_line.split(":")


        if len(parts) > 1:

            value = parts[-1].strip()


            if "%" in value:

                average_score = value





    # Find evaluation result

    if "Final Evaluation" in clean_line:

        parts = clean_line.split(":")


        if len(parts) > 1:

            final_evaluation = parts[-1].strip()





    # Find weak topics

    if clean_line.startswith("-"):

        weak_topics.append(
            clean_line
        )





# Display dashboard

print("\nProject Summary")
print("----------------")

print(
    "Average Score:",
    average_score
)


print(
    "Evaluation Status:",
    final_evaluation
)


print(
    "Chunks Evaluated:",
    total_chunks
)




print("\nWeak Sections")
print("----------------")


if weak_topics:

    for topic in weak_topics:

        print(topic)

else:

    print(
        "No weak sections found"
    )




print("\nVisualization")
print("----------------")

print(
    "dashboard/charts/chunk_scores.png"
)



print("\nDashboard generated successfully!")