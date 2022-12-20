# ÖZNUR ÖZNUR 190209803 PYTHON PROGRAMMING MIDTERM PROJECT
import turtle
import pandas as pd
from province import Province
import ctypes

screen = turtle.Screen()
screen.setup(1200, 750)
screen.title("Turkey State Game")
image = "unnamed.gif"
screen.addshape(image)
turtle.shape(image)

provinces_data = pd.read_csv("81_province.csv")
provinces = provinces_data["province"].tolist()

guessed_province = []
missing_province = []

count = 0
# asking provinces
while count < 82:
    if count == 0:
        answer = screen.textinput(title="Guess The Province", prompt="Please enter a province name :)").title()
    else:
        answer = screen.textinput(title=f"{count}/81 Province Correct", prompt="Keep going! :)").title()

    # exiting the loop
    if answer == "Exit":
        break

    # checking the provinces and placing it on a map
    if answer in provinces:
        guessed_province.append(answer)  # appendending answer to the guessed_province list.
        coordinate = provinces_data[provinces_data.province == answer]
        x_cord = int(coordinate["x"])
        y_cord = int(coordinate["y"])
        province_ = Province(x_cord, y_cord, answer)
        count += 1

    elif answer in guessed_province:
        def mbox(title, text, style):   # I  know this part doesnt work,I tried so many solutions but none of work.I really would like to teach me this part when you are free.Thank you teacher.
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        mbox('Hey! This is a warning', 'This city has already entered', 1)
        count -= 0
    else:
        def mbox(title, text, style):
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        mbox('Hey! This is a warning', 'There is no such a province in Turkey', 1)
        count -= 0


for province in provinces:
    if province not in guessed_province:
        missing_province.append(provinces)
df = pd.DataFrame(missing_province)
df.to_csv("Missing_province.csv")

