'''Test animation of a group of objects making a face.
'''
from graphics import *
import time

def move_All(shape_list, dx, dy):
    '''move all shapes in shape_list by (dx, dy)'''
    for shape in shape_list:
        shape.move(dx, dy)

def move_all_on_line(shape_list, dx, dy, repetitions, delay):
    '''animate the shapes in shape_list along a line.
    move by the specified number of repetitions.
    have the specified delay in second after each repeat.
    '''
    for i in range(repetitions):
        move_All(shape_list, dx, dy)
        time.sleep(delay)

def main():
    win_width = 300
    win_height = 300
    win = GraphWin('back and forth', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("pink")
    rect.draw(win)

    head = Circle(Point(40, 100), 25)
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill("yellow")
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill("red")
    mouth.draw(win)

    face_list = [head, eye1, eye2, mouth] #all pieces constructed must be placed in a list for use in the moove_all_on_line functon

    cir2 = Circle(Point(150, 125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    move_all_on_line(face_list, 5, 0,46, .05)
    move_all_on_line(face_list, -5, 0,46, .05)

    Text(Point(win_width/2, 20), 'click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()

main()