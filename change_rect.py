from graphics import *


def main():
    win_height = 300
    win_width = 280
    win = GraphWin('changing image', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    circle = Circle(Point(40, 100), 25)
    circle.setFill('blue')
    circle.setOutline('pink')
    circle.draw(win)

    message = Text(Point(win_width / 2, 15), 'click to change image')
    message.draw(win)

    message.setText('click to draw a rectangle')
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(15)

    win.getMouse()
    rectangle = Rectangle(Point(200, 90), Point(220, 100))
    rectangle.setFill('pink')
    rectangle.setOutline('blue')
    rectangle.draw(win)

    message.setText('click anywhere to quit')
    win.getMouse()
    win.close()


main()