import random
import Questions


class Game:
    def __init__(self):
        self.points = 0
        self.questions_count = 0
        self.player_help_count = 10
        self.correct_answer = None
        self.current_question = None

    def welcome_message(self):
        while True:
            self.name_input = input("Hello! Tell us your name:")
            if self.name_input.strip():
                break
            else:
                print("Please enter a valid name.")
        message = (
            f"Welcome {self.name_input} in TextQuizGame! version 1.3a\n"
            "You will have to answer 20 questions.\n"
            "Of course, if you will have a trouble, you can ask for help by typing HELP.\n"
            "You have few options to choose for help, they are using different amount of points, which are:\n"
            "next: 4 points\n"
            "time: 2 points\n"
            "half: 1 point\n"
            f"Your total points: {self.player_help_count} \n"
        )
        print(message)
        input("Press ENTER to start the game...")

    def questions_shuffle(self):
        shuffled_questions = list(Questions.questions.values())
        random.shuffle(shuffled_questions)
        return shuffled_questions

    def correct_player_answer(self):
        self.correct_answer = self.current_question["correct"]

    def half_answers(self):
        question = self.questions_shuffle()[self.questions_count]
        correct_option = question["correct"]
        wrong_options = [option for option in question["answers"] if option != correct_option]
        random.shuffle(wrong_options)
        wrong_option = wrong_options[0]
        remaining_options = [option for option in question["answers"] if
                             option == correct_option or option == wrong_option]
        new_answers = {option: question["answers"][option] for option in remaining_options}
        question["answers"] = new_answers
        print(f"There are two options left: {', '.join(remaining_options)}")

    def printing_question(self):
        shuffled_questions = self.questions_shuffle()
        self.current_question = shuffled_questions[self.questions_count]
        self.correct_player_answer()
        question_text = self.current_question["question"]
        print(f"Question {self.questions_count + 1}: {question_text}")
        for option, answer in self.current_question['answers'].items():
            print(f"{option}: {answer}")

    def lose_game(self):
        print(f"Game over! You scored {self.points} points.")
        while True:
            restart_input = input('Type "restart" to try again, or "exit" to quit: ')
            if restart_input.lower() == "restart":
                self.run_game()
                break
            elif restart_input.lower() == "exit":
                exit()
            else:
                print("Invalid input. Please type 'restart' to try again or 'exit' to quit.")

    def win_game(self):
        print("Congratulations! You won!")
        print(f"You scored {self.points} points.")
        if self.points >= 40:
            print("You have incredible knowledge about programming!")
        elif self.points >= 30:
            print("Very Good.")
        elif self.points >= 20:
            print("Not bad.")
        elif self.points >= 10:
            print("Keep learning and improving.")

    def player_choice(self, player_input=""):
        while self.questions_count < 20:
            if not player_input.strip():
                print("Please enter a valid input.")
                self.printing_question()
                player_input = input("Which answer is correct?: ")
                continue

            if player_input.lower() in ["a", "b", "c", "d"]:
                if player_input == self.correct_answer:
                    self.points += 1
                    self.questions_count += 1
                    print("Correct! Good Job! You earned 1 point.")
                else:
                    print(f"Incorrect answer. The correct answer was {self.correct_answer}.")
                    self.lose_game()
                if self.questions_count < 20:
                    self.printing_question()
                    player_input = input("Which answer is correct?: ")
            elif player_input.lower() == "help":
                self.player_help_logic()
                # If player used 'half' help, ask for input again
                if self.questions_count < 20 and self.player_help_count >= 0:
                    self.printing_question()
                    player_input = input("Which answer is correct?: ")
            else:
                print("Invalid input. Please enter a, b, c, d, or help.")
        if self.questions_count == 20:
            self.win_game()

    def player_help_logic(self):
        input_help = input("Choose what kind of help would you like to use? (next/half/time): ")
        if input_help.lower() == "next":
            if self.player_help_count < 4:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                self.player_help_count -= 4
                self.questions_count += 1
                print(f"Let's move to another question. Current help points: {self.player_help_count}")
                self.player_choice("")

        elif input_help.lower() == "half":
            if self.player_help_count < 1:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                self.player_help_count -= 1
                self.half_answers()
                print(f"One random wrong answer has been removed. Current help points: {self.player_help_count} ")
                self.player_choice("")

        elif input_help.lower() == "time":
            if self.player_help_count < 2:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                self.player_help_count -= 2
                print(f"You have 30 seconds more to answer. Current help points: {self.player_help_count}")
                self.player_choice("")

    def run_game(self):
        self.points = 0
        self.questions_count = 0
        self.player_help_count = 10
        self.correct_answer = None
        self.current_question = None
        self.welcome_message()
        self.player_choice("")
