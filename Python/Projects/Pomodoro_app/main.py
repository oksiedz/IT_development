import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    count_down(5 * 60)


def reset_pomodoro():
    start_pomodoro()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(tagOrId=timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_picture = tk.PhotoImage(file="Attachments/tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_picture)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label Timer
pomodoro_timer_label = tk.Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 35, "bold"))
pomodoro_timer_label.grid(column=1, row=0)
# label checkboxes
check_label = tk.Label(fg=GREEN, bg=YELLOW, text="☑", font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

# start and reset button
start_button = tk.Button(text="Start", command=start_pomodoro, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_pomodoro, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
