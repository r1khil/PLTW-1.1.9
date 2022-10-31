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

painter.penup()
painter.goto(0,100)

painter.setheading(90)
painter.pendown()
for outside in range(6):
  drawpetal()
  painter.left(30)
    
wn = turtle.Screen()
wn.mainloop()