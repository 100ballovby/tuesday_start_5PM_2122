def spider(turtle, x, y, lines, length):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    for line in range(lines):
        turtle.fd(length)
        turtle.bk(length)
        turtle.rt(360 / lines)


    return None



