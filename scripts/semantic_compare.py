import os
import sys

from sentence_transformers import SentenceTransformer, util


# ---------------------------------
# Allow importing config.py
# ---------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from config import CHUNKS_FOLDER



# ---------------------------------
# File location
# ---------------------------------

AI_REFERENCE_FILE = "reports/ai_generated_text.txt"



print("=" * 50)
print("AI SEMANTIC COURSE EVALUATION")
print("=" * 50)



# ---------------------------------
# Load AI model
# ---------------------------------

print("\nLoading AI model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("AI model loaded!")



# ---------------------------------
# Read AI generated content
# ---------------------------------

with open(
    AI_REFERENCE_FILE,
    "r",
    encoding="utf-8"
) as file:

    reference_text = file.read()



print(
    "\nReference content loaded"
)



# Create reference embedding

reference_embedding = model.encode(
    reference_text,
    convert_to_tensor=True
)



# ---------------------------------
# Read chunks
# ---------------------------------

chunks = []


for file_name in sorted(
    os.listdir(CHUNKS_FOLDER)
):

    if file_name.endswith(".txt"):

        path = os.path.join(
            CHUNKS_FOLDER,
            file_name
        )


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            chunks.append(
                {
                    "name": file_name,
                    "text": file.read()
                }
            )



print(
    "Chunks loaded:",
    len(chunks)
)



# ---------------------------------
# Semantic comparison
# ---------------------------------

scores = []


print("\nSimilarity Results")
print("------------------")


for chunk in chunks:


    chunk_embedding = model.encode(
        chunk["text"],
        convert_to_tensor=True
    )


    similarity = util.cos_sim(
        chunk_embedding,
        reference_embedding
    )


    score = round(
        float(similarity[0][0]) * 100,
        2
    )


    scores.append(score)


    print(
        chunk["name"],
        "|",
        score,
        "%"
    )



# ---------------------------------
# Average score
# ---------------------------------

average_score = round(
    sum(scores) / len(scores),
    2
)



print("\n====================")
print(
    "Average Semantic Score:",
    average_score,
    "%"
)
print("====================")


if average_score >= 80:

    print(
        "Evaluation: High Coverage"
    )


elif average_score >= 50:

    print(
        "Evaluation: Moderate Coverage"
    )


else:

    print(
        "Evaluation: Low Coverage"
    )