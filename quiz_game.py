import random

class Question:
    def __init__(self, prompt, choices, answer_index):
        self.prompt = prompt
        self.choices = choices
        self.answer_index = answer_index

    def ask(self):
        print("\n" + self.prompt)
        shuffled_choices = self.choices[:]
        random.shuffle(shuffled_choices)
        for i, choice in enumerate(shuffled_choices, start=1):
            print(f"{i}. {choice}")

        while True:
            try:
                user_input = int(input("Select your answer (1-4): "))
                if user_input < 1 or user_input > 4:
                    raise ValueError("Selection out of range")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a number between 1 and 4.")

        selected_choice = shuffled_choices[user_input - 1]
        correct_choice = self.choices[self.answer_index - 1]

        if selected_choice == correct_choice:
            print("✅ Correct!\n")
            return True
        else:
            print(f"❌ Incorrect! The right answer was: {correct_choice}\n")
            return False

class QuizGame:
    def __init__(self, player_name, questions):
        self.player_name = player_name
        self.questions = questions
        self.score = 0

    def play(self):
        print(f"🎉 Welcome to the Quiz Challenge, {self.player_name}!\n")
        random.shuffle(self.questions)
        for question in self.questions:
            if question.ask():
                self.score += 1
        print(f"🏁 Game Over! {self.player_name}, your final score is {self.score} out of {len(self.questions)}.")

def main():
    print("Welcome to the Quiz Game!")
    name = input("Please enter your name: ")

    questions = [
        Question("What is the capital city of France?", ["London", "Berlin", "Paris", "Madrid"], 3),
        Question("Which language is primarily used for web development?", ["Python", "HTML", "C++", "Java"], 2),
        Question("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
        Question("Who authored 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], 3),
        Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
        Question("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 3),
    ]

    game = QuizGame(name, questions)
    game.play()

if __name__ == "__main__":
    main()
