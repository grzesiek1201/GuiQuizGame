import time
from threading import Thread


class Timer:
    def __init__(self):
        self.start_time = None
        self.time_answer = 30
        self.paused_time = 0
        self.time_up = False
        self.print_time = True
        self.timer_thread = None

    def stop_timer(self):
        if self.start_time is not None:
            if self.paused_time > 0:
                return self.paused_time
            else:
                return time.time() - self.start_time
        else:
            return 0

    def start_timer(self):
        self.time_up = False
        self.start_time = time.time()
        self.timer_thread = Thread(target=self.player_timer)
        self.timer_thread.start()
        print("Timer started at:", self.start_time)

    def pause_timer(self):
        self.print_time = False
        print("Timer paused at:", time.time(), "Print time:", self.print_time)

    def resume_timer(self):
        self.print_time = True
        print("Timer resumed at:", time.time(), "Print time:", self.print_time)

    def restart_timer(self):
        self.start_timer()
        print("Timer restarted at:", self.start_time)
        self.start_time = None
        self.time_up = False

    def player_timer(self):
        while not self.time_up:
            time.sleep(1)
            if not self.print_time:
                continue
            remaining_time = self.time_answer - self.stop_timer()
            if remaining_time <= 30 and remaining_time > 20:
                print("30 seconds left")
            elif remaining_time <= 20 and remaining_time > 10:
                print("20 seconds left")
            elif remaining_time <= 10 and remaining_time > 0:
                print("10 seconds left")
            elif remaining_time <= 0:
                print("\nTime's up! You didn't answer the question.")
                self.time_up = True

    def add_timer(self):
        self.time_answer += 30
        print(f"+30 sec!. Current time left {self.time_answer}")
