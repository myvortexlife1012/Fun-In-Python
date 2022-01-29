#mouse_move-easy


import pyautogui as mouse

def mouse_move_to__rel(x,y):
    mouse.moveRel(x, y) # ... alt is p.moveTo(50,50)

def mouse_move_to__non_rel(x,y):
    mouse.moveTo(x, y) # ... alt is p.moveRel(50,50)


#it moves it - for the whole length - by 1 px
def left(w):
    x,y = mouse.position()
    c=1
    for i in range(w):
        px = int(i)
        mouse.moveRel(x-c, y)
        c += 1
def up(h):
    x,y = mouse.position()
    c=1
    for i in range(h):
        px = int(i)
        mouse.moveRel(x, y-c)
        c += 1
def right(w):
    x,y = mouse.position()
    c=1
    for i in range(w):
        mouse.moveRel(x+c, y)
        c += 1
def down(h):
    x,y = mouse.position()
    c=1
    for i in range(h):
        mouse.moveRel(x, y+c)
        c += 1

def draw_box(w,h):
    left(w)
    up(h)
    right(w)
    down(h)


#x,y coords to start the mouse at
x=200
y=200
mouse.moveTo(x, y)
#click collection - button
w=60
h=40
draw_box(w,h)

