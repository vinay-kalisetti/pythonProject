# import module
import turtle
from random import randint, choice

# set up screen
width = 700
height = 500
s = turtle.Screen()
s.setup(width, height)
s.bgcolor('black')
s.title("Fireworks")

# colors
colors = ['red', 'green', 'yellow', 'gold', 'pink', 'blue', 'white', 'violet', 'orange']


class Fireworks:
    def __init__(self, radius):
        self.T = turtle.pen()
        self.T.speed(0)
        self.T.color(choice(colors))
        self.T.hideturtle()
        self.T.up()
        self.T.setposition(randint(-250, 250), randint(0, 200))
        self.T.down()
        self.radius = radius

    def update(self):
        self.T.forward(self.radius)
        self.T.backward(self.radius)
        self.T.left(10)

    def clean(self):
        self.T.clear()
        self.T.color(choice(colors))
        self.T.up()
        self.T.setposition(randint(-250, 250), randint(0, 200))
        self.T.down()

        # obj(class) Fireworks(radius)
        T1 = Fireworks(randint(10, 100))
        T2 = Fireworks(randint(10, 100))
        T3 = Fireworks(randint(10, 100))
        T4 = Fireworks(randint(10, 100))
        T5 = Fireworks(randint(10, 100))

        ##
        T = turtle.pen()
        # T.sety(-150)
        T.color('green')
        T.write('WELCOME', align='center', font=(None, 50))
        T.write('MY NAME IS VINAY', align='center', font=(None, 20))
        T.hideturtle()


turtle.mainloop()
