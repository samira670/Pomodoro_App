from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEXT = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 1

# Initialize remaining_time variable
remaining_time = 0
timer_running = False

# Timer Reset Function
def timer_reset():
    global remaining_time, REP, timer_running
    REP = 1
    remaining_time = 0
    canvas.itemconfig(canvas_text, text="00:00")
    timer_running = False

# Timer Mechanism
def start_timer():
    global REP, remaining_time, timer_running
    SHORT_BREAK_SEC = 60 * SHORT_BREAK_MIN
    LONG_BREAK_SEC = 60 * LONG_BREAK_MIN
    WORK_SEC = WORK_MIN * 60
    timer_running = True
    if REP == 1 or REP == 3 or REP == 5 or REP == 7:
        remaining_time = WORK_SEC
        count_down()
    elif REP == 2 or REP == 4 or REP == 6:
        remaining_time = SHORT_BREAK_SEC
        if REP == 4:
            label.config(text=TEXT+TEXT)
        if REP == 6:
            label.config(text=TEXT + TEXT+TEXT)
        count_down()
    elif REP == 8:
        remaining_time = LONG_BREAK_SEC
        label.config(text=TEXT + TEXT+TEXT+TEXT)
        count_down()

# Countdown Mechanism
def count_down():
    global REP, remaining_time
    if remaining_time > 0 and timer_running:
        count_min = remaining_time // 60
        count_sec = remaining_time % 60
        canvas.itemconfig(canvas_text, text=f"{count_min:02}:{count_sec:02}")
        remaining_time -= 1
        canvas.after(1000, count_down)
    elif timer_running:
        REP += 1
        start_timer()

# UI Setup
window = Tk()
window.config(padx=100, pady=50)
window.title("Pomodoro")

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
window.config(bg=YELLOW)

button_start = Button(text="Start", bg=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", bg=YELLOW, command=timer_reset)
button_reset.grid(row=2, column=2)

label = Label(fg=GREEN, bg=YELLOW)
label_text = label.config(text=TEXT)
label.grid(row=3, column=1)

window.mainloop()
