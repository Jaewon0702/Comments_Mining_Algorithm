from tkinter import *

bad_words = ["바보", "멍청이", "똥개"]  # 나쁜 표현
check = 0

comment = input("댓글을 입력하세요: ")


def image(title, file):
    window = Tk()
    window.title(title)
    photo = PhotoImage(file=file)
    label1 = Label(window, image=photo)
    label1.pack()
    window.mainloop()


for b in bad_words:
    if b in comment:
        image("sad", "Emoticon/sad.gif")
        check = 1
        break

if check == 0:
    image("smile", "Emoticon/smile.gif")
