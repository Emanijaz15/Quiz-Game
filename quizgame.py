questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "What is 5 + 7?": "12",
    "Python is a ___ language.": "programming"
}
score = 0
for q, a in questions.items():
    user = input(q + " ").strip().lower()
    if user == a:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {a}\n")

print(f"You got {score}/{len(questions)} correct.")