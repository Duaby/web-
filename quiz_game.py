def ask_question(question, options, correct_index):
    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    try:
        answer = int(input("Your choice (1-4): "))
        if answer < 1 or answer > 4:
            raise ValueError("Choice out of range")
        if answer == correct_index:
            print("✅ Correct!\n")
            return True
        else:
            print(f"❌ Wrong! The correct answer was: {options[correct_index - 1]}\n")
            return False
    except ValueError as e:
        print(f"⚠️ Invalid input: {e}")
        print("Please enter a number between 1 and 4.")
        return False

def main():
    print("🎮 Welcome to the Multiple Choice Game!\n")
    name = input("Enter your name: ")
    score = 0

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct": 3
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["Python", "HTML", "C++", "Java"],
            "correct": 2
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Venus", "Mars", "Jupiter"],
            "correct": 3
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
            "correct": 3
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct": 4
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "correct": 3
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct"]):
            score += 1

    print(f"\n🎉 Game Over, {name}! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
