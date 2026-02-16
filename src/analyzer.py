import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Client (Fast & Clean)
client = genai.Client(api_key=API_KEY)

def analyze_resume(resume_text, jd_text):
    prompt = f"""
    You are a Tech Recruiter.
    Job: {jd_text}
    Candidate: {resume_text}
    
    Output strictly valid JSON:
    {{
        "name": "Name",
        "score": 0-100,
        "summary": "1 sentence verdict",
        "missing_critical_skills": ["Skill1", "Skill2"]
    }}
    """
    
    try:
        # WE ARE SWITCHING BACK TO YOUR MODEL HERE
        response = client.models.generate_content(
            model="models/gemini-2.5-flash", 
            contents=prompt
        )
        
        # Clean the response instantly
        text = response.text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[-1].replace("```", "")
            
        return json.loads(text)
        
    except Exception as e:
        # If 2.5 fails, we fallback to 1.5-flash automatically (Safety net)
        try:
            print(f"⚠️ 2.5 failed, retrying with 1.5-flash...")
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents=prompt
            )
            text = response.text.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[-1].replace("```", "")
            return json.loads(text)
        except:
            return None