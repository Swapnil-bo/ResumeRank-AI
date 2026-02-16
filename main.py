import time
import os
import csv
import sys

# Ensure we can import from src regardless of where we run the script
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.utils import extract_text_from_pdf, get_pdf_files
from src.analyzer import analyze_resume

# --- ROBUST PATH SETUP ---
# Get the absolute path of the folder where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct paths relative to BASE_DIR
RESUME_FOLDER = os.path.join(BASE_DIR, "resumes")
JD_FILE = os.path.join(BASE_DIR, "job_description.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "final_rankings.csv")

def main():
    print("🚀 Starting ResumeRank AI (Robust Version)...")
    
    # 1. Debug: Print where we are looking
    print(f"📍 Looking for resumes in: {RESUME_FOLDER}")
    
    # Check if folder exists
    if not os.path.exists(RESUME_FOLDER):
        print(f"❌ CRITICAL ERROR: The folder '{RESUME_FOLDER}' does not exist.")
        print("   -> Did you create a folder named 'resumes' (lowercase)?")
        print("   -> Did you accidentally put it inside 'src'?")
        return

    # 2. Load Job Description
    try:
        with open(JD_FILE, "r", encoding="utf-8") as f:
            jd_text = f.read()
    except FileNotFoundError:
        print(f"❌ Critical Error: {JD_FILE} not found.")
        print(f"   -> Make sure 'job_description.txt' is in: {BASE_DIR}")
        return

    # 3. Find Resumes
    try:
        pdf_files = [f for f in os.listdir(RESUME_FOLDER) if f.endswith(".pdf")]
    except Exception as e:
        print(f"❌ Error accessing folder: {e}")
        return

    print(f"📂 Found {len(pdf_files)} resumes to process.")
    
    if len(pdf_files) == 0:
        print("⚠️ No PDF files found! Add some .pdf files to the 'resumes' folder.")
        return

    results = []

    # 4. Process Loop
    for filename in pdf_files:
        print(f"   Running analysis on: {filename}...", end=" ", flush=True)
        file_path = os.path.join(RESUME_FOLDER, filename)
        
        # We need to import the extraction logic from utils, 
        # but since we already imported it at top, we just use it.
        # Note: We need to make sure utils.py is actually doing the work.
        
        # Quick fix: if extract_text_from_pdf isn't working from import, 
        # we can just use the logic here for debugging, but let's trust the import first.
        from src.utils import extract_text_from_pdf 
        
        resume_text = extract_text_from_pdf(file_path)
        
        if resume_text:
            analysis = analyze_resume(resume_text, jd_text)
            
            if analysis:
                analysis['filename'] = filename
                results.append(analysis)
                print(f"✅ Score: {analysis.get('score', 0)}")
            else:
                print("❌ Analysis Failed (AI Error)")
        else:
            print("❌ Empty Text (PDF Read Error)")

    # 5. Save Results
    if results:
        results.sort(key=lambda x: x.get('score', 0), reverse=True)
        
        # specific keys based on analyzer.py output
        keys = ["score", "name", "summary", "missing_critical_skills", "email", "filename"]
        
        try:
            with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for row in results:
                    # Filter row to only include keys we defined
                    filtered_row = {k: row.get(k, "N/A") for k in keys}
                    writer.writerow(filtered_row)
                
            print(f"\n🏆 Success! {len(results)} candidates ranked.")
            print(f"📄 Results saved to: {OUTPUT_FILE}")
            
            top_candidate = results[0]
            print(f"\n🥇 Top Pick: {top_candidate.get('name', 'Unknown')} (Score: {top_candidate.get('score', 0)})")
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")

if __name__ == "__main__":
    main()