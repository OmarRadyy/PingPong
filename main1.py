from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('ℙ𝕚𝕟𝕘 ℙ𝕠𝕟𝕘')
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor()+ ball.y_move)
    # ده لاكتشاف اصطدام الحائط
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *=-1
    # وده لاكتشاف اصطدام المضارب
    if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <=-330 and ball.distance(l_paddle) <= 50):
        ball.x_move *= -1
        speed*=0.9*0.9
    # ده لو طلع بره المضارب يرجع للنص ويروح للاعب الاخر
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.x_move*=-1
        speed = 0.1
        score.l_point()
    #نفس النظام بس في ناحية الشمال مع المضارب 
    if ball.xcor() < -400 :
        ball.goto(0,0)
        ball.x_move*=-1
        speed = 0.1
        score.r_point()
    if score.r_score == 6 or score.l_score == 6:
        game_on = False
        score.done()        
    
   
    

      
        





screen.exitonclick()