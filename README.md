# Course Evaluator AI

## Project Overview

Course Evaluator AI is an automated system that evaluates AI-generated educational content against textbook content using semantic similarity techniques.

The system analyzes whether AI-generated explanations properly cover important concepts from a textbook and generates an evaluation report with coverage scores and recommendations.


---

## Objective

The main objective of this project is to:

- Extract content from educational PDFs
- Process and clean extracted text
- Divide textbook content into meaningful chunks
- Compare AI-generated answers with textbook sections
- Measure content coverage using AI-based semantic similarity
- Generate evaluation reports and visual summaries


---

## System Workflow
PDF Document
|
↓
Text Extraction
|
↓
Text Cleaning
|
↓
Content Chunking
|
↓
AI Generated Content
|
↓
Semantic Similarity Analysis
|
↓
Coverage Evaluation
|
↓
Final Report + Dashboard


---

## Features

### 1. PDF Text Extraction

- Extracts textbook content automatically
- Supports educational PDF documents


### 2. Text Cleaning

Removes unnecessary formatting and prepares text for analysis.


### 3. Intelligent Chunking

Divides large textbook content into smaller sections for detailed evaluation.


### 4. AI Semantic Comparison

Uses sentence embeddings to compare meaning instead of only matching words.

Technology:

- Sentence Transformers
- Cosine Similarity


### 5. Coverage Evaluation

Each section is classified as:

| Score | Evaluation |
|---|---|
| 85%+ | Excellent Coverage |
| 70-85% | Strong Coverage |
| 50-70% | Moderate Coverage |
| Below 50% | Needs Improvement |


### 6. Report Generation

Generates:

- Evaluation report
- Weak section identification
- Recommendations


### 7. Visualization Dashboard

Creates:

- Topic-wise similarity charts
- Evaluation summary


---

## Technologies Used

### Programming Language

- Python


### Libraries

- PyMuPDF
- Sentence Transformers
- Scikit-learn
- Matplotlib


### AI Model

Sentence Transformer:
all-MiniLM-L6-v2


---

## Project Structure
COURSE-EVALUATOR
├── data
│
├── reports
│ ├── processed
│ ├── evaluation
│
├── scripts
│ ├── read_pdf.py
│ ├── clean_text.py
│ ├── split_text.py
│ ├── compare_chunks.py
│ ├── generate_report.py
│ └── create_chart.py
│
├── dashboard
│ ├── summary.txt
│ └── charts
│ └── chunk_scores.png
│
└── README.md

## Project Results

Traditional Similarity Score:
66.48%

AI Semantic Similarity Score:
62%

Total Question Chunks:
12

Dashboard:
Streamlit-based interactive dashboard displaying evaluation scores, reports, and charts.


## How to Run

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run dashboard/app.py
## Dashboard Preview

![Dashboard](images/dashboard.png)