# board.py
# written by Quinn Huggins
import turtle


screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Tic-Tac-Toe.py")
screen.setworldcoordinates(-6, -6, 6, 6)
screen.tracer(0, 0)

grid = turtle.Turtle()
grid.hideturtle()
grid.speed(0)


def draw_outline():
    grid.pensize(10)
    grid.penup()
    grid.goto(5, 5)
    grid.pendown()
    grid.right(90)
    grid.forward(10)
    grid.right(90)
    grid.forward(10)
    grid.right(90)
    grid.forward(10)
    grid.right(90)
    grid.forward(10)
    draw_board()


def draw_board():
    grid.pencolor("black")
    grid.pensize(10)

    grid.up()
    grid.goto(-5, -2)
    grid.seth(0)
    grid.down()
    grid.fd(10)

    grid.up()
    grid.goto(-5, 2)
    grid.seth(0)
    grid.down()
    grid.fd(10)

    grid.up()
    grid.goto(-2, -5)
    grid.seth(90)
    grid.down()
    grid.fd(10)

    grid.up()
    grid.goto(2, -5)
    grid.seth(90)
    grid.down()
    grid.fd(10)
    grid.up()
