import random
import Questions
from QuizTimers import Timer


class GameHandler:
    def __init__(self):
        self.questions_count = 0
        self.player_help_count = 10
        self.correct_answer = None
        self.current_question = None
        self.QuizTimers = Timer()

    def welcome_message(self):
        self.name_input = input("Hello! Tell us your name:")
        message = (
            f"Welcome {self.name_input} in TextQuizGame! version 1.2\n"
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

    def printing_question(self):
        if not self.current_question:
            shuffled_questions = self.questions_shuffle()
            self.current_question = shuffled_questions[self.questions_count]
            question_text = self.current_question["question"]
            print(f"Question {self.questions_count + 1}: {question_text}")
            self.QuizTimers.start_timer()
            print("print_time in printing_question:", self.QuizTimers.print_time)
            for option, answer in self.current_question['answers'].items():
                print(f"{option}: {answer}")

    def correct_player_answer(self):
        self.correct_answer = self.questions_shuffle()[self.questions_count]["correct"]

    def half_answers(self):
        question = self.questions_shuffle()[self.questions_count]
        correct_option = question["correct"]
        wrong_options = [option for option in question["answers"] if option != correct_option]
        random.shuffle(wrong_options)
        wrong_option = wrong_options[0]
        remaining_options = [correct_option, wrong_option]
        question["answers"] = {option: question["answers"][option] for option in remaining_options}
        print(f"There is two options left: {correct_option} or {wrong_option}")
