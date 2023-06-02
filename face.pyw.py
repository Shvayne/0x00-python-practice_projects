'''get an introduction into the world of python animations
with this simple code for a basic simliey :)
'''
from graphics import *
def main():
    win_width = 200 #window width
    win_height = 150 #height
    win = GraphWin('face', win_width, win_height) #title of window and dimensions
    win.setCoords(0, 0, win_width, win_height) #make right side up coordinates!

    head = Circle(Point(40, 100), 25) #set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill("blue")
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) #set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) #set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    message = Text(Point(win_width/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
