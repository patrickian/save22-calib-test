import turtle
def kurba(x):
	for x in range(x):
		turtle.forward(1)
		turtle.right(1)

def kurba2(x):
	for x in range(x):
		turtle.forward(.09)
		turtle.right(.5)


def kurba3(x):
	for x in range(x):
		turtle.forward(.25)
		turtle.right(1)

def squirtle():
	#-------outline-------
	turtle.color('red')
	turtle.left(90)
	turtle.forward(225)
	turtle.right(90)
	turtle.forward(50)
	kurba(160)
	#turtle.forward(25)
	#turtle.backward(30)
	turtle.right(200)
	turtle.forward(10)
	kurba(180)
	turtle.forward(83)
	turtle.penup()
	turtle.right(90)
	turtle.forward(175)
	turtle.right(90)
	turtle.forward(35)
	turtle

	turtle.pendown()
	turtle.forward(15)
	kurba2(360)
	turtle.forward(15)
	turtle.right(90)
	turtle.forward(20)
	
	turtle.penup()
	turtle.right(180)
	turtle.forward(100)

	turtle.pendown()
	turtle.left(90)
	turtle.forward(30)
	kurba3(180)
	turtle.forward(30)
	turtle.right(90)
	turtle.forward(30)
	turtle.exitonclick()

def main():
	squirtle()
if __name__ == '__main__':
 	main()
