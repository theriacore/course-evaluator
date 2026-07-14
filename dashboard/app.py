import streamlit as st
import sys
import os


# ---------------------------------
# Add project root path
# ---------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from config import (
    EVALUATION_FILE,
    FINAL_REPORT,
    CHART_OUTPUT
)



# ---------------------------------
# Page settings
# ---------------------------------

st.set_page_config(
    page_title="Course Evaluator",
    page_icon="📘",
    layout="wide"
)



# ---------------------------------
# Title
# ---------------------------------

st.title(
    "📘 Course Evaluator Dashboard"
)


st.write(
    "AI-based evaluation system for comparing course content coverage."
)


st.divider()



# ---------------------------------
# Project Information
# ---------------------------------

st.header(
    "Project Information"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        """
        📚 Source

        Class 9 Python Textbook
        """
    )


with col2:

    st.info(
        """
        🤖 Methods

        Traditional Similarity
        +
        AI Semantic Comparison
        """
    )


with col3:

    st.info(
        """
        📊 Output

        Coverage Evaluation
        """
    )



st.divider()



# ---------------------------------
# Read Traditional Evaluation
# ---------------------------------

traditional_score = "Not Available"
traditional_status = "Not Available"



if os.path.exists(EVALUATION_FILE):

    with open(
        EVALUATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()



    for line in content.split("\n"):


        if "Average Similarity Score:" in line:

            traditional_score = (
                line
                .replace(
                    "Average Similarity Score:",
                    ""
                )
                .strip()
            )



        if "Final Evaluation:" in line:

            traditional_status = (
                line
                .replace(
                    "Final Evaluation:",
                    ""
                )
                .strip()
            )



# ---------------------------------
# Read Semantic Evaluation
# ---------------------------------

semantic_score = "Not Available"
semantic_status = "Not Available"



semantic_file = (
    "reports/evaluation/"
    "semantic_evaluation_results.txt"
)



if os.path.exists(semantic_file):

    with open(
        semantic_file,
        "r",
        encoding="utf-8"
    ) as file:

        semantic_content = file.read()



    for line in semantic_content.split("\n"):


        if "Semantic Score:" in line:

            semantic_score = (
                line
                .replace(
                    "Semantic Score:",
                    ""
                )
                .strip()
            )



        if "Evaluation:" in line:

            semantic_status = (
                line
                .replace(
                    "Evaluation:",
                    ""
                )
                .strip()
            )



# ---------------------------------
# Evaluation Summary
# ---------------------------------

st.header(
    "Evaluation Summary"
)



col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        "Traditional Score",
        traditional_score
    )



with col2:

    st.metric(
        "AI Semantic Score",
        semantic_score
    )



with col3:

    st.metric(
        "Chunks Analysed",
        "12"
    )



st.divider()



# ---------------------------------
# Comparison
# ---------------------------------

st.header(
    "Evaluation Comparison"
)



st.write(
    f"""
### Traditional Method

Score:
{traditional_score}

Status:
{traditional_status}


### AI Semantic Method

Score:
{semantic_score}

Status:
{semantic_status}
"""
)



st.divider()



# ---------------------------------
# Final Report
# ---------------------------------

st.header(
    "Final Report"
)



if os.path.exists(FINAL_REPORT):

    with open(
        FINAL_REPORT,
        "r",
        encoding="utf-8"
    ) as file:

        report = file.read()



    st.text_area(
        "Report",
        report,
        height=300
    )


else:

    st.warning(
        "Final report not found"
    )



st.divider()



# ---------------------------------
# Chart
# ---------------------------------

st.header(
    "Coverage Chart"
)



if os.path.exists(CHART_OUTPUT):

    st.image(
        CHART_OUTPUT,
        use_container_width=True
    )


else:

    st.warning(
        "Chart not found"
    )



st.success(
    "Dashboard loaded successfully!"
)