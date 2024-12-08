from tkinter import Tk, Label, Button, Entry


def okey():
    weight = w.get()
    height = h.get()
    try:
        weight = float(weight)
        height = float(height)
        height = height / 100
        BMI = weight / height ** 2
        if BMI < 18.5:
            L1.config(text="Your weight status : Thin", fg="#00eaea")
        elif 18.5 <= BMI <= 24.9:
            L1.config(text="Your weight status : Normal", fg="#0be205")
        elif 25 <= BMI <= 29.9:
            L1.config(text="Your weight status : Overweight", fg="#ffff00")
        elif 30 <= BMI <= 34.9:
            L1.config(text="Your weight status : Fat (1)", fg="orange")
        elif 35 <= BMI <= 39.9:
            L1.config(text="Your weight status : Fat (2)", fg="orange")
        elif 40 <= BMI:
            L1.config(text="Your weight status : Fat (3)", fg="orange")
    except ValueError:
        L1.config(text="Please type your weight and height ! ", fg="red")


window = Tk()
window.config(bg="black")
Label(window, text="Welcome to 'Healthy body'", font=("bradley hand ITC", 20), bg="black", fg="gold").pack()
Label(window, text="", background="black").pack()
Label(window, text="type your information", bg="black", fg="white", font=("Segoe UI Black", 10)).pack()
Label(window, text="", background="black").pack()
Label(window, text="weight : (kg)", bg="black", fg="white", font=("Comic Sans MS", 10)).pack()
w = Entry(window)
w.pack()
Label(window, text="height : (cm)", bg="black", fg="white", font=("Comic Sans MS", 10)).pack()
h = Entry(window)
h.pack()
Label(window, text="", background="black").pack()
Button(window, text="OK", bg="green", command=okey, font=("Arial Black", 8)).pack()
Label(window, text="", background="black").pack()
L1 = Label(window, text="", bg="black", fg="white")
L1.pack()
window.title("Healthy body")
window.geometry("400x350")
window.resizable(width=False, height=False)
window.mainloop()
