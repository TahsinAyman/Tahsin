import turtle

p1 = turtle.Turtle()
p1.speed(10)
turtle.title('Tahsin')

p1.color('green')

p1.begin_fill()
p1.right(90)
p1.forward(50)
p1.right(90)
p1.forward(200)
p1.right(90)
p1.forward(200)
p1.right(90)
p1.forward(400)
p1.right(90)
p1.forward(200)
p1.right(90)
p1.forward(200)
p1.end_fill()

p1.color('green', 'red')
p1.right(180)
p1.forward(50)
p1.left(90)
p1.forward(100)

p1.begin_fill()
p1.circle(50)
p1.end_fill()

p1.color('green')
p1.forward(100)
p1.color('white', 'white')
p1.forward(50)
p1.left(90)
p1.forward(50)
p1.color('black')
p1.pensize(2)
p1.write('Thank You')

turtle.done()

