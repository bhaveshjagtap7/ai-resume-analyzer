from flask import Flask, request, jsonify
import os
from resume_parser import extract_text
from skill_extractor import extract_skills
from scoring import calculate_score
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return "AI Resume Analyzer Running"

@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["resume"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    skills = extract_skills(text)

    return jsonify({
        "skills": skills,
        "message": "Resume analyzed successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)

    score = calculate_score(skills)
    