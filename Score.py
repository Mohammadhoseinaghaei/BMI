from tkinter import *


def ok():
    try:
        farsi_3 = float(farsi.get())
        dini_3 = float(dini.get())
        zist_3 = float(zist.get())
        english_3 = float(english.get())
        shimi_3 = float(shimi.get())
        arabi_3 = float(arabi.get())
        riazi_3 = float(riazi.get())
        fizik_3 = float(fizik.get())
        behdasht_3 = float(behdasht.get())
        hoviyat_3 = float(hoviyat.get())
        if farsi_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif dini_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif zist_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif english_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif shimi_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif arabi_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif riazi_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif fizik_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif behdasht_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        elif hoviyat_3 > 20:
            value_moadel.config(text="!نمیتوانید نمره بالاتر از 20 وارد کنید", font=("Segoe UI Semibold", 15),fg="#400000")
        else:
            lessons = (farsi_3 * 18.64) + (dini_3 * 14.23) + (zist_3 * 15.11) + (english_3 * 10.17) + (
                    shimi_3 * 12.46) + (
                              arabi_3 * 7.80) + (riazi_3 * 8.65) + (fizik_3 * 7.78) + (behdasht_3 * 2.96) + (
                              hoviyat_3 * 2.20)
            gtp = lessons / 100
            value_moadel.config(text="معدل: {:.4}".format(gtp), fg="#e7f209", font=("Segoe UI Semibold", 19))
    except ValueError:
        value_moadel.config(text="!لطفا اطلاعات را صحیح، وارد نمایید", fg="#400000", font=("Segoe UI Semibold", 15))


window = Tk()
window.config(background="#0145b6")
window.title("GPT calculation")
window.geometry("500x600")
window.resizable(width=False, height=False)
Label(window, text="«به برنامه محاسبه معدل خوش آمدید»", font=("Segoe UI Semibold", 20), fg="#fb6a00",
      bg="#0145b6").pack()
Label(window, text="", bg="#0145b6").pack()
Label(window, text=":برای محاسبه معدل کل، نمره های خود را وارد کنید", bg="#0145b6", font=("Segoe UI Semibold", 10),
      fg="white").pack(anchor=NE)
Label(window, text="فارسی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=445, y=120)
farsi = Entry(window, width=8)
farsi.place(x=438, y=150)
Label(window, text="دین و زندگی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=224, y=120)
dini = Entry(window, width=15)
dini.place(x=214, y=150)
Label(window, text="زیست", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=20, y=120)
zist = Entry(window, width=8)
zist.place(x=13, y=150)
Label(window, text="زبان", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=455, y=200)
english = Entry(window, width=5)
english.place(x=452, y=230)
Label(window, text="شیمی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=240, y=200)
shimi = Entry(window, width=8)
shimi.place(x=233, y=230)
Label(window, text="عربی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=20, y=200)
arabi = Entry(window, width=8)
arabi.place(x=11, y=230)
Label(window, text="ریاضی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=445, y=280)
riazi = Entry(window, width=8)
riazi.place(x=438, y=310)
Label(window, text="فیزیک", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=240, y=280)
fizik = Entry(window, width=8)
fizik.place(x=233, y=310)
Label(window, text="سلامت و بهداشت", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=10, y=280)
behdasht = Entry(window, width=15)
behdasht.place(x=13, y=310)
Label(window, text="هویت اجتماعی", bg="#0145b6", font=("Segoe UI Semibold", 10)).place(x=405, y=360)
hoviyat = Entry(window, width=15)
hoviyat.place(x=401, y=390)
Button(window, width=10, bg="green", text="محاسبه", command=ok, font=("Segoe UI Semibold", 10)).place(x=220, y=450)
value_moadel = Label(window, text="", bg="#0145b6")
value_moadel.place(x=203, y=500)



window.mainloop()
