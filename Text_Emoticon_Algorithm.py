from tkinter import *

bad_words = ["김치녀", "된장녀", "한녀", "한남", "김치남", "맘충", "메갈", "워마드","쌍도남",
             "틀딱충", "1호선 냄새", "반송장",
             "전라디언", "홍어", "통구이",
             "짱꼴라", "짱깨", "착짱죽짱", "튀기", "파키벌레",]  # 혐오 표현
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
