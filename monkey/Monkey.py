from random import choice
from time import sleep
from tkinter import N, S, Canvas, PhotoImage, Tk, mainloop


WIDTH, HEIGHT, GAP = 600, 350, 50
PLACES = [(GAP, HEIGHT), (WIDTH - GAP, HEIGHT)]


def control(event):
    global banana_mod
    key = event.keysym
    global monkey_speed
    if key == "d":
        monkey_speed = 20
    if key == "a":
        monkey_speed = -20
    if key == "space":
        banana_mod = "fly"    
    print(event)

def stop(event):
    key = event.keysym
    global monkey_speed
    if key == "d" or key == "a":
        monkey_speed = 0 

def place_banana():
    dx, dy = choice(PLACES)
    canvas.coords(banana, dx , dy)

def monkey_touch():
    bx,by = canvas.coords(banana)
    mx,my = canvas.coords(monkey)
    return abs(bx - mx) < GAP 

def banana_move():
    global banana_mod
    if banana_mod == "lay":
        if monkey_touch(): 
            banana_mod = "bring"
            return
    if banana_mod == "bring":
        mx, my = canvas.coords(monkey)
        canvas.coords(banana, mx, my)
        return
    if banana_mod == "fly":
        canvas.move(banana, 0 , -10)
        bx,by = canvas.coords(banana)
        if by < 0:
            place_banana()
            banana_mod ="lay"

def parrot_touch():
    bx, by = canvas.coords(banana)
    px, py = canvas.coords(parrot)
    return abs(bx - px) < GAP and abs(by - py) < GAP

def parrot_move():
    global parrot_speed, parrot_mode
    if parrot_touch():
        parrot_mode = "hit"
    if parrot_mode == "fly":
        canvas.move(parrot, parrot_speed,0)
    px, py = canvas.coords(parrot)
    if px < 0 or px > WIDTH:
        parrot_speed *= -1
    else:
        canvas.move(parrot, 0, abs(parrot_speed))
        px, py = canvas.coords(parrot)
        if py > HEIGHT:
            parrot_mode = "fly"
            canvas.coords(parrot, GAP, 0)


root = Tk()
canvas: Canvas = Canvas( root, width = WIDTH, height = HEIGHT )
canvas.pack()

monkey_img = PhotoImage(file = "monkey.png")
jungle_img = PhotoImage(file = "jungle.png")
banana_img = PhotoImage(file = "banana.png")
parrot_img = PhotoImage(file = "parrot.gif")


canvas.create_image(WIDTH / 2, HEIGHT  / 2, image = jungle_img)
monkey = canvas.create_image(WIDTH / 2, HEIGHT, anchor = S, image = monkey_img)
banana = canvas.create_image(GAP,WIDTH / 2, anchor = S, image = banana_img)
parrot = canvas.create_image(GAP,0, anchor = N, image = parrot_img)

place_banana()


banana_mod = "lay"
parrot_mode = "fly"
monkey_speed = 0
parrot_speed = 10 

canvas.bind_all ("<KeyPress>", control)
canvas.bind_all ("<KeyRelease>", stop)


run = True
while run:

    canvas.move(monkey, monkey_speed,0 )
    banana_move()
    parrot_move()
    canvas.update()
    sleep(0.01)
 
mainloop()