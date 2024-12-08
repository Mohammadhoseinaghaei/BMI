from tkinter import *
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = "0123456789"
symbols = "`~!@#$%^&*)_+=}{:'><[]/"
al = lower + upper + number + symbols


def password_get():
    password = "".join(random.sample(al, IN.get()))
    if IN.get() < 4:
        la.config(text="error1", fg='#dd0000', font=("DejaVu Sans Mono", 13))
    elif 1000 > IN.get() > 20:
        la.config(text="Your password has too many characters", fg='#c60000', font=("DejaVu Sans Mono", 13))
    else:
        la.config(text="PASSWORD =>   {} ".format(password), fg='#000028', font=("DejaVu Sans Mono", 13))


window = Tk()
window.title("Password")
window.config(bg="gray")
Label(window, text="Strong Password", font=("Segoe UI Black", 20), fg="black", bg="gray").pack()
Label(window, text="", bg="gray").pack()
Label(window, text="", bg="gray").pack()
Label(window, text="Enter the length of password:", bg="gray", font=("Comic Sans MS", 10)).pack()
IN = IntVar()
Label(window, text="", bg="gray").pack()
password_len = Spinbox(window, from_=4, to=1000000000, width=3, textvariable=IN)
password_len.pack()
Label(window, text="", bg="gray").pack()
Label(window, text="", bg="gray").pack()
Button(window, text="Click me", command=password_get, width=10, bg="green", font=("Arial Black", 10)).pack()
Label(window, text="", bg="gray").pack()
la = Label(window, text="", bg="gray")
la.pack()

window.geometry("350x300")
window.resizable(width=True, height=False)
window.mainloop()
