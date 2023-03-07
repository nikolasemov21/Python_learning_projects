from turtle import Turtle, Screen

# object creating
tim = Turtle()
screen = Screen()

tim.speed("fastest")
tim.pensize(5)
tim.shape("turtle")


# functions for movement and clear
def move_forwards():
    tim.pendown()
    tim.forward(5)


def move_backwards():
    tim.pendown()
    tim.backward(5)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def forward_no_pen():
    tim.penup()
    tim.forward(5)


def backward_no_pen():
    tim.penup()
    tim.backward(5)


# getting the user input
screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=forward_no_pen, key="Up")
screen.onkeypress(fun=backward_no_pen, key="Down")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=clear, key="c")
screen.exitonclick()
