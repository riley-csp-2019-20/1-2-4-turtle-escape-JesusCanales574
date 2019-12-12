import turtle as trtl
import random 


joe = trtl.Turtle()
turtlesize = 2
joe.pensize(4)
player = trtl.Turtle()
player.color("blue")

player.penup()
player.turtlesize(.5)
player.shape("turtle")
player.goto(500,250)
player.pendown()

wall_width =  15
door_width =  20
distance = 20
joe.speed(0)

def drawDoor():
    joe.penup()
    joe.forward(door_width)
    joe.pendown()

def drawBarrier():
    joe.right(90)
    joe.forward(wall_width*2)
    joe.backward(wall_width*2)
    joe.left(90)


for i in range(50):
    if i > 4:
        door = random.randint (door_width, distance - door_width*2)
        barrier = random.randint (wall_width, distance - door_width*2)
    
        if door < barrier:
            joe.forward(door)
            drawDoor()
            joe.forward(barrier-door-door_width)
            drawBarrier()
            joe.forward(distance - barrier)
        else: 
            joe.forward(barrier)
            drawBarrier()
            joe.forward(door-barrier)
            drawDoor()
            joe.forward(distance-door-door_width)

    joe.left(90)
    distance += wall_width

wn = trtl.Screen()

def Up():
    player.setheading(90)
    player.forward(15)

def Down():
    player.setheading(270)
    player.forward(15)

def Left():
    player.setheading(180)
    player.forward(15)

def Right():
    player.setheading(0)
    player.forward(15)

wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right,"Right")
wn.listen()


wn.mainloop()