
'''interactive graphics program to draw a triangle,
with prompts in a text object and feedback via mouse clicks.
this program illustrates all of the most common GraphWin methods,
plus some ways to change the appearance of the graphics
'''
from graphics import *


def main():
    win_width = 300
    win_height = 300
    win = GraphWin('Draw a triangle', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)  # make right side up cordinates!
    win.setBackground('yellow')

    message = Text(Point(win_width / 2, 20), 'click on three points')
    message.draw(win)  # draw within window

    # get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    vertices = [p1, p2, p3]
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('click anywhere to quit')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)

    win.getMouse()
    win.close()


main()

