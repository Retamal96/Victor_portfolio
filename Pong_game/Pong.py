#simple pong game

import turtle

wn = turtle.Screen()
wn.title("Pong by @Victor_Retamal_")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

Score_a = 0
Score_b = 0
Increment = 0.01
#padle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

#padle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.4
Ball.dy = 0.4

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 22, "normal"))

#Moves
def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#key board binding
wn.listen()
wn.onkeypress(paddle_a_up, key='w')
wn.onkeypress(paddle_a_down, key='s')
wn.onkeypress(paddle_b_up, key='Up')
wn.onkeypress(paddle_b_down, key='Down')



## Main game loop
while True:
    wn.update()
    # ball movement
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    #Borders
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx*= -1
        Score_a += 1
        pen.clear()
        pen.write(f"Player A:{Score_a}  Player B:{Score_b}", align="center", font=("Courier", 22, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx*= -1
        Score_b += 1
        pen.clear()
        pen.write(f"Player A:{Score_a}  Player B:{Score_b}", align="center", font=("Courier", 22, "normal"))

    #collisions
    if (Ball.xcor() > 340  and  Ball.xcor() < 350) and (Ball.ycor()< paddle_b.ycor() +40 and Ball.ycor() > paddle_b.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= - 1

    if (Ball.xcor() < -340  and  Ball.xcor() > -350) and (Ball.ycor()< paddle_a.ycor() +40 and Ball.ycor() > paddle_a.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= - 1


    #Limiting the area
    if paddle_a.ycor() > 300:
        paddle_a.sety(300)
    if paddle_a.ycor() < -300:
        paddle_a.sety(-300)
    if paddle_b.ycor() > 300:
        paddle_b.sety(300)
    if paddle_b.ycor() < -300:
        paddle_b.sety(-300)

    #IA Player
    if paddle_b.ycor() < Ball.ycor() and abs(paddle_b.ycor() - Ball.ycor())  >10:
        paddle_b_up()
    if paddle_b.ycor() > Ball.ycor() and abs(paddle_b.ycor() - Ball.ycor())  >10:
        paddle_b_down()
