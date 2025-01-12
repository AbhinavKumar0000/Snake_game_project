from turtle import Turtle, Screen


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        txt1 = open("data.txt", "r")
        self.high_score = int(txt1.read())
        txt1.close()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align= "center", font =("Arial",18,"normal"))

    def reset(self):
        if self.score > self.high_score:

            self.high_score = self.score
        self.score = 0
        txt = open("data.txt", "w")
        txt.write(f"{self.high_score}")
        txt.close()
        self.update_scoreboard()



    def increase(self):
        self.score +=1
        self.update_scoreboard()

