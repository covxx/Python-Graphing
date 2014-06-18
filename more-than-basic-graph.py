import turtle
import sys
import time
#
# =========================================
#                                         =
#    Christian Jensen L3 110216 1/31/14   =
#      Cat-o-Grapher v0.986.083c          =
#                                         =
#                                         =
#    ACII Art Is Cool!!!                  =
#                                         =
#         /\_/\                           =
#    ____/ o o \                          =
#  /~____  =ø= /                          =
# (______)__m_m)                          =
#                                         =
#       chris.com/ascii/                  =
# =========================================
#
pen=turtle.Pen()
pen.speed(0)
t=turtle.Pen()
wn=turtle.Screen()
t.ht()#hides the turtle
wn.bgcolor("#3399FF") #Sets background color
#DEF ALL THINGS
def rst():
    t.setpos(0,0,0)
def catattack(x, a=0.250, b=-10, c=0): #something cool
  return a*x**2 + b*x + c
def dostuff():
    for x in range(0,51):
        t.goto(x, catattack(x))
    t.st()   #Shows the turtle
    t.right(180)
    t.color('purple')
    t.ht()
    t.write('Done :D', align='center', font=("Trebuchet ms", 10, "bold"))
def fun2():
    t.pensize(3)
    t.color("purple")
    y=x2+5
def fun1():
    t.pensize(3)
    t.color("green")
    for x in range(-250,260):
        y=x+5
#def fun3():
#===============================================
#OK GRAPH TIME
def grph():
# Draw the grid
    pen.up()
    pen.pencolor('gray')
    for j in range (0, 510, 10):
          pen.goto(j - 250 ,- 250)
          pen.down()
          if j%50 == 0 :
             pen.pencolor('blue')
             pen.pensize(2)
          else:
             pen.pencolor('gray')
             pen.pensize(0)
          pen.goto(j-250, 250)
          pen.up()

    for j in range (0, 510, 10):
          pen.goto(- 250 , 250 -j)
          pen.down()
          if j%50 == 0 :
             pen.pencolor('blue')
             pen.pensize(2)
          else:
            pen.pensize(0)
            pen.pencolor('gray')
          pen.goto(250, 250 -j)
          pen.up()
# lable the x and y axis
    pen.color('black')
    pen.goto(0,260)
    pen.down()
    pen.write('y axis')
    pen.up()
    pen.goto(280,0)
    pen.down()
    pen.write('x axis')
    pen.ht()
# Draw the x and y orgin lines
    pen.color('black')
    pen.pensize(4)
    pen.up()
    pen.goto(-250,0)
    pen.down()
    pen.forward(500)
    pen.up()
    pen.goto(0,250)
    pen.right(90)
    pen.down()
    pen.forward(500)
    pen.up()
    return
#def mkname
def mkcat():
    print('           /\_/\   ')
    print('      ____/ o o \  ')
    print('    /~____  =ø= /  ')
    print('   (______)__m_m)  ')
def mkpretty():
    t.speed(1)
    t.color('yellow')
    t.pensize(3)
    return
#thelineshaveeyes()
#Why not just give everything cool names?
print('Welcome to the Cat-o-Grapher v0.986.083c')
print('Please Enjoy Your Stay')
grph()
#Beware if you're not a dragon born
mkpretty()
#Making stuff pretty again
rst()
fun2()
rst()
fun1()
rst()
fun3()
#dostufftwo()
print("All done or am I?")
time.sleep(5)
mkcat()
print('Bye now')
sys.exit()
