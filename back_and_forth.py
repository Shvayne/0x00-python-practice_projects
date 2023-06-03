'''test animation and depth.
'''
from graphics import *
import time


def Move_on_line(shape, dx, dy, repetitions, delay):
    # moves the given shape, a certain number of repetitions, in dy and dx positions, and a number of delay
    for i in range(repetitions):
        # while(1):
        shape.move(dx, dy)
        time.sleep(delay)


def main():
    win_width = 300
    win_height = 300
    win = GraphWin('back and forth', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    rect = Rectangle(Point(200, 90), Point(220, 100))  # object1
    rect.setFill("blue")
    rect.draw(win)

    cir1 = Circle(Point(40, 100), 25)  # object2
    cir1.setFill("red")
    cir1.draw(win)

    cir2 = Circle(Point(150, 125), 25)  # object3
    cir2.setFill("red")
    cir2.draw(win)

    Move_on_line(cir1, 5, 0, 46, .05)
    Move_on_line(cir1, -5, 0, 46, .05)

    # wait for a final click to exit
    Text(Point(win_width / 2, 20), 'click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()


main()
