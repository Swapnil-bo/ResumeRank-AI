import os
from fpdf import FPDF

# Ensure the folder exists
if not os.path.exists("resumes"):
    os.makedirs("resumes")

def create_resume(filename, name, role, skills, experience):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    content = f"""
    Name: {name}
    Role: {role}
    
    Skills:
    {skills}
    
    Experience:
    {experience}
    """
    
    pdf.multi_cell(0, 10, content)
    pdf.output(f"resumes/{filename}")
    print(f"✅ Created: resumes/{filename}")

# --- DATA GENERATION ---
data = [
    ("resume_alice.pdf", "Alice Chen", "AI Engineer", 
     "Python, TensorFlow, SQL, Git, FastAPI, Gemini API", 
     "2 years building AI agents. Developed a chatbot for a fintech startup."),
    
    ("resume_bob.pdf", "Bob Smith", "Junior Developer", 
     "Python, HTML, CSS, Basic SQL", 
     "Fresh graduate. Completed a Python bootcamp. No commercial experience."),
    
    ("resume_charlie.pdf", "Charlie Davis", "Senior C++ Architect", 
     "C++, C#, Java, System Architecture, High-Frequency Trading", 
     "15 years experience in low-latency systems. Looking for leadership roles."),
    
    ("resume_diana.pdf", "Diana Prince", "Marketing Manager", 
     "SEO, Content Marketing, Google Ads, Copywriting", 
     "Managed a team of 10. Increased organic traffic by 200%."),
    
    ("resume_evan.pdf", "Evan Wright", "Self-Taught Programmer", 
     "JavaScript, Node.js, React, some Python", 
     "Built several freelance websites. Learning AI on weekends.")
]

print("🚀 Generating Dummy Resumes...")
for filename, name, role, skills, exp in data:
    create_resume(filename, name, role, skills, exp)

print("\n🎉 Done! You now have 5 test PDFs in the 'resumes' folder.")