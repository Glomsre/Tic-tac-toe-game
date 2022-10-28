from tkinter import *
from tkinter import messagebox

# ---------------------------- CHECK BUTTON PRESSED ------------------------------- #
val = 0


def button_pressed(button_press):
    global val

    if val == 0:
        button_press["text"] = "X"
        val = 1
        button_press["state"] = "disabled"
        win(button_press["text"], p1)

    elif val == 1:
        button_press["text"] = "O"
        val = 0
        button_press["state"] = "disabled"
        win(button_press["text"], p2)


# ---------------------------- PLAYERS ------------------------------- #
p1 = 'Player 1'
p2 = 'Player 2'


def current_player(p):
    if p == p1:
        x = 0
        return x
    elif p == p2:
        o = 1
        return o


# ---------------------------- CHECK WIN ------------------------------- #
def win(s, p):
    global btn

    if btn[0]['text'] == s and btn[1]['text'] == s and btn[2]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()
    elif btn[3]['text'] == s and btn[4]['text'] == s and btn[5]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()
    elif btn[6]['text'] == s and btn[7]['text'] == s and btn[8]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()

    if btn[0]['text'] == s and btn[3]['text'] == s and btn[6]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()
    elif btn[1]['text'] == s and btn[4]['text'] == s and btn[7]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()
    elif btn[2]['text'] == s and btn[5]['text'] == s and btn[8]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()

    if btn[0]['text'] == s and btn[4]['text'] == s and btn[8]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()
    elif btn[2]['text'] == s and btn[4]['text'] == s and btn[6]['text'] == s:
        messagebox.showinfo(title="Result", message=f"{p} WIN !")
        reset()


# ---------------------------- RESET GAME ------------------------------- #
def reset():

    for i in range(0, len(btn)):
        btn[i]['state'] = "normal"
        btn[i]['text'] = "*"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("TIC-TAC-TOE")
window.config(padx=50, pady=50)

b0 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b0))
b0.grid(row=2, column=1)
b1 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b1))
b1.grid(row=2, column=3, columnspan=2)
b2 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b2))
b2.grid(row=2, column=5)

b3 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b3))
b3.grid(row=3, column=1)
b4 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b4))
b4.grid(row=3, column=3, columnspan=2)
b5 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b5))
b5.grid(row=3, column=5)

b6 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b6))
b6.grid(row=4, column=1)
b7 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b7))
b7.grid(row=4, column=3, columnspan=2)
b8 = Button(width=7, height=3, text="*", command=lambda: button_pressed(b8))
b8.grid(row=4, column=5)

btn = [b0, b1, b2, b3, b4, b5, b6, b7, b8]


window.mainloop()
