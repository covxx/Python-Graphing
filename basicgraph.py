import turtle
import math
#forever hating python
tt=turtle.Pen()
tt.pensize(2)
def fun1():
    tt.up()
    tt.color("green")
    for x in range(-250, 250):
        y = x + 5
        tt.goto(x,y)
        tt.down()
def fun2():
    tt.up()
    tt.color("purple")
    for x in range(-250, 250):
        y=x**2+5
        tt.goto(x,y)
        tt.down()
def fun3():
    tt.up()
    tt.color("yellow")
    for x in range(-250, 250):
        y= x ** 3% 5
        tt.goto(x,y)
        tt.down()
def grph():
# Draw penhe grid
    pen=turtle.Pen()
    pen.speed(0)
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
#********************************************
# start of Main program
#********************************************
grph()
fun1()
fun2()
fun3()
#itbroke
