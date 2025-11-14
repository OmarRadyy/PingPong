from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_highscore = self.get_score_l()
        self.r_highscore = self.get_score_r()
        self.update()

    def get_score_r(self):
        with open("r_highscore.txt", "r") as file:
            return int(file.read())
    def get_score_l(self):
        with open("i_highscore.txt", "r") as file:
            return int(file.read())
    
    def save_score_r(self):
        with open("r_highscore.txt", "w") as file:
            file.write(str(self.r_highscore))
    def save_score_l(self):
        with open("i_highscore.txt", "w") as file:
            file.write(str(self.l_highscore))       
    
    
    def l_point(self):
        self.l_score += 1
        self.update()
    
    def r_point(self):
        self.r_score +=1
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"Score: {self.l_score}\nHigh Score: {self.l_highscore}", align='center', font=('courier', 20, 'normal'))
        self.goto(100,250)
        self.write(f"Score: {self.r_score}\nHigh Score: {self.r_highscore}", align='center', font=('courier', 20, 'normal'))
    def done(self):
        self.clear()
        self.goto(0,100)
        if self.l_score > self.l_highscore:
            self.l_highscore = self.l_score
            self.save_score_l()
        self.write(f"---------- Done ---------- \n\nFinal Score: {self.l_score} \n\n High Score: {self.l_highscore}", align='center', font=('courier', 20, 'normal'))
        self.goto(0,40)
        self.write("Max score is only 6", align='center', font=('Arial', 40, 'normal'))
        self.goto(0,-100)
        if self.r_score > self.r_highscore:
            self.r_highscore = self.r_score
            self.save_score_r()
        self.write(f"---------- Done ---------- \n\nFinal Score: {self.r_score} \n\n High Score: {self.r_highscore}", align='center', font=('courier', 20, 'normal'))
    