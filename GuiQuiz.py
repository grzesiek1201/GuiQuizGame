import tkinter as tk
from tkinter import messagebox
import random
import Questions
from QuizTimers import Timers
from DataGame import Data


class QuizGUI:
    def __init__(self, master):
        self.data_manager = Data()
        self.points = 0
        self.questions_count = 0
        self.player_help_count = 10
        self.help_extra_points = 0
        self.correct_answer = None
        self.current_question = None
        self.shuffled_questions = self.questions_shuffle()
        self.help_used = False
        self.timers = Timers()
        self.master = master
        self.master.title("Gui Quiz Game")
        self.master.geometry("800x600")
        self.selected_answer = None

        self.create_welcome_gui()
        self.game_gui()
        self.help_gui()
        self.answer_gui()
        self.after_game_gui()
        self.timer_running = False


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
        self.start_button = tk.Button(self.master, text=" BEGIN", font=("Helvetica", 12), command= self.start_game)

        self.load_player_label= tk.Label(self.master,text="Would you like to load your last saved game?", font=("Helvetica", 12))
        self.yes_load_button= tk.Button(self.master, text= "YES")
        self.no_load_button= tk.Button(self.master, text="NO")

    def timer_gui(self):
        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.timer_label.place(relx=0.9, rely=0.05, anchor=tk.CENTER)

    def help_gui(self):
        self.help_button = tk.Button(self.master, text="Help", font=("Helvetica", 12), command=self.show_help_buttons)
        self.next_button = tk.Button(self.master, text="next", font=("Helvetica", 12), command=self.help_next)
        self.half_button = tk.Button(self.master, text="half", font=("Helvetica", 12), command=self.help_half)
        self.time_button = tk.Button(self.master, text="time", font=("Helvetica", 12), command=self.help_time)
        self.save_button = tk.Button(self.master, text="save game", font=("Helvetica", 12))

    def answer_gui(self):
        self.answer_a_button = tk.Button(self.master, text="A", font=("Helvetica", 12), command=lambda: self.select_answer("A"))
        self.answer_b_button = tk.Button(self.master, text="B", font=("Helvetica", 12), command=lambda: self.select_answer("B"))
        self.answer_c_button = tk.Button(self.master, text="C", font=("Helvetica", 12), command=lambda: self.select_answer("C"))
        self.answer_d_button = tk.Button(self.master, text="D", font=("Helvetica", 12), command=lambda: self.select_answer("D"))

    def after_game_gui(self):
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.exit_button = tk.Button(self.master, text="Exit", command=exit)

    def help_points_gui(self):
        self.help_points_label = tk.Label(self.master,text=f"Help points:{self.player_help_count} ")

    def game_points_gui(self):
        self.game_points_label= tk.Label(self.master, text=f"Score: {self.points}")

    def start_timer(self):
        self.timer_running = True
        self.master.after(30000, self.timer_finished)

    def timer_finished(self):
        self.timer_running = False
        # przegrana kod
        print("Timer finished!")

    def show_load_game(self):
        self.load_player_label.pack()

    def restart_game(self):
        self.data_manager.reset_player_data(self.name_input)


    def select_answer(self, answer):
        self.selected_answer = answer

    def show_question(self, question):
        self.label.config(text=question)

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
                                   "Of course, if you have trouble, you can ask for help by using the HELP button.\n"
                                   "You have a few options to choose for help, each using a different amount of points:\n"
                                   "next: 4 points\n"
                                   "time: 2 points\n"
                                   "half: 1 point\n"
                                   "or\n"
                                   "save: to save the game\n"
                                   f"Your total points:", font=("Helvetica", 12))
            self.name_entry.delete(0, tk.END)
            self.name_label.pack_forget()
            self.name_entry.pack_forget()
            self.name_button.pack_forget()
            self.start_button.pack()
        else:
            tk.messagebox.showerror("Error", "Please enter your name.")

    def start_game(self, question):
        self.show_question(question)

    def questions_shuffle(self):
        shuffled_questions = list(Questions.questions.values())
        random.shuffle(shuffled_questions)
        return shuffled_questions

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
