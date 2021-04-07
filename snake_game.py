import turtle
#add delay by importing time
import time
import random
delay = 0.1
#score
score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title("Snake Game by Raphael Madu")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0" , align = "center" , font = ("Courier", 24 , "normal"))

#functions
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def go_right():
  if head.direction != "left":
    head.direction = "right"

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#main game loop
while True:
  wn.update()

  #check for collision with the border
  if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    #Hide segments
    for segment in segments:
      segment.goto(1000,1000)

    #clear the segments list
    segments.clear()

    #reset the delay
    delay = 0.1
    
    #reset the score
    score = 0

    pen.clear()  
    pen.write(f"Score: {score} High Score: {high_score}" , align = "center" , font = ("Courier", 24 , "normal"))


  #check for collision with food
  if head.distance(food) < 20:
    #move food to random spot on screen
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    food.goto(x,y)

    #add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    #shorten the delay
    delay  = delay - 0.001


    #increase the score
    score = score + 10

    if score > high_score:
      high_score = score

    pen.clear()  
    pen.write(f"Score: {score} High Score: {high_score}" , align = "center" , font = ("Courier", 24 , "normal"))

  #move the end segments in reverse order
  for index in range(len(segments)-1 ,0 , -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)

  #move segment zer0 to where the head is
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)


  move()

  #check for head collisions with body
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      #hide the segments
      for segment in segments:
        segment.goto(1000,1000)

      #clear the segments list
      segments.clear()

      #reset the delay
      delay  = 0.1

      #Reset the score
      score = 0
      
      #update the score display
      pen.clear()  
      pen.write(f"Score: {score} High Score: {high_score}" , align = "center" , font = ("Courier", 24 , "normal"))


  time.sleep(delay)


wn.mainloop()