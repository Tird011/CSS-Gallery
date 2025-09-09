import turtle

def draw_circle(t, x, y, radius, label, accepting=False):
    """Draw a circle at (x,y) with radius and label"""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)
    if accepting:
        t.penup()
        t.goto(x, y - radius - 5)
        t.pendown()
        t.circle(radius + 5)  # double circle for accepting state
    t.penup()
    t.goto(x, y)
    t.write(label, align="center", font=("Arial", 12, "bold"))

def draw_arrow(t, x1, y1, x2, y2, text):
    """Draw an arrow with a label"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()
    midx, midy = (x1+x2)/2, (y1+y2)/2
    t.goto(midx, midy)
    t.write(text, align="center", font=("Arial", 10, "normal"))

def draw_dfa_start0():
    screen = turtle.Screen()
    screen.title("DFA for strings starting with 0")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Draw states
    draw_circle(t, -200, 0, 40, "q0")  # start
    draw_circle(t, 0, 0, 40, "q_acc", accepting=True)
    draw_circle(t, 200, 0, 40, "q_trap")

    # Start arrow
    draw_arrow(t, -300, 0, -240, 0, "start")

    # Transitions
    draw_arrow(t, -160, 0, -40, 0, "0")
    draw_arrow(t, -160, -20, 160, -20, "1")
    draw_arrow(t, 40, 40, -40, 40, "0,1")
    draw_arrow(t, 240, 40, 160, 40, "0,1")

    screen.getcanvas().postscript(file="/mnt/data/dfa_start0_turtle.eps")
    turtle.bye()

draw_dfa_start0()

