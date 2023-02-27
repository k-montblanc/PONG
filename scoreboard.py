from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0


    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):

        self.write(f"{self.score}", False, align="left", font=("Arial", 40, "bold"))
    def add_points(self):
        self.score+= 1
        self.clear()
        self.update_score()


