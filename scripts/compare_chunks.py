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


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


from config import (
    AI_TEXT_FILE,
    CHUNKS_FOLDER,
    EVALUATION_FILE
)



# -----------------------------
# Extract topic from chunk
# -----------------------------

def get_topic(text):

    lines = text.split("\n")

    ignored = [
        "Document Author",
        "Page",
        "Class",
        "Python Programming Language",
        "Theoretical Questions",
        "Questions"
    ]


    for line in lines:

        line = line.strip()


        if len(line) < 5:
            continue


        if any(
            word.lower() in line.lower()
            for word in ignored
        ):
            continue


        if line.isdigit():
            continue


        return line[:60]


    return "Unknown Topic"




# -----------------------------
# Split AI generated text
# -----------------------------

def split_ai_text(text, size=500):

    words = text.split()

    sections = []


    for i in range(0, len(words), size):

        sections.append(
            " ".join(
                words[i:i+size]
            )
        )


    return sections




print("Loading AI similarity model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



# -----------------------------
# Read AI generated content
# -----------------------------

with open(
    AI_TEXT_FILE,
    "r",
    encoding="utf-8"
) as file:

    ai_text = file.read()



ai_sections = split_ai_text(
    ai_text
)



print("Creating AI embeddings...")


ai_embeddings = model.encode(
    ai_sections
)




scores = []

weak_topics = []



# -----------------------------
# Evaluate chunks
# -----------------------------

with open(
    EVALUATION_FILE,
    "w",
    encoding="utf-8"
) as report:


    report.write(
        "Chunk Evaluation Report\n"
    )

    report.write(
        "======================\n\n"
    )



    for filename in sorted(
        os.listdir(CHUNKS_FOLDER)
    ):


        if filename.endswith(".txt"):


            path = os.path.join(
                CHUNKS_FOLDER,
                filename
            )



            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                chunk_text = file.read()



            topic = get_topic(
                chunk_text
            )



            chunk_embedding = model.encode(
                [chunk_text]
            )



            similarity = cosine_similarity(
                chunk_embedding,
                ai_embeddings
            )



            score = max(
                similarity[0]
            ) * 100



            scores.append(
                score
            )



            if score >= 85:

                evaluation = "Excellent Coverage"


            elif score >= 70:

                evaluation = "Strong Coverage"


            elif score >= 50:

                evaluation = "Moderate Coverage"


            else:

                evaluation = "Needs Improvement"

                weak_topics.append(
                    topic
                )



            result = (
                f"{filename} | "
                f"{topic} | "
                f"{score:.2f}% | "
                f"{evaluation}"
            )


            print(result)


            report.write(
                result + "\n"
            )




# -----------------------------
# Final evaluation
# -----------------------------

average_score = (
    sum(scores) / len(scores)
)



if average_score >= 85:

    final_status = "Excellent Coverage"


elif average_score >= 70:

    final_status = "Strong Coverage"


elif average_score >= 50:

    final_status = "Moderate Coverage"


else:

    final_status = "Needs Improvement"




with open(
    EVALUATION_FILE,
    "a",
    encoding="utf-8"
) as report:


    report.write(
        "\n\nFinal Evaluation\n"
    )

    report.write(
        "================\n"
    )

    report.write(
        f"Average Similarity Score: {average_score:.2f}%\n"
    )

    report.write(
        f"Final Evaluation: {final_status}\n"
    )


    report.write(
        "\nWeak Sections:\n"
    )


    if weak_topics:


        for topic in weak_topics:

            report.write(
                f"- {topic}\n"
            )


    else:

        report.write(
            "No weak sections found.\n"
        )




print("\nEvaluation completed!")

print(
    f"Average Score: {average_score:.2f}%"
)

print(
    f"Final Evaluation: {final_status}"
)

print(
    f"Saved: {EVALUATION_FILE}"
)