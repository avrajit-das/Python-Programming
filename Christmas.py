from turtle import *
import random

n = 170
speed("fastest")
left(90)
forward(3*n)

card=Screen()
card.setup(1.0,1.0,0,0)
card.title("Christmas Celebration! by Avrajit Das")
colors=['#92b6f0', '#d95d78', '#5cdbb5', '5ccde0', '#e0d758', '#ed9277']
card.bgcolor(random.choice(colors))

color("dark green")
backward(n*4.8)
tracer(8,50)

def drawTupi():
	pen.color('red')
	pen.fillcolor('red')
	pen.begin_fill()
	for i in range(3):
		pen.fd(50)
		pen.right(120)
	pen.end_fill()
	for i in range(6):
		pen.dot(10,'white')
		pen.fd(10)
	pen.right(130)
	pen.fd(55)
	pen.dot(10,'white')

def gach(a, b):
	if a<= 0:
		return
	forward(b)
	gach(a-1, b*.8)
	right(120)
	gach(a-3, b*.5)
	right(120)
	backward(b)

def makeBorof():
	for i in range(50):
		borof=Turtle()
		borof.pu()
		borof.color("white")
		borof.shape("circle")
		borof.speed(0)
		borof.goto(random.randint(-700, 700), random.randint(-700, 700))
		borof.dot(7, 'white')
		boroflist.append(borof)

def borofbristi():
	for i in boroflist:
		i.goto(random.randint(-700, 700), random.randint(-700, 700))
		i.dot(7, 'white')

boroflist=[]
makeBorof()
gach(15, n)
card.tracer(False)
card.tracer(True)

pen=Turtle()
pen.hideturtle()
pen.color("black")
pen.pu()
pen.setx(-500)
pen.color('Yellow')
pen.write("Merry\nChristmas!!!!", font=("phosphate",40, "italic"),align="left")
pen.setheading(-90)
pen.fd(100)
pen.write("To All of You", font=("phosphate",30,"bold"),align="left")

pen.setheading(0)
pen.fd(360)
pen.left(145)
pen.fd(40)
drawTupi()

while True:
	borofbristi()
	card.bgcolor(random.choice(colors))
backward(n/2)
tatabyebye()