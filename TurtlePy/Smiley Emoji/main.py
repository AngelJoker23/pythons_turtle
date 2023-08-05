import turtle
smiley = turtle.Turtle()

#Eyes
def eye(col, rod):
    smiley.down()
    smiley.fillcolor(col)
    smiley.begin_fill()
    smiley.end_fill()
    smiley.up()

    #Face
def face():
    smiley.goto(-40, 120)
    eye('white', 15)
    smiley.goto(-37, 130)
    eye('black', 5)
    smiley.goto(40, 120)
    eye('white', 15)
    smiley.goto(37, 130)
    eye('black', 5)

    #Mouth
def mouth():
    smiley.goto(-40, 85)
    smiley.down()
    smiley.right(90)
    smiley.circle(40, 180)
    smiley.up()

    #Tongue
def tongue():
    smiley.goto(-10, 45)
    smiley.down()
    smiley.right(180)
    smiley.fillcolor('red')
    smiley.begin_fill()
    smiley.circle(10, 180)
    smiley.end_fill()
    smiley.hideturtle()

turtle.done()