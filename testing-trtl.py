import turtle as trtl

painter = trtl.Turtle()


painter.color("black")
painter.begin_fill()
painter.circle(80)
painter.end_fill()


wn = trtl.Screen()
wn.mainloop()