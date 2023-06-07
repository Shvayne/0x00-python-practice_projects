'''make a chioce of color via mouse clicks in rectangles'''
from graphics import *
def is_between(x, end1, end2):
    '''return true if x is between the ends or equal to either.
        the ends do not need to be in increasing order.'''
    return end1 <= x <= end2 or end2 <= x <= end1
def is_inside(point, rect):
    '''return true if the point is inside the rectangle rect.'''
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return is_between(point.getX(), pt1.getX(), pt2.getX()) and is_between(point.getY(), pt1.getY(), pt2.getY())

def make_colored_rect(corner, width, height, color, win):
    '''return a rectangle drawn in win with the upper left corner and color specified.'''
    corner2 = corner.clone()
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def main():
    win_width = 400
    win_height = 400
    win = GraphWin('pick colors', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    red_button = make_colored_rect(Point(310, 350), 80, 30, 'red', win)
    yellow_button = make_colored_rect(Point(310, 310), 80, 30, 'yellow', win)
    blue_button = make_colored_rect(Point(310, 270), 80, 30, 'blue', win)

    house = make_colored_rect(Point(60, 200), 180, 150, 'gray', win)
    door = make_colored_rect(Point(90, 150), 40, 100, 'white', win)
    roof = Polygon(Point(50, 200), Point(250, 200), Point(150, 300))
    roof.setFill('black')
    roof.draw(win)

    msg = Text(Point(win_width/2, 375), 'click to choose a house color.')
    msg.draw(win)
    pt = win.getMouse()
    if is_inside(pt, yellow_button):
        color = 'yellow'
    elif is_inside(pt, red_button):
        color = 'red'
    elif is_inside(pt, blue_button):
        color = 'blue'
    else:
        color = 'white'
    house.setFill(color)

    msg.setText('click to choose a door color')
    pt = win.getMouse()
    if is_inside(pt, red_button):
        color = 'red'
    elif is_inside(pt, yellow_button):
        color = 'yellow'
    elif is_inside(pt, blue_button):
        color = 'blue'
    else:
        color = 'white'
    door.setFill(color)

    msg.setText('click anywhere to quit.')
    win.getMouse()
    win.close()

main()

