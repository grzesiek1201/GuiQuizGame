import tkinter as tk
from tkinter import messagebox
import random
import Questions
from QuizTimers import Timers
from DataGame import Data
import time


class QuizGUI:
    def __init__(self, master):
        self.points = 0
        self.questions_count = 0
        self.player_help_count = 10
        self.help_extra_points = 0
        self.correct_answer = None
        self.current_question = None
        self.help_used = False
        self.timers = Timers()
        self.data_manager = Data()
        self.shuffled_questions = self.questions_shuffle()
        self.master = master
        self.master.title("Gui Quiz Game")
        self.master.geometry("800x600")
        self.selected_answer = None
        self.create_welcome_gui()


    def create_welcome_gui(self):
        self.label = tk.Label(self.master, text="Welcome! Tell us your name!", font=("Helvetica", 20), bg="lightblue")
        self.label.pack(anchor=tk.CENTER, expand=True)

        self.name_label = tk.Label(self.master, text="Enter your name:", font=("Helvetica", 14), bg="lightblue")
        self.name_label.pack(pady=0.90)

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 14), bg="lightblue")
        self.name_entry.pack(pady=0.90)

        self.name_button = tk.Button(self.master, text="Start game", font=("Helvetica", 14), command=self.welcome_game, bg="Yellow")
        self.name_button.pack()

    def game_gui(self):
        self.start_button = tk.Button(self.master, text=" BEGIN", font=("Helvetica", 14), command=self.start_game, bg="Yellow")
        self.load_button = tk.Button(self.master, text="LOAD GAME", font=("Helvetica", 14), bg="Yellow")

        self.start_button.pack(pady=0.70, anchor=tk.S)
        self.load_button.pack(pady=0.80, anchor=tk.S)

    def help_gui(self):
        self.help_button = tk.Button(self.master, text="Help", font=("Helvetica", 14), command=self.show_help_buttons, bg="Yellow")
        self.next_button = tk.Button(self.master, text="next", font=("Helvetica", 14), command=self.help_next, bg="Yellow")
        self.half_button = tk.Button(self.master, text="half", font=("Helvetica", 14), command=self.help_half, bg="Yellow")
        self.time_button = tk.Button(self.master, text="time", font=("Helvetica", 14), command=self.help_time, bg="Yellow")
        self.save_button = tk.Button(self.master, text="save game", font=("Helvetica", 14), command=self.save_game, bg="Yellow")

    def answer_gui(self):
        answer_frame = tk.Frame(self.master)
        answer_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.answer_a_button = tk.Button(answer_frame, text="A", font=("Helvetica", 14), bg="Yellow",
                                         command=lambda: self.select_answer("A"))
        self.answer_a_button.pack(side=tk.LEFT, padx=5)
        self.answer_b_button = tk.Button(answer_frame, text="B", font=("Helvetica", 14), bg="Yellow",
                                         command=lambda: self.select_answer("B"))
        self.answer_b_button.pack(side=tk.LEFT, padx=5)
        self.answer_c_button = tk.Button(answer_frame, text="C", font=("Helvetica", 14), bg="Yellow",
                                         command=lambda: self.select_answer("C"))
        self.answer_c_button.pack(side=tk.LEFT, padx=5)
        self.answer_d_button = tk.Button(answer_frame, text="D", font=("Helvetica", 14), bg="Yellow",
                                         command=lambda: self.select_answer("D"))
        self.answer_d_button.pack(side=tk.LEFT, padx=5)

    def question_answer(self):
        self.label_question_answer = tk.Label(self.master, text="Which answer you choose?",font=("Helvetica", 16), bg="lightblue")
        self.label_question_answer.place(relx=0.50, rely=0.80, anchor=tk.S)

    def help_points_gui(self):
        self.help_points_label = tk.Label(self.master, text=f"Help points:{self.player_help_count} ", font=("Helvetica", 14), bg="Yellow")
        self.help_points_label.place(relx=0.95, rely=0.05, anchor=tk.NE)

    def game_points_gui(self):
        self.game_points_label = tk.Label(self.master, text=f"Score: {self.points}", font=("Helvetica", 14), bg="Yellow")
        self.game_points_label.place(relx=0.94, rely=0.1, anchor=tk.NE)

    def after_game_gui(self):
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.exit_button = tk.Button(self.master, text="Exit", command=exit)

    def leaderboard_gui(self):
        self.data_manager.load_players_data()
        self.data_manager.leaderboard()
        leaderboard_text = "Top 10 Players:\n"
        for i, player in enumerate(self.data_manager.sorted_players[:self.data_manager.num_players], 1):
            leaderboard_text += f"{i}. {player['player']}: {player['points']} points\n"
        self.leaderboard_label = tk.Label(self.master, text=leaderboard_text, font=("Helvetica", 16), bg="lightblue")
        self.leaderboard_label.pack(anchor=tk.CENTER)

    def show_answers_options(self):
        self.answer_a_button.pack()
        self.answer_b_button.pack()
        self.answer_c_button.pack()
        self.answer_d_button.pack()

    def show_help_buttons(self):
        self.label.pack_forget()
        self.start_button.pack_forget()
        self.help_button.pack_forget()
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.half_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.time_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.SE)

    def hide_help_buttons(self):
        self.next_button.pack_forget()
        self.time_button.pack_forget()
        self.half_button.pack_forget()

    def points_label(self):
        self.label_points= tk.Label(self.master, text=f"You have run out of help points. Current help points: {self.player_help_count}",font=("Helvetica", 16), bg="lightblue")

    def help_next(self):
        if self.player_help_count < 4:
            self.points_label()
        else:
            self.player_help_count -= 4
            self.questions_count += 1
            self.label_question_answer.forget()
            self.next_label= tk.Label(self.master, text=f"Let's move to another question. Current help points: {self.player_help_count}",font=("Helvetica", 16), bg="lightblue")
            self.next_label.place(relx=0.50, rely=0.70, anchor=tk.S)
            time.sleep(2)
            self.question_answer()

    def help_half(self):
        if self.player_help_count < 1:
            self.points_label()
        else:
            self.player_help_count -= 1
            self.half_answers()
            self.help_used = True
            self.label_question_answer.forget()
            self.half_label= tk.Label(self.master, text=f"Two options left. Current help points: {self.player_help_count}",font=("Helvetica", 16), bg="lightblue")
            self.half_label.place(relx=0.50, rely=0.70, anchor=tk.S)
            time.sleep(2)
            self.question_answer()

    def help_time(self):
        if self.player_help_count < 2:
            self.points_label()
        else:
            self.player_help_count -= 2
            self.help_used = True
            self.timers.help_add_time()
            self.label_question_answer.forget()
            self.time_label= tk.Label(self.master, text=f"You have 30 seconds more to answer. Current help points: {self.player_help_count}",font=("Helvetica", 16), bg="lightblue")
            self.time_label.place(relx=0.50, rely=0.70, anchor=tk.S)
            time.sleep(2)
            self.question_answer()

    def half_answers(self):
        question = self.shuffled_questions[self.questions_count]
        correct_option = question["correct"]
        wrong_options = [option for option in question["answers"] if option != correct_option]
        random.shuffle(wrong_options)
        wrong_option = wrong_options[0]
        remaining_options = {option: answer for option, answer in question["answers"].items()
                             if option == correct_option or option == wrong_option}
        question_text = self.current_question["question"]
        print(f"Question {self.questions_count + 1}: {question_text}")
        for option, answer in remaining_options.items():
            print(f"{option}: {answer}")

    def welcome_game(self):
        self.name_input = self.name_entry.get().strip()
        if self.name_input:
            self.label_welcome= self.label.config(text=f"Welcome {self.name_input} to TextQuizGame! version 1.5\n"
                                   "You will have to answer 20 questions.\n"
                                   "You have a few options to choose for help, each using a different amount of points:\n"
                                   "next: 4 points\n"
                                   "time: 2 points\n"
                                   "half: 1 point\n"
                                   "or\n"
                                   "save: to save the game\n"
                                   "You can load your previous saved game by using LOAD GAME button\n"
                                   "Press BEGIN to start the game", font=("Helvetica", 15), pady=-10, anchor=tk.N)
            self.name_entry.delete(0, tk.END)
            self.name_label.pack_forget()
            self.name_entry.pack_forget()
            self.name_button.pack_forget()
            self.game_gui()
            self.help_gui()
        else:
            tk.messagebox.showerror("Error", "Please enter your name.")

    def start_game(self):
        self.answer_gui()
        self.question_answer()
        self.help_points_gui()
        self.game_points_gui()
        self.start_button.pack_forget()
        self.load_button.pack_forget()
        self.show_help_buttons()
        self.print_current_question(self.shuffled_questions[self.questions_count])
        self.show_answers_options()

    def select_answer(self, answer):
        time.sleep(3)
        self.selected_answer = answer
        self.correct_answer = self.current_question["correct"]
        if self.selected_answer == self.correct_answer:
            self.good_label= tk.Label(self.master, text="Yes! That is correct answer!")

        else:
            self.bad_label = tk.Label(self.master, text="Wrong! You lose!")
            self.after_game_gui()

    def correct_player_answer(self):
        self.correct_answer = self.current_question["correct"]

    def player_answer(self):
        self.current_question = self.shuffled_questions[self.questions_count]
        self.correct_player_answer()
        if self.help_used == True:
            self.player_input = input("Which answer is correct?: ")
        else:
            self.print_current_question()
            self.player_input = input("Which answer is correct?: ")
            self.help_used = False

    def next_question(self):
        if self.questions_count < len(self.shuffled_questions):
            self.current_question = self.shuffled_questions[self.questions_count]
            self.correct_player_answer()
        else:
            self.win_game()

    def print_current_question(self, question):
        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack(anchor=tk.CENTER)
        question_text = question["question"] + "\n"
        for option, answer in question['answers'].items():
            question_text += f"{option}. {answer}\n"

        self.question_label = tk.Label(self.master, text=question_text, font=("Helvetica", 18,"bold"), justify=tk.LEFT,bg="lightblue")
        self.question_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.selected_answer = tk.StringVar()

    def questions_shuffle(self):
        shuffled_questions = list(Questions.questions.values())
        random.shuffle(shuffled_questions)
        return shuffled_questions

    def save_game(self):
        self.data_manager.update_player(
            self.name_input,
            self.points,
            current_question=self.questions_count,
            current_help=self.player_help_count
        )
        self.data_manager.save_game_state(self.name_input, self.points, self.questions_count, self.player_help_count)

    def load_game(self):
        self.save_input = input("Would you like to load your last saved game? (YES/NO): ")
        if self.save_input.lower() == "yes":
            self.name_input = input("Enter your name: ")
            game_state = self.data_manager.load_game_state(self.name_input)
            if game_state is not None:
                self.points = game_state["points"]
                self.questions_count = game_state["currentQuestion"]
                self.player_help_count = game_state["currentHelp"]
                print("Game loaded successfully.")
            else:
                print("No saved game state found for this player.")
        elif self.save_input.lower() == "no":
            pass

    def restart_game(self):
        self.data_manager.reset_player_data(self.name_input)

    def extra_points(self):
        self.help_extra_points = self.player_help_count * 2
        self.points = self.help_extra_points + self.points


def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
