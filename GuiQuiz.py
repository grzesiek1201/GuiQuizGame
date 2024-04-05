import tkinter as tk
from TextQuizGame import Game


class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.master.title("Gui Quiz Game")
        self.master.geometry("800x600")

        self.label = tk.Label(master, text="Welcome! Tell us your name!", font=("Helvetica", 12))
        self.label.pack(pady=150, anchor=tk.CENTER, expand=True)

        self.name_label = tk.Label(master, text="Enter your name:", font=("Helvetica", 12))
        self.name_label.pack()

        self.name_entry = tk.Entry(master, font=("Helvetica", 12))
        self.name_entry.pack()

        self.start_button = tk.Button(master, text="Start game", font=("Helvetica", 12), command=self.start_game)
        self.start_button.pack()

        self.help_button = tk.Button(master, text="Help", font=("Helvetica", 12), command=self.show_help_buttons)

        self.next_button = tk.Button(master, text="next", font=("Helvetica", 12), command=self.help_next)
        self.half_button = tk.Button(master, text="half", font=("Helvetica", 12), command=self.help_half)
        self.time_button = tk.Button(master, text="time", font=("Helvetica", 12), command=self.help_time)
        self.save_button = tk.Button(master, text="save game", font=("Helvetica", 12), command=self.help_save)

        self.answer_entry = tk.Entry(master, font=("Helvetica", 12))
        self.submit_button = tk.Button(master, text="Submit", font=("Helvetica", 12), command=self.submit_answer)

    def show_help_buttons(self):
        self.label.pack_forget()
        self.start_button.pack_forget()
        self.help_button.pack_forget()
        self.answer_entry.pack()
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.half_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.time_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.SE)

    def help_next(self):
        self.game.help_next()

    def help_half(self):
        self.game.help_half()

    def help_time(self):
        self.game.help_time()

    def help_save(self):
        self.game.help_save()

    def submit_answer(self):
        answer = self.answer_entry.get()
        self.game.player_input = answer
        self.game.player_choice(answer)
        self.answer_entry.delete(0, tk.END)

    def start_game(self):
        name = self.name_entry.get().strip()
        if name:
            self.game.name_input = name
            self.label.config(text=f"Welcome {name} to TextQuizGame! version 1.5\n"
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
            self.start_button.pack_forget()
            self.help_button.pack()
        else:
            tk.messagebox.showerror("Error", "Please enter your name.")


def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
