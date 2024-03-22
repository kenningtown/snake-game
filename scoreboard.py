import random
from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x= 0,y=260)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 13, 'normal'))


    def update(self):
        self.score +=1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=('Arial', 13, 'normal'))
