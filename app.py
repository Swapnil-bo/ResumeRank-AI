import streamlit as st
import pandas as pd
import os

# Page Config
st.set_page_config(page_title="ResumeRank AI", page_icon="🤖", layout="wide")

# Title and Header
st.title("🤖 ResumeRank AI")
st.markdown("### Automated Candidate Scoring System")

# Define paths
csv_path = "final_rankings.csv"
resume_folder = "resumes"

# Metric Cards
col1, col2, col3 = st.columns(3)
col1.metric("Job Role", "Python Developer")
col2.metric("Processing Engine", "Gemini 2.5 Flash")

# Load Data
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    
    # Sort by Score
    df = df.sort_values(by="score", ascending=False)
    
    # Update the candidate count metric
    col3.metric("Candidates Ranked", len(df))

    # --- LEADERBOARD SECTION ---
    st.markdown("---")
    st.subheader("🏆 Top Candidates")
    
    # Display the table with specific columns
    st.dataframe(
        df[["score", "name", "summary", "missing_critical_skills"]],
        column_config={
            "score": st.column_config.ProgressColumn(
                "Match Score",
                help="AI-calculated fit based on JD",
                format="%d",
                min_value=0,
                max_value=100,
            ),
            "missing_critical_skills": "Missing Skills"
        },
        use_container_width=True,
        hide_index=True,
    )

    # --- DETAILED VIEW ---
    st.markdown("---")
    st.subheader("📄 Detailed Breakdown")
    
    selected_candidate = st.selectbox("Select a Candidate", df["name"])
    
    if selected_candidate:
        # Get data for this person
        person_data = df[df["name"] == selected_candidate].iloc[0]
        
        c1, c2 = st.columns([1, 2])
        
        with c1:
            st.info(f"**Score: {person_data['score']}/100**")
            if person_data['score'] > 75:
                st.success("Recommendation: INTERVIEW ✅")
            elif person_data['score'] > 50:
                st.warning("Recommendation: REVIEW ⚠️")
            else:
                st.error("Recommendation: REJECT ❌")
        
        with c2:
            st.write(f"**Summary:** {person_data['summary']}")
            st.write(f"**Missing Skills:** {person_data['missing_critical_skills']}")
            st.caption(f"File Source: {person_data['filename']}")

else:
    st.warning("⚠️ No data found. Please run 'main.py' first to generate rankings.")
    if st.button("Run Analysis Now"):
        os.system("python main.py")
        st.rerun()