import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#creating window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")

#width ad height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

#head of snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"

#food in the game
food = turtle.Turtle()
color = random.choice(['red', 'blue', 'yellow'])
shape = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shape)
food.color(color)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Scoree :0", align = "center", 
          font = ("candara", 24, "bold"))

#assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x= head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


segments = []

# main gameplay
while True:
    wn.update()
    if head.xcor () >290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'yellow'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {}". format(score, high_score),
                  align = "center", font = ("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)

        # adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange") #tail color
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} high Score : {}".format(score, high_score), 
                  align = "center", font = ("cendara", 24, "bold"))
    
    #checking for head collision with body segments
    for i in range(len(segments)-1,0,-1):
        x= segments[i-1].xcor()
        y= segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    for segment in segments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'yellow'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score),
                    align ="center", font= ("candara",24, "bold"))
    time.sleep(delay)

wn.mainloop()
