import tkinter as tk
from tkinter import messagebox
import random
import Questions
from QuizTimers import Timers
from DataGame import Data


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
        self.game_gui()
        self.help_gui()
        self.answer_gui()

    def create_welcome_gui(self):
        self.label = tk.Label(self.master, text="Welcome! Tell us your name!", font=("Helvetica", 12))
        self.label.pack(pady=150, anchor=tk.CENTER, expand=True)

        self.name_label = tk.Label(self.master, text="Enter your name:", font=("Helvetica", 12))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.name_entry.pack()

        self.name_button = tk.Button(self.master, text="Start game", font=("Helvetica", 12), command=self.welcome_game)
        self.name_button.pack()

    def game_gui(self):
        self.start_button = tk.Button(self.master, text=" BEGIN", font=("Helvetica", 12), command=self.start_game)
        self.load_button = tk.Button(self.master, text="LOAD GAME",font=("Helvetica", 12))

    def help_gui(self):
        self.help_button = tk.Button(self.master, text="Help", font=("Helvetica", 12), command=self.show_help_buttons)
        self.next_button = tk.Button(self.master, text="next", font=("Helvetica", 12), command=self.help_next)
        self.half_button = tk.Button(self.master, text="half", font=("Helvetica", 12), command=self.help_half)
        self.time_button = tk.Button(self.master, text="time", font=("Helvetica", 12), command=self.help_time)
        self.save_button = tk.Button(self.master, text="save game", font=("Helvetica", 12), command=self.load_game)

    def answer_gui(self):
        self.answer_a_button = tk.Button(self.master, text="A", font=("Helvetica", 12), command=lambda: self.select_answer("A"))
        self.answer_b_button = tk.Button(self.master, text="B", font=("Helvetica", 12), command=lambda: self.select_answer("B"))
        self.answer_c_button = tk.Button(self.master, text="C", font=("Helvetica", 12), command=lambda: self.select_answer("C"))
        self.answer_d_button = tk.Button(self.master, text="D", font=("Helvetica", 12), command=lambda: self.select_answer("D"))

    def help_points_gui(self):
        self.help_points_label = tk.Label(self.master, text=f"Help points:{self.player_help_count} ", font=("Helvetica", 12))
        self.help_points_label.place(relx=0.95, rely=0.05, anchor=tk.NE)

    def game_points_gui(self):
        self.game_points_label = tk.Label(self.master, text=f"Score: {self.points}", font=("Helvetica", 12))
        self.game_points_label.place(relx=0.95, rely=0.1, anchor=tk.NE)

    def show_question(self, question):
        self.label.config(text=question, font=("Helvetica", 12))
        self.label.pack(anchor=tk.CENTER)

    def show_answers_options(self):
        self.answer_a_button.pack(anchor=tk.S)
        self.answer_b_button.pack(anchor=tk.S)
        self.answer_c_button.pack(anchor=tk.S)
        self.answer_d_button.pack(anchor=tk.S)

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

    def help_next(self):
        self.help_next()
        self.hide_help_buttons()

    def help_half(self):
        self.help_half()
        self.hide_help_buttons()

    def help_time(self):
        self.help_time()
        self.hide_help_buttons()

    def welcome_game(self):
        self.name_input = self.name_entry.get().strip()
        if self.name_input:
            self.label.config(text=f"Welcome {self.name_input} to TextQuizGame! version 1.5\n"
                                   "You will have to answer 20 questions.\n"
                                   "Of course, if you have trouble, you can ask for help by using the HELP button.\n"
                                   "You have a few options to choose for help, each using a different amount of points:\n"
                                   "next: 4 points\n"
                                   "time: 2 points\n"
                                   "half: 1 point\n"
                                   "or\n"
                                   "save: to save the game\n"
                                   f"Your total points: ", font=("Helvetica", 12))
            self.name_entry.delete(0, tk.END)
            self.name_label.pack_forget()
            self.name_entry.pack_forget()
            self.name_button.pack_forget()
            self.start_button.pack()
            self.load_button.pack()
            self.help_points_gui()
            self.game_points_gui()
        else:
            tk.messagebox.showerror("Error", "Please enter your name.")

    def start_game(self):
        self.start_button.pack_forget()
        self.load_button.pack_forget()
        self.show_help_buttons()
        self.show_question(self.shuffled_questions[self.questions_count])
        self.show_answers_options()

    def select_answer(self, answer):
        self.selected_answer = answer
        self.correct_answer = self.current_question["correct"]
        if self.selected_answer == self.correct_answer:
            print("good")
        else:
            print("mo")

    def print_current_question(self, question):
        self.label.config(text=question["question"])

        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack()

        self.selected_answer = tk.StringVar()

        for option, answer in question['answers'].items():
            answer_button = tk.Radiobutton(self.answers_frame, text=answer, font=("Helvetica", 12),
                                           variable=self.selected_answer, value=option)
            answer_button.grid()

        submit_button = tk.Button(self.master, text="Submit", font=("Helvetica", 12), command=self.submit_answer)
        submit_button.pack(pady=10, row=0)

    def questions_shuffle(self):
        shuffled_questions = list(Questions.questions.values())
        random.shuffle(shuffled_questions)
        return shuffled_questions

    def correct_player_answer(self):
        self.correct_answer = self.current_question["correct"]

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

    def load_game(self):
        print("load")

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
