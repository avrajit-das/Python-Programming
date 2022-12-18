import turtle
t= turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(3)
t.color('saddlebrown')
t.left(90)
t.backward(100)
t.speed(180)
t.shape('turtle')

def gach(i):	#define tree
	if i<10:
		return
	else:
		t.forward(i)
		t.color('Gold')
		t.circle(2)
		t.color('Maroon')
		t.left(30)
		gach(3*i/4)		#tree
		t.right(60)
		gach(3*i/4)
		t.left(30)
		t.backward(i)
gach(100)	#tree
turtle.done()
