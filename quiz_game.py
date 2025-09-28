import random
import uuid

class Player:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.score = 0

    def add_score(self, mark):
        self.score += mark

class Question:
    def __init__(self, id, questionText, options, correct_index, mark):
        self.id = id
        self.questionText = questionText
        self.options = options
        self.correct_index = correct_index
        self.mark = mark

    def ask(self):
        print("\n" + self.questionText)
        shuffled_options = self.options[:]
        random.shuffle(shuffled_options)
        for i, option in enumerate(shuffled_options, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                answer = int(input("Select your answer (1-4): "))
                if answer < 1 or answer > 4:
                    raise ValueError("Choice out of range")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a number between 1 and 4.")

        selected_option = shuffled_options[answer - 1]
        correct_option = self.options[self.correct_index - 1]

        if selected_option == correct_option:
            print(f"✅ Correct! You earned {self.mark} points.\n")
            return self.mark
        else:
            print(f"❌ Wrong! The correct answer was: {correct_option}\n")
            return 0

class GameManager:
    def __init__(self, player, questions):
        self.player = player
        self.questions = questions

    def start_game(self):
        print(f"🎮 Welcome {self.player.name} to the Multiple Choice Game!\n")
        random.shuffle(self.questions)
        for question in self.questions:
            earned_mark = question.ask()
            self.player.add_score(earned_mark)
        print(f"🏆 Game Over! {self.player.name}, your final score is: {self.player.score} out of {sum(q.mark for q in self.questions)}")

def main():
    print("Welcome to the Multiple Choice Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    questions = [
        Question(1, "What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 3, 5),
        Question(2, "Which language is used for web apps?", ["Python", "HTML", "C++", "Java"], 2, 5),
        Question(3, "Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3, 5),
        Question(4, "Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], 3, 5),
        Question(5, "What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4, 5),
        Question(6, "Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 3, 5),
    ]

    game_manager = GameManager(player, questions)
    game_manager.start_game()

if __name__ == "__main__":
    main()
