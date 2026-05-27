def calculate_ats_score(skills, text):
    required_skills = ["python", "react", "sql", "machine learning", "ai"]

    score = 0

    # Skill match (60%)
    matched = 0
    for skill in required_skills:
        if skill in skills:
            matched += 1

    skill_score = (matched / len(required_skills)) * 60

    # Keyword match (20%)
    keywords = ["project", "experience", "developed", "team"]
    keyword_count = sum(1 for k in keywords if k in text.lower())
    keyword_score = (keyword_count / len(keywords)) * 20

    # Basic formatting assumption (20%)
    format_score = 20 if len(text) > 500 else 

    score = skill_score + keyword_score + format_score

    return int(score)
