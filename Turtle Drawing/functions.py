import turtle
import random


# functions
def draw_square(turtle_draw, size):
    # this function draws square in the argument you can put how big the side you want to be
    for _ in range(4):
        turtle_draw.forward(size)
        turtle_draw.right(90)


def draw_dashed_line(turtle_draw, lines_count, space, line_size):
    # this function draws dashed line, you can select how many dashes to have as well as the space
    # in between and the size of the lines.
    for _ in range(lines_count):
        turtle_draw.forward(line_size)
        turtle_draw.penup()
        turtle_draw.forward(space)
        turtle_draw.pendown()


def random_color(turtle_draw):
    # this function pick random color from list to change the turtle's pen color
    colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
               "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
    turtle_draw.color(random.choice(colours))


def draw_overlay_shapes(turtle_draw, side_size):
    # This function draws figures with 3,4,5,6,7,8,9,10 angles overlayed one over the other in random
    # different colours.

    for i in range(3, 10):
        a = i
        random_color(turtle)
        while a > 0:
            turtle_draw.forward(side_size)
            turtle_draw.right(360 / i)
            a -= 1


def random_walk(turtle_draw):
    # This function makes the turtle draw in randomly chosen direction. The while loop has no end purposely,
    # so the random walk is infinite.
    turtle_draw.pensize(10)
    turtle_draw.speed(10)
    while True:
        random_color(turtle_draw)
        turtle_draw.forward(40)
        turning = random.randint(1, 4)
        if turning == 1:
            turtle_draw.seth(0)
        elif turning == 2:
            turtle_draw.seth(90)
        elif turning == 3:
            turtle_draw.seth(180)
        else:
            turtle_draw.seth(270)


def spirograph(turtle_draw, size_of_gap):
    # This function draws spirograph with random color for each circle (using the rando_color() function from above)
    turtle_draw.pensize(2)
    turtle_draw.speed("fastest")

    for i in range(int(360/size_of_gap)):
        random_color(turtle_draw)
        turtle_draw.circle(100)
        turtle_draw.left(size_of_gap)
        turtle_draw.hideturtle()


