def calculate_score(skills):
    required_skills = ["python", "react", "sql", "ai", "machine learning"]

    score = 0

    for skill in skills:
        if skill in required_skills:
            score += 20

    if score > 100:
        score = 100

    return score
