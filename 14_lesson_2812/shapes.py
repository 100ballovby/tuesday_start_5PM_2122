def draw_square(turtle, x, y, p_size=1, color='black', length=50):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.pensize(p_size)
    turtle.color(color)

    for line in range(4):
        turtle.fd(length)
        turtle.lt(90)
    return None


def draw_star(turtle, x, y, p_size=1, color='black', length=50):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.pensize(p_size)
    turtle.color(color)

    for line in range(5):
        turtle.fd(length)
        turtle.rt(144)
    return None


def x_angle(turtle, x, y, corners, p_size=1, color='black', length=50):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.pensize(p_size)
    turtle.color(color)

    if corners >= 3:
        for line in range(corners):
            turtle.fd(length)
            turtle.lt(360 / corners)
    else:
        turtle.write('Меньше 3 углов не может быть!')
    return None



