from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
TAN = "#FFF5E0"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(time_min):
    timer_countdown(time_min*60)


def timer_countdown(time_amount):
    # 1 min is 60 seconds
    # set min to input, calculate seconds
    # every 60 secs reset secs and decrement minute
    minutes = math.floor(time_amount/60)
    secs = time_amount % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if secs < 10:
        secs = f"0{secs}"
    if time_amount >= 0:
        canvas.after(1000, timer_countdown, time_amount - 1)
        canvas.itemconfig(timer_text, text=f"{minutes}:{secs}")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomo")
window.config(padx=50, pady=50, bg=TAN)

# Background
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.configure(bg=TAN)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

# UI Elements
checkmark = Label(text="✔", fg=GREEN, bg=TAN)
timer_title = Label(text="Timer", fg=GREEN, bg=TAN, font=(FONT_NAME, 35))
start_button = Button(text="Start", command=lambda: start_timer(1))
reset_button = Button(text="Reset", command=timer_reset)

# Layout
canvas.grid(row=1, column=1)
timer_title.grid(row=0, column=1)
checkmark.grid(row=3, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

window.mainloop()
