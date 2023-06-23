import turtle
import pandas
from tkinter import messagebox

image = "./edirnemap.gif"
screen = turtle.Screen()
screen.title("Edirne İlçe Tahmin Etme Oyunu")
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./ilceler.csv")
secilen_ilce = []
ilce_list = data["ilce"].to_list()
print(ilce_list)


ilce_turtle = turtle.Turtle()
ilce_turtle.penup()
ilce_turtle.hideturtle()

game_on = True
skor = 0
messagebox.showwarning("Dikkat!", "İlçe isimlerini türkçe karakter kullanmadan girmelisiniz!")
while game_on:

    if skor > 8:
        messagebox.showinfo("Tebrikler!", "9 ilçenin 9'ini de doğru bildiniz!")
        game_on = False
    if skor < 9:
        alinan_ilce = screen.textinput(title=f"{skor}/9 İlçe Doğru", prompt="Bir İlçe Söyleyin!").lower()

    if alinan_ilce in secilen_ilce and skor < 9:
        messagebox.showinfo("Uyarı", "Bu ilçeyi zaten tahmin etmiştiniz!")

    if alinan_ilce in ilce_list:
        ilce_list.remove(alinan_ilce)
        secilen_ilce.append(alinan_ilce)
        asil_ilce = data[data["ilce"] == alinan_ilce]
        pos_x = int(asil_ilce["x"])
        pos_y = int(asil_ilce["y"])
        print(pos_x, pos_y)
        ilce_turtle.goto(pos_x, pos_y)
        ilce_turtle.write(alinan_ilce.title())
        skor += 1

