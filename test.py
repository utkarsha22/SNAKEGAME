import turtle
import time
import random
delay = 0.1
#set up the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screen updayes


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0,100)

segments = []




#Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"


def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)

    
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)

    
    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)

    
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x +20)

#ketboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#main game loop
while True:
    wn.update()


#check for a collision with the food
    if head.distance(food) < 20:
        #move the food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    


    move()

    time.sleep(delay)

wn.mainloop()