# Simple Pong in python 3 for beginers.
import turtle
import winsound


n = turtle.Screen()
n.title("Pong")
n.bgcolor("black")
n.setup(width=800,height=600)
n.tracer(0)

#score
score_a = 0 
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)


#Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("white")
ball1.penup()
ball1.goto(0,0)
ball1.dx = 1
ball1.dy = -1

balls=[ball1]

#Pen 
pen=turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup() 
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0 ",align="center",font=("courier",24,"normal"))

# Function 

def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)  

# ai player function
def ai_paddle():
        
        closest_ball = balls[0] 
        for ball in balls:
            if ball.xcor() > closest_ball.xcor():
                closest_ball = ball
        
        if paddle_b.ycor() < closest_ball.ycor() - 20:
            paddle_b.sety(paddle_b.ycor() + 3)  # moves slower than ball
        elif paddle_b.ycor() > closest_ball.ycor() + 20:
            paddle_b.sety(paddle_b.ycor() - 3)
            
# reset game 
def end_game(winner):
    global score_a, score_b, game_over
    pen.goto(0, 0)
    pen.clear()
    
    # hide everything before showing winner text
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    ball1.hideturtle()

    pen.write(f"{winner} Wins!", align="center", font=("courier", 36, "normal"))
    n.update()
    
    choice = n.textinput("Game Over", "Play again? (y/n): ")
    
    if choice and choice.strip().lower() == "y":
        # reset scores
        score_a = 0
        score_b = 0
        # reset ball
        ball1.goto(0, 0)
        ball1.dx = 0.5
        ball1.dy = -0.5
        # reset paddles
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        # reset scoreboard
        pen.goto(0, 260)
        pen.clear()
        pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))
        n.listen()
    else:
        pen.goto(0, -50)
        pen.write("Thanks for playing!", align="center", font=("courier", 24, "normal"))
        n.update()
        game_over = True

# Keyboard binding                   
n.listen() 
n.onkeypress(paddle_a_up,"w")
n.onkeypress(paddle_a_down,"s")
n.onkeypress(paddle_b_up,"Up")
n.onkeypress(paddle_b_down,"Down")               
        
# AI choice
choice = n.textinput("Game Mode", "Play against AI? (y/n): ")
ai_enabled = choice.strip().lower() == "y" if choice else False
n.listen()

#game_over
game_over = False

#Main game loop
while True:
    n.update()
    if game_over:
        break

    if ai_enabled:
        ai_paddle()
   

    for ball in balls:
        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    
        #Border checking 
        if ball.ycor() > 290 :
            ball.sety(290)
            ball.dy *= -1
            winsound.Beep(450,40) 

        if ball.ycor() < -290 :
            ball.sety(-290)
            ball.dy *= -1
            winsound.Beep(450,40)  

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {} ". format(score_a,score_b),align="center",font=("courier",24,"normal"))
            winsound.Beep(300,150)
            
        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1 
            score_b += 1 
            pen.clear() 
            pen.write("Player A: {}  Player B: {} ". format(score_a,score_b),align="center",font=("courier",24,"normal")) 
            winsound.Beep(300,150)
           
        # limit of scores
        if score_a == 10:
            pen.clear()
            end_game("Player A wins ")

        if score_b == 10:
            pen.clear()
            end_game("Player B wins ")
                
        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40) :
            ball.setx(340)
            ball.dx *= -1
            winsound.Beep(459,32)

        if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40) :
            ball.setx(-340)
            ball.dx *= -1 
            winsound.Beep(459,32)

   

      
       
