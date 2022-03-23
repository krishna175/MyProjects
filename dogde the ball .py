# -----------------------------------------------------------------------------
#
# Dodge The Ball!
# Language - Python
# Modules - pygame, sys, random, math
#
# Controls - Mouse Movement
#
#
# -----------------------------------------------------------------------------
from tkinter import messagebox
import pygame
import sys
import random
from math import *
from tkinter import *
from PIL import ImageTk,Image


def homepage():
    global home
    home = Tk()
    home.configure(bg="white")
    home.title('DODGE THE BALL 2.0')
    home.iconbitmap("Images/ball_icon.ico")
    home.resizable(False, False)

    window_width, window_height = 370, 200

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    home.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    #backgound image
    temp_size = Image.open("Images/backgound.jpg")
    temp_resized = temp_size.resize((202, 200), Image.ANTIALIAS)  #image size
    template = ImageTk.PhotoImage(temp_resized)
    template_image = Label(home, image=template, borderwidth="0")
    template_image.place(x="200", y="50")  # image position

    #button
    receipt_size = Image.open("Images/play.png")
    receipt_resized = receipt_size.resize((100,40), Image.ANTIALIAS) #button size
    receipt_image = ImageTk.PhotoImage(receipt_resized)
    Label(image=receipt_image)
    button_receipt = Button(home, image=receipt_image, borderwidth="0", activebackground='black', command=sendmailsplash)
    button_receipt.place(x=120, y=30) #button position

    quitbutton = Image.open("Images/quit.png")
    quitebtn = quitbutton.resize((100, 40), Image.ANTIALIAS)
    quiteimg = ImageTk.PhotoImage(quitebtn)
    Label(image=quiteimg)
    qutie = Button(home, image=quiteimg, borderwidth="0", activebackground='black')
    qutie.place(x=120, y=100)

    home.mainloop()


def sendmailsplash():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 200, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)

    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()

    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0")
    gif_label.place(x="65", y="6")
    animation(count)

    sending_label = Label(sendsplash, text="LOADING....", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="67", y="60")
    sendsplash.after(4000, gameLoop)

    sendsplash.mainloop()


pygame.init()

width = 400
height = 500
display = pygame.display.set_mode((width, height),pygame.NOFRAME)
pygame.display.set_caption("Dodge The Ball!")
clock = pygame.time.Clock()

background = (51, 51, 51)       #color
playerColor = (249, 231, 159)

red = (203, 67, 53)
yellow = (241, 196, 15)
blue = (46, 134, 193)
green = (34, 153, 84)
purple = (136, 78, 160)
orange = (214, 137, 16)

colors = [red, yellow, blue, green, purple, orange]

score = 0


class Ball:
    def __init__(self, radius, speed):
        self.x = 0
        self.y = 0
        self.r = radius
        self.color = 0
        self.speed = speed
        self.angle = 0

    def createBall(self):
        self.x = width / 2 - self.r
        self.y = height / 2 - self.r
        self.color = random.choice(colors)
        self.angle = random.randint(-180, 180)

    def move(self):
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))

        if self.x < self.r or self.x + self.r > width:
            self.angle = 180 - self.angle
        if self.y < self.r or self.y + self.r > height:
            self.angle *= -1

    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r * 2, self.r * 2))

    def collision(self, radius):
        pos = pygame.mouse.get_pos()

        dist = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5

        if dist <= self.r + radius:
            gameOver()


class Target:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = self.w

    def generateNewCoord(self):
        self.x = random.randint(self.w, width - self.w)
        self.y = random.randint(self.h, height - self.h)

    def draw(self):
        color = random.choice(colors)

        pygame.draw.rect(display, color, (self.x, self.y, self.w, self.h))


def gameOver():
    loop = True

    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Over!", True, (230, 230, 230))

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        display.fill(background)

        display.blit(text, (20, height / 2 - 100))
        displayScore()

        pygame.display.update()
        clock.tick()
        newgame()

def newgame():
    response = messagebox.askyesno("Game Over!!","Play again ? ")
    if response == True:
        sendmailsplash()
    elif response == False:
        pygame.quit()
        sys.exit()



def checkCollision(target, d, objTarget):
    pos = pygame.mouse.get_pos()
    dist = ((pos[0] - target[0] - objTarget.w) ** 2 + (pos[1] - target[1] - objTarget.h) ** 2) ** 0.5

    if dist <= d + objTarget.w:
        return True
    return False


def drawPlayerPointer(pos, r):
    pygame.draw.ellipse(display, playerColor, (pos[0] - r, pos[1] - r, 2 * r, 2 * r))


def close():
    pygame.quit()
    sys.exit()


def displayScore():
    font = pygame.font.SysFont("Forte", 30)
    scoreText = font.render("Score: " + str(score), True, (230, 230, 230))
    display.blit(scoreText, (10, 10))


def gameLoop():
    home.wm_state('iconic')
    sendsplash.destroy()
    global score
    score = 0

    loop = True

    pRadius = 10

    balls = []

    for i in range(1):
        newBall = Ball(pRadius + 2, 5)
        newBall.createBall()
        balls.append(newBall)

    target = Target()
    target.generateNewCoord()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        display.fill(background)

        for i in range(len(balls)):
            balls[i].move()

        for i in range(len(balls)):
            balls[i].draw()

        for i in range(len(balls)):
            balls[i].collision(pRadius)

        playerPos = pygame.mouse.get_pos()
        drawPlayerPointer((playerPos[0], playerPos[1]), pRadius)

        collide = checkCollision((target.x, target.y), pRadius, target)

        if collide:
            score += 1
            target.generateNewCoord()
        elif score == 2 and len(balls) == 1:
            newBall = Ball(pRadius + 2, 5)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 5 and len(balls) == 2:
            newBall = Ball(pRadius + 2, 6)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 10 and len(balls) == 3:
            newBall = Ball(pRadius + 2, 7)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 15 and len(balls) == 4:
            newBall = Ball(pRadius + 2, 8)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 20 and len(balls) == 5:
            newBall = Ball(pRadius + 2, 9)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()

        target.draw()
        displayScore()

        pygame.display.update()
        clock.tick(60)


homepage()
