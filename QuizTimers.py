import time
import threading


class Timers:
    def __init__(self):
        self.player_time = 30
        self.timer_thread = None
        self.timer_gui = None

    def start_time(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread_stop = True
            self.timer_thread.join()
        self.timer_thread_stop = False
        self.timer_thread = threading.Thread(target=self.count_down)
        self.timer_thread.start()

    def count_down(self):
        while self.player_time > 0 and not getattr(self, 'timer_thread_stop', False):
            time.sleep(1)
            self.player_time -= 1

    def stop_time(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()

    def help_add_time(self):
        self.player_time += 30

    def reset_question_timer(self):
        self.player_time = 30
