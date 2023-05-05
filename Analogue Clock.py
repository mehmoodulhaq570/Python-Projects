# Importing the modules
import turtle
import time

# Creating the screen
wndw = turtle.Screen()
wndw.bgcolor("green")
wndw.setup(width=600, height=600)
wndw.title("Analogue Clock")
wndw.tracer(0)

# Create the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

#Functions
def draw_clock(h,m,s,pen):
    # Draw clock face
    pen.penup()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw clock marketings for minutes and seconds
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(60):
     pen.fd(200)   
     pen.pendown()
     pen.fd(10)
     pen.penup() 
     pen.goto(0,0)
     pen.rt(6)
     
    # Draw numbers on clock face
    # One
    pen.penup()   
    pen.goto(0,0)
    pen.setheading(60)
    pen.fd(145) 
    pen.setheading(0)
    pen.fd(15) 
    pen.write(1,move = False, align="center",font=("Arial",25,"normal"))

    # Two
    pen.penup()
    pen.goto(0,0)
    pen.setheading(30)
    pen.fd(135) 
    pen.setheading(0)
    pen.fd(35) 
    pen.write(2,move = False, align="center",font=("Arial",25,"normal"))

    # Three
    pen.penup()
    pen.goto(0,0)
    pen.setheading(352)
    pen.fd(150) 
    pen.setheading(0)
    pen.fd(25) 
    pen.write(3,move = False, align="center",font=("Arial",25,"normal"))

    # Four
    pen.penup()
    pen.goto(0,0)
    pen.setheading(315)
    pen.fd(150) 
    pen.setheading(0)
    pen.fd(45) 
    pen.write(4,move = False, align="center",font=("Arial",25,"normal")) 

    # Five
    pen.penup()
    pen.goto(0,0)
    pen.setheading(290)
    pen.fd(178) 
    pen.setheading(0)
    pen.fd(25) 
    pen.write(5,move = False, align="center",font=("Arial",25,"normal"))

    # Six
    pen.penup()
    pen.goto(0,0) 
    pen.setheading(270)
    pen.fd(190) 
    pen.write(6,move = False, align="center",font=("Arial",25,"normal"))

    # Seven
    pen.penup()
    pen.goto(0,0)
    pen.setheading(258)
    pen.fd(170) 
    pen.setheading(180)
    pen.fd(48) 
    pen.write(7,move = False, align="center",font=("Arial",25,"normal"))

    # Eight
    pen.penup()
    pen.goto(0,0)
    pen.setheading(228)
    pen.fd(150) 
    pen.setheading(180)
    pen.fd(50) 
    pen.write(8,move = False, align="center",font=("Arial",25,"normal"))
    # Nine
    pen.penup()
    pen.goto(0,0)
    pen.setheading(188)
    pen.fd(150) 
    pen.setheading(180)
    pen.fd(25) 
    pen.write(9,move = False, align="center",font=("Arial",25,"normal"))
    # Ten
    pen.penup()
    pen.goto(0,0)
    pen.setheading(150)
    pen.fd(135) 
    pen.setheading(180)
    pen.fd(25) 
    pen.write(10,move = False, align="center",font=("Arial",25,"normal"))
    # Eleven
    pen.penup()
    pen.goto(0,0)
    pen.setheading(120)
    pen.fd(145) 
    pen.setheading(180)
    pen.fd(15) 
    pen.write(11,move = False, align="center",font=("Arial",25,"normal")) 
    # Twelve
    pen.penup()
    pen.goto(0,0) 
    pen.setheading(90)
    pen.fd(150) 
    pen.write(12,move = False, align="center",font=("Arial",25,"normal"))

    # Draw clock face
    pen.penup()
    pen.goto(0,0)
    pen.pencolor("Yellow")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

    # Draw clock face
    pen.penup()
    pen.goto(0,0)
    pen.pencolor("blue")
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw clock face
    pen.penup()
    pen.goto(0,0)
    pen.pencolor("red")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # Draw clock face
    pen.penup()
    pen.goto(0,0)
    pen.pencolor("gold")
    pen.setheading(268)
    pen.fd(125)
    pen.setheading(0)
    pen.fd(5)
    pen.write("Analogue Clock",move=False,align="center",font=("Arial",12,"normal"))

    # Draw clock face
    pen.penup()
    pen.goto(0,0)
    pen.pencolor("gold")
    pen.setheading(88)
    pen.fd(90)
    pen.write("Dream Sky",move=False,align="center",font=("Arial",15,"normal"))           
      
#Main loop
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h,m,s,pen)

wndw.mainloop()
