import tkinter as tk
from TextQuizGame import Game


class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.master.title("Gui Quiz Game")
        self.master.geometry("800x600")

        self.label = tk.Label(master, text="Welcome in Quiz Game!", font=("Helvetica", 14))
        self.label.pack()

        self.start_button = tk.Button(master, text="Start game", font=("Helvetica", 10), command=self.show_buttons)
        self.start_button.pack()

        self.next_button = tk.Button(master, text="next", font=("Helvetica", 10), command=self.help_next)
        self.half_button = tk.Button(master, text="half", font=("Helvetica", 10), command=self.help_half)
        self.time_button = tk.Button(master, text="time", font=("Helvetica", 10), command=self.help_time)
        self.save_button = tk.Button(master, text="save game", font=("Helvetica", 10), command=self.help_save)

        self.answer_entry = tk.Entry(master, font=("Helvetica", 10))
        self.submit_button = tk.Button(master, text="Submit", font=("Helvetica", 10), command=self.submit_answer)

    def show_buttons(self):
        self.start_button.pack_forget()
        self.answer_entry.pack()
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.NE)
        self.half_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.NE)
        self.time_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.NE)
        self.save_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.NE)

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

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
