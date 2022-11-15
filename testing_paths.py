import turtle as trtl

painter = trtl.Turtle()

paintercolor = input("What color would you like?")

painter.color(paintercolor)
painter.left(90)
painter.circle(50,180)

wn = trtl.Screen()
wn.mainloop()