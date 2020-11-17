from tkinter import *

bad_words = ["바보", "멍청이", "똥개"]  # 나쁜 표현
good_words = ["사랑", "행복", "웃음"]  # 좋은 표현

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
        break


for g in good_words:
    if g in comment:
        image("smile", "Emoticon/smile.gif")
        break
