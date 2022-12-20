import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Turkey States Game")
image = "unnamed.gif"
screen.addshape(image)
turtle.shape(image)

def mouse_click_coords(x, y):
    print(x, y)

# onscreenclick is an event listener
turtle.onscreenclick(mouse_click_coords)
# wkwk
turtle.mainloop()
