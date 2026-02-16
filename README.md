 # 🤖 ResumeRank AI

**An AI-powered recruitment assistant that automatically screens, scores, and ranks candidate resumes against job descriptions.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

## 🚀 Overview
Hiring is broken. Recruiters spend hours manually reviewing hundreds of resumes. **ResumeRank AI** solves this by using Large Language Models (LLMs) to:
1.  **Read** PDF resumes and extract key skills.
2.  **Compare** them against a specific Job Description (JD).
3.  **Score** candidates from 0-100 based on relevance.
4.  **Rank** them in a real-time dashboard.

> **Note:** This project uses Google's **Gemini 2.5 Flash** model for high-speed, cost-effective processing.

## 🛠️ Tech Stack
* **Core Logic:** Python
* **AI Engine:** Google Gemini 2.5 Flash
* **UI/Dashboard:** Streamlit
* **Data Handling:** Pandas & JSON
* **PDF Parsing:** PyPDF

## ⚙️ How It Works
1.  **Input:** The system accepts a folder of PDF resumes and a Job Description text file.
2.  **Processing:** * Iterates through every PDF.
    * Extracts raw text.
    * Sends text + JD to Gemini via API.
    * LLM performs a "Chain of Thought" analysis to evaluate skills and experience.
3.  **Output:** Returns a structured JSON with score, summary, and missing skills.
4.  **Visualization:** Displays a ranked leaderboard on the Streamlit web app.

## 🔋 Features
* ✅ **Batch Processing:** Handles multiple resumes in seconds.
* ✅ **Strict Scoring:** Uses a custom prompt to avoid generic "AI positivity."
* ✅ **Gap Analysis:** Explicitly lists *missing* critical skills for each candidate.
* ✅ **Interactive UI:** Click on any candidate to see their detailed breakdown.

## 🏃‍♂️ How to Run locally

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/ResumeRank-AI.git](https://github.com/YOUR_USERNAME/ResumeRank-AI.git)
cd ResumeRank-AI