# simple ping ponmg game in Python 3
# Made by Justyna Replin®

import turtle  #turtle module, basic graphics, easier than pycharm from turtle import Turtle
import winsound

wn= turtle.Screen() # creating a window

wn.title("Pong")
wn.bgcolor("black")  #changing background colour
wn.setup(width=800, height= 600)
wn.tracer(0)   #stops updating our window

#functionS
def paddle_a_up():
    y= paddle_a.ycor()  #returns the y coordination
    y+= 20 # adds 20 px to y coordinate , y moves up
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # returns the y coordination
    y -= 20  # adds 20 px to y coordinate , y moves up
    paddle_a.sety(y)   # sets paddle coordination to present y coordination

def paddle_b_up():
    y = paddle_b.ycor()  # returns the y coordination
    y += 20  # adds 20 px to y coordinate , y moves up
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # returns the y coordination
    y -= 20  # adds 20 px to y coordinate , y moves up
    paddle_b.sety(y)


#Keyboard binding
wn.listen() # listens to keyboard inputs
wn.onkeypress(paddle_a_up, "w") # after binding w , function paddle_a_up is executing
wn.onkeypress(paddle_b_up, "i") # after binding w , function paddle_b_up is executing
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "k")


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()  # turtle usually draws a line to objects, we dont need that
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0) # animation speed, not the movement speed
ball.shape("square")
ball.color("white")
ball.penup()  # turtle usuallly draws a line to objects, we dont need that
ball.goto(0,0)
ball.dx =0.2  #  how many pixels ball moves (every time)
ball.dy =0.2


# score
gamerscore_1 =0
gamerscore_2 =0

#string score
pen= turtle.Turtle()
pen.speed(0)
pen.color("#FFFFFF")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1:0   Player 2:0".format(gamerscore_1,gamerscore_2), align="center",font=("Courier", 24,"normal"))



#main game loop
while True:

    wn.update()
    # ball moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor()> 290:   # below border checking
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of the ball
    elif ball.ycor()<-290:
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()> 390:   # bottom border checking
        gamerscore_1+=1
        pen.clear()
        pen.write("Player  1:{}    Player 2:{} ".format(gamerscore_1,gamerscore_2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
    elif ball.xcor()<-390:
        ball.goto(0, 0)
        gamerscore_2 += 1
        pen.clear()
        pen.write("Player 1:{}    Player 2:{}".format(gamerscore_1,gamerscore_2), align = "center", font=("Courier", 24, "normal"))

    if paddle_a.ycor() >255:
        paddle_a.sety(255)
    elif paddle_a.ycor() <-255:
        paddle_a.sety(-255)

    if paddle_b.ycor()> 255:
        paddle_b.sety(255)
    elif paddle_b.ycor()<-255:
        paddle_b.sety(-255)

    # paddle collisions
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor() -40):
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *=-1


    if (ball.xcor() <-340 and ball.xcor() > -350) and (ball.ycor()< paddle_a.ycor() +40 and ball.ycor()>paddle_a.ycor() -40):
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *=-1