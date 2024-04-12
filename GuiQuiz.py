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

    def create_welcome_gui(self):
        self.label = tk.Label(self.master, text="Welcome! Tell us your name!", font=("Helvetica", 20))
        self.label.pack(pady=150, anchor=tk.CENTER, expand=True)

        self.name_label = tk.Label(self.master, text="Enter your name:", font=("Helvetica", 14))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.name_entry.pack()

        self.name_button = tk.Button(self.master, text="Start game", font=("Helvetica", 14), command=self.welcome_game)
        self.name_button.pack()

    def game_gui(self):
        self.start_button = tk.Button(self.master, text=" BEGIN", font=("Helvetica", 14), command=self.start_game)
        self.load_button = tk.Button(self.master, text="LOAD GAME", font=("Helvetica", 14))

        self.start_button.pack()
        self.load_button.pack()
    def help_gui(self):
        self.help_button = tk.Button(self.master, text="Help", font=("Helvetica", 14), command=self.show_help_buttons)
        self.next_button = tk.Button(self.master, text="next", font=("Helvetica", 14), command=self.help_next)
        self.half_button = tk.Button(self.master, text="half", font=("Helvetica", 14), command=self.help_half)
        self.time_button = tk.Button(self.master, text="time", font=("Helvetica", 14), command=self.help_time)
        self.save_button = tk.Button(self.master, text="save game", font=("Helvetica", 14), command=self.load_game)

    def answer_gui(self):
        answer_frame = tk.Frame(self.master)
        answer_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.answer_a_button = tk.Button(answer_frame, text="A", font=("Helvetica", 14),
                                         command=lambda: self.select_answer("A"))
        self.answer_a_button.pack(side=tk.LEFT, padx=5)
        self.answer_b_button = tk.Button(answer_frame, text="B", font=("Helvetica", 14),
                                         command=lambda: self.select_answer("B"))
        self.answer_b_button.pack(side=tk.LEFT, padx=5)
        self.answer_c_button = tk.Button(answer_frame, text="C", font=("Helvetica", 14),
                                         command=lambda: self.select_answer("C"))
        self.answer_c_button.pack(side=tk.LEFT, padx=5)
        self.answer_d_button = tk.Button(answer_frame, text="D", font=("Helvetica", 14),
                                         command=lambda: self.select_answer("D"))
        self.answer_d_button.pack(side=tk.LEFT, padx=5)

    def help_points_gui(self):
        self.help_points_label = tk.Label(self.master, text=f"Help points:{self.player_help_count} ", font=("Helvetica", 14))
        self.help_points_label.place(relx=0.95, rely=0.05, anchor=tk.NE)

    def game_points_gui(self):
        self.game_points_label = tk.Label(self.master, text=f"Score: {self.points}", font=("Helvetica", 14),)
        self.game_points_label.place(relx=0.94, rely=0.1, anchor=tk.NE)

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
                                   "You have a few options to choose for help, each using a different amount of points:\n"
                                   "next: 4 points\n"
                                   "time: 2 points\n"
                                   "half: 1 point\n"
                                   "or\n"
                                   "save: to save the game\n"
                                   "You can load your previous saved game by using LOAD GAME button\n"
                                   "Press BEGIN to start the game", font=("Helvetica", 16), pady=-10,)
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
        self.help_points_gui()
        self.game_points_gui()
        self.start_button.pack_forget()
        self.load_button.pack_forget()
        self.show_help_buttons()
        self.print_current_question(self.shuffled_questions[self.questions_count])
        self.show_answers_options()

    def select_answer(self, answer):
        self.selected_answer = answer
        self.correct_answer = self.current_question["correct"]
        if self.selected_answer == self.correct_answer:
            print("good")
        else:
            print("mo")

    def print_current_question(self, question):
        self.answers_frame = tk.Frame(self.master)
        self.answers_frame.pack(anchor=tk.CENTER)
        question_text = question["question"] + "\n"
        for option, answer in question['answers'].items():
            question_text += f"{option}. {answer}\n"

        self.question_label = tk.Label(self.master, text=question_text, font=("Helvetica", 18,"bold"), justify=tk.LEFT)
        self.question_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.selected_answer = tk.StringVar()

    def questions_shuffle(self):
        shuffled_questions = list(Questions.questions.values())
        random.shuffle(shuffled_questions)
        return shuffled_questions

    def load_game(self):
        print("load")

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
