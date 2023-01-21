import turtle as flr
import colorsys as ad

flr.setup(700,700)
flr.speed(-400)
flr.width(3)
flr.bgcolor("black")

for j in range(25):
	for i in range(15):
		flr.color(ad.hsv_to_rgb(i/15, j/25, 1))
		flr.right(90)
		flr.circle(200-j*4, 90)
		flr.left(90)
		flr.circle(200-j*4, 90)
		flr.right(180)
		flr.circle(50, 24)
flr.hideturtle()
flr.done()