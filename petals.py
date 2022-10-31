import turtle as trtl
painter = trtl.Turtle()

def drawpetal():

  #starts filling
  painter.begin_fill()

  #turn the painter to face north
  painter.setheading(90)

  #traces petal
  painter.left(30)
  painter.forward(50)
  painter.setheading(90)

  #makes curve
  painter.circle(-50,180)

  #turns right
  painter.right(30)
  painter.forward(50)

  #finishes petal
  painter.setheading(180)
  painter.forward(50)

  painter.end_fill()
  
  painter.left(30)
  
drawpetal()

wn = trtl.Screen()
wn.mainloop()