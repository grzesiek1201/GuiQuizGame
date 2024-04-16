import time
import threading


class Timers:
    def __init__(self):
        self.player_time = 30
        self.time_up = False
        self.timer_thread = None

    def start_time(self):
        self.timer_thread = threading.Thread(target=self.count_down)
        self.timer_thread.start()

    def count_down(self):
        while self.player_time > 0:
            time.sleep(1)
            self.player_time -= 1
            minutes = self.player_time // 60
            seconds = self.player_time % 60
            self.formatted_time = f"{minutes:02d}:{seconds:02d}"
        else:
            time.sleep(1)

    def stop_time(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()

    def help_add_time(self):
        self.player_time += 30

    def reset_timer(self):
        self.player_time = 30
        self.time_up = False
        self.timer_thread = None

    def reset_question_timer(self):
        self.player_time = 30

