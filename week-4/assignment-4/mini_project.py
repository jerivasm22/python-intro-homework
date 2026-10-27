
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]


top_score = 0
top_name = ""
total_score = 0
unique_subjects = set()
high_scorers = []

for student in students:
    score = student["score"]
    name = student["name"]
    subjet = student["subject"]
    if score > top_score:
        top_score = score
        top_name = name
    total_score += score
    unique_subjects.add(subjet)
    if score > 75:
        high_scorers.append(name)
class_average = total_score / len(students)

print(f"Top scorer:         {top_name} ({top_score})")
print(f"Class average:      {class_average}")
print(f"Subjects offered:   {unique_subjects}")
print(f"High scorers:       {high_scorers}")

