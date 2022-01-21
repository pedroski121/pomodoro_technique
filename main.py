from tkinter import *
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
check_mark = []
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps 
    global check_mark
    global timer_text
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text,text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    reps = 0
    check_mark = []

    

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps 
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps==7:
        label_timer.config(text="Work", fg = GREEN)
        count_down(work_sec)
    elif reps == 8:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        label_timer.config(text="Break", fg = PINK)
        count_down(short_break_sec)
    else:
        pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count == 0:
        start_timer()
        if reps % 2 == 0:
            check_mark.append('✔')
            check_marks = ' '.join([str(check) for check in check_mark])
            label_mark.config(text = check_marks)
    if count_sec != "00" and count_sec < 10 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        timer = window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


label_start = Button(text="Start", bg=YELLOW, bd=0, command=start_timer)
label_start.grid(column=0, row=2)

label_reset = Button(text="Reset", bg=YELLOW, bd=0, command=reset_timer)
label_reset.grid(column=2, row=2)

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)

label_mark = Label( fg=GREEN)
label_mark.grid(column=1, row=3)


window.mainloop()
