import math
from turtle import *

def dila(k):
	return 15*math.sin(k)**3
def dilb(k):
	return 12*math.cos(k)-5*\
		   math.cos(2*k)-2*\
		   math.cos(3*k)-\
		   math.cos(4*k)
speed(10000)
bgcolor("black")
for i in range(10000):
	goto(dila(i)*20, dilb(i)*20)
	for j in range(5):
		color("#f73487")
	goto(0,0)
done()