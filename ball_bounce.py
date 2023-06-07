from graphics import *
import time, random

def bounce_in_box(shape, dx, dy, xlow, xhigh, ylow, yhigh):
    '''animate a shape moving in jumps(dx, dy), bouncing when its center
reaches the low and high x and y coordinates)
'''
    delay = .005
    for i in range(600):
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        if x < xlow:
            dx = -dx
        elif x > xhigh:
            dx = -dx

        if y < ylow:
            dy = -dy
        elif y > yhigh:
            dy = -dy
        time.sleep(delay)

def get_random_point(xlow, xhigh, ylow, yhigh):
    '''return a random point with coordinates in the range specified.'''
    x = random.randrange(xlow, xhigh + 1)
    y = random.randrange(ylow, yhigh + 1)
    return Point(x, y)
def make_disk(center, radius, win):
    '''return a red disk that is drawn in win with given center and radius'''
    disk = Circle(center, radius)
    disk.setOutline("red")
    disk.setFill("red4")
    disk.draw(win)
    return disk

def bounce_ball(dx, dy):
    '''make a ball bounce around the screen, initially moving by (dx, dy) at each jump'''
    win_width = 290
    win_height = 290

    win = GraphWin('ball bounce', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)

    radius = 10
    xlow = radius #center is seperated from the wall by the radius at a bounce
    xhigh = win_width - radius
    ylow = radius
    yhigh = win_height - radius

    center = get_random_point(xlow, xhigh, ylow, yhigh)
    ball = make_disk(center, radius, win)

    bounce_in_box(ball, dx, dy, xlow, xhigh, ylow, yhigh)
    win.close()

bounce_ball(3, 5)