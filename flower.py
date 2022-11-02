import turtle

painter = turtle.Turtle()

def drawpetal():
  print("Starting petal")
  #starts filling
  painter.begin_fill()

  #turn the painter to face north

  #traces petal
  painter.left(30)
  painter.forward(50)
  print("about to set 90, ",painter.heading() )
  painter.rt(30)

  #makes curve
  painter.circle(-50,180)

  #turns right
  painter.right(30)
  painter.forward(50)

  #finishes petal
  print("about to set 100, ",painter.heading() )
  painter.lt(120)
  painter.forward(50)

  painter.end_fill()

#sets color blue
painter.pencolor("blue")
painter.fillcolor("blue")

# sets up the painter
painter.penup()
painter.goto(0,100)




painter.setheading(90)
painter.pendown()

#draws petal

for outside in range(6):
  drawpetal()
  painter.left(30)
  
#switches to yellow
painter.pencolor("yellow")
painter.fillcolor("yellow")

#prepares for inner yellow
painter.setheading(0)
painter.pensize(10)

#draws inner hexagon
painter.begin_fill()
for hexagon in range(6):
  painter.forward(100)
  painter.left(300)
painter.end_fill()

 
#prepares for black circle

painter.pencolor("black")
painter.fillcolor("black")
painter.penup()
painter.goto(50,-25)


#blackc circle

painter.begin_fill()
painter.circle(40) 
painter.end_fill()
painter.hideturtle()


wn = turtle.Screen()
wn.mainloop()