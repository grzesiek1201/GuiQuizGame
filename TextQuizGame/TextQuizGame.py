
from QuizTimers import Timer
from GameHandling import GameHandler


class Game:
    def __init__(self):
        self.points = 0
        self.questions_count = 0
        self.player_help_count = 10
        self.timer = Timer()
        self.GameHandler = GameHandler()

    def player_choice(self, player_input):
        timer = Timer()
        timer.start_timer()

        if player_input.lower() in ["a", "b", "c", "d"]:
            if player_input == self.GameHandler.correct_answer:
                if timer.stop_timer() <= 20:
                    self.points += 2
                    print("Correct! Good Job! You earned 2 points for being very fast!")
                else:
                    self.points += 1
                    print("Correct! Good Job! You earned 1 point.")
            else:
                print(f"Incorrect answer. The correct answer was {self.GameHandler.correct_answer}.")
                self.timer.stop_timer()
                self.lose_game()
        elif player_input.lower() == "help":
            self.timer.stop_timer()
            self.player_help_logic()
        else:
            print("Invalid input. Please enter a, b, c, d, or help.")
            return

        self.questions_count += 1
        self.GameHandler.current_question = None

    def player_help_logic(self):
        input_help = input("Choose what kind of help would you like to use? (next/half/time): ")
        if input_help.lower() == "next":
            if self.player_help_count < 4:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                print(f"Let's move to another question. Current help points: {self.player_help_count}")
                self.player_help_count -= 4
                self.questions_count += 1

        elif input_help.lower() == "half":
            if self.player_help_count < 1:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                self.player_help_count -= 1
                self.GameHandler.half_answers()
                print(f"One random wrong answer has been removed. Current help points: {self.player_help_count} ")

        elif input_help.lower() == "time":
            if self.player_help_count < 2:
                print(f"You have run out of help points. Current help points: {self.player_help_count}")
            else:
                self.player_help_count -= 2
                self.timer.add_timer()
                print(f"You have 30 seconds more to answer. Current help points: {self.player_help_count}")

        self.timer.resume_timer()

    def restart_game(self):
        game = Game()
        game.run_game()
        self.timer.restart_timer()

    def lose_game(self):
        print(f"Game over! You scored {self.points} points.")
        self.timer.stop_timer()

        while True:
            restart_input = input('Type "restart" to try again, or "exit" to quit: ')
            if restart_input.lower() == "restart":
                self.restart_game()
            elif restart_input.lower() == "exit":
                exit()
            else:
                print("Invalid input. Please type 'restart' to try again or 'exit' to quit.")

    def win_game(self):
        if self.questions_count == 20:
            print("Congratulations! You won! ")
            if self.points >= 40:
                print(f"You have incredible knowledge about programming! You have earned {self.points} points.")
            elif self.points >= 30:
                print(f"Very Good. You have earned {self.points} points.")
            elif self.points >= 20:
                print(f"Not bad. You have earned {self.points} points.")
            elif self.points >= 10:
                print(f"Keep learning and improving. You have earned {self.points} points.")
            exit()

    def run_game(self):
        self.GameHandler.welcome_message()
        while self.questions_count < 20:
            print("Entering loop in run_game method")
            self.GameHandler.printing_question()
            self.GameHandler.correct_player_answer()
            player_input = input("Which answer is correct?: ")
            if player_input.lower() == "help":
                self.player_help_logic()
                continue
            self.player_choice(player_input)
            if self.timer.time_up:
                self.lose_game()
