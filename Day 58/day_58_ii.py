import time
import tkinter as tk

session_count = 0

# Create main window
window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("300x300")

# Add a label for Timer
timer_label = tk.Label(window, text="25:00", font=("Arial", 40))
timer_label.pack(pady=50)

# create start button
def start_timer():
    global session_count
    if session_count % 2 == 0:
        countdown(25 * 60) # work session
    elif session_count % 8 == 7:
        countdown(15 * 60) # long break
    else :
        countdown(5 * 60) # short break
    session_count += 1

start_button = tk.Button(window, text="Start", command=start_timer, font=("Arial", 16))
start_button.pack()

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        window.after(1000, countdown, seconds-1)
    else:     
        print("Times Up!")