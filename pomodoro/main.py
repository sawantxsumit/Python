import tkinter as tk
from tkinter import messagebox
import time
import threading
import platform

try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

# Constants
WORK_25 = 25 * 60
BREAK_5 = 5 * 60
WORK_50 = 50 * 60
BREAK_10 = 10 * 60

ALARM_SOUND = "alarm.wav"  # Provide your own mp3 or wav

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("800x600")

        # === Background Image ===
        self.bg_image = Image.open("background.png")
        self.bg_image = self.bg_image.resize((800, 600), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.mode = "25/5"
        self.session_time = WORK_25
        self.break_time = BREAK_5
        self.running = False
        self.on_break = False
        self.timer_thread = None

        self.build_ui()

    def build_ui(self):
        self.label = tk.Label(self.root, text="Pomodoro Timer", font=("Arial", 18))
        self.label.pack(pady=10)

        self.time_label = tk.Label(self.root, text=self.format_time(self.session_time), font=("Arial", 32))
        self.time_label.pack(pady=10)

        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.pack()

        self.mode25_btn = tk.Button(self.mode_frame, text="25/5", command=lambda: self.set_mode("25/5"))
        self.mode25_btn.grid(row=0, column=0, padx=5)

        self.mode50_btn = tk.Button(self.mode_frame, text="50/10", command=lambda: self.set_mode("50/10"))
        self.mode50_btn.grid(row=0, column=1, padx=5)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        self.start_btn = tk.Button(self.btn_frame, text="Start", command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(self.btn_frame, text="Stop", command=self.stop_timer)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="Reset", command=self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def set_mode(self, mode):
        if self.running:
            return
        self.mode = mode
        if mode == "25/5":
            self.session_time = WORK_25
            self.break_time = BREAK_5
        else:
            self.session_time = WORK_50
            self.break_time = BREAK_10
        self.on_break = False
        self.time_label.config(text=self.format_time(self.session_time))

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.start()
            self.play_alarm()

    def run_timer(self):
        current_time = self.break_time if self.on_break else self.session_time

        while current_time > 0 and self.running:
            mins, secs = divmod(current_time, 60)
            self.time_label.config(text=f"{mins:02d}:{secs:02d}")
            self.root.update()
            time.sleep(1)
            current_time -= 1

        if self.running:
            self.on_break = not self.on_break
            self.play_alarm()
            self.start_timer()  # Auto-start next session/break

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.stop_timer()
        if self.mode == "25/5":
            self.session_time = WORK_25
        else:
            self.session_time = WORK_50
        self.on_break = False
        self.time_label.config(text=self.format_time(self.session_time))

    def play_alarm(self):
        if SOUND_AVAILABLE:
            threading.Thread(target=lambda: playsound(ALARM_SOUND)).start()
        else:
            print("[INFO] Alarm sound is not available. Install playsound or use platform alarm.")

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
