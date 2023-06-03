'''test animation of a group of elements making a face.
combine the face elements in a function and use it twice.
have an extra level of repetiotion in the animation
'''
from graphics import *
import time

def move_all(shape_list, dx, dy):
    '''moves all shapes in shape_list by (dx, dy).'''
    for shape in shape_list:
        shape.move(dx, dy)


def move_all_on_line(shape_list, dx, dy, repetitions, delay):
    '''animate all shapes in shape_list along a line.
move by (dx, dy) each time.
repeat the specified numbeer of repetions.
have a specified delay in seconds after each repeat.
'''
    for i in range(repetitions):
        move_all(shape_list, dx, dy)
        time.sleep(delay)

def make_face(center, win): #new func!
    '''display face centered at center in window win
return a list of all shapes in the face'
'''
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1_center = center.clone() #face positions arerelative to the center
    eye1_center.move(-10, 5) #locate further points in relation to others
    eye1 = Circle(eye1_center, 5)
    eye1.setFill("blue")
    eye1.draw(win)

    eye2_end1 = eye1_center.clone()
    eye2_end1.move(15, 0)
    eye2_end2 = eye2_end1.clone()
    eye2_end2.move(10, 0)
    eye2 = Line(eye2_end1, eye2_end2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouth_corner1 = center.clone()
    mouth_corner1.move(-10, -10)
    mouth_corner2 = mouth_corner1.clone()
    mouth_corner2.move(20, -5)
    mouth = Oval(mouth_corner1, mouth_corner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]

def main():
    win_width = 300
    win_height = 300
    win = GraphWin('back and forth', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    face_list = make_face(Point(40, 100), win)
    face_list2 = make_face(Point(150, 125), win)

    steps_across = 46
    dx = 5
    dy = 3
    wait = .05

    for i in range(3):
        move_all_on_line(face_list, dx, 0, steps_across, wait)
        move_all_on_line(face_list, -dx, dy, steps_across//2, wait)
        move_all_on_line(face_list, -dx, -dy, steps_across//2, wait)

    Text(Point(win_width/2, 20), 'click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()


main()