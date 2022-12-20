from turtle import Turtle

class Province(Turtle):
    def __init__(self, x, y, province):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=province, align="center", font=("Arial", 10, "normal"))

