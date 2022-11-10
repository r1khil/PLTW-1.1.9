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


def draw_petals():

  #draws petal

  for outside in range(6):
    drawpetal()
    painter.left(30)


def yellow_hexagon():
 
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

def black_circle():
 
  #prepares for black circle

  painter.pencolor("black")
  painter.fillcolor("black")
  painter.penup()
  painter.goto(50 + starting_x,-25)


  #black circle

  painter.begin_fill()
  painter.circle(40) 
  painter.end_fill()
  painter.hideturtle()


#sets color blue
def painter_color_is_blue():
  painter.pencolor("blue")
  painter.fillcolor("blue")

# sets up the painter

def painter_set_up():
  painter.showturtle()
  painter.penup()
  painter.goto(starting_x, starting_y)
  painter.pensize(1)

  painter.setheading(90)
  painter.pendown()



#ask user for inputs


number_of_flowers = int(input("How many flowers would you like? Please provide a positive integer. "))


#sets starting variables
starting_x = 0

starting_y = 100

#execution



if number_of_flowers == 1:
  painter_color_is_blue()
  painter_set_up()
  draw_petals()
  yellow_hexagon()
  black_circle()
elif number_of_flowers == 0:
  print("No flowers drawn.")
  quit()
elif number_of_flowers < 0:
  print("Sorry, I can't print a negative amount of flowers. Positive integers only!")
  quit()
elif number_of_flowers >= 1:
  for total_flowers in range(number_of_flowers):
    painter_color_is_blue()
    painter_set_up()
    draw_petals()
    yellow_hexagon()
    black_circle()
    painter_color_is_blue()
    starting_x = starting_x + 500
    painter_set_up
    




wn = turtle.Screen()
wn.mainloop()