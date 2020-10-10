from math import sqrt, pi
import pygame
import sys
import tkinter as tk
from tkinter import messagebox


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def valid_point(p):
    d = p.dist(origin)
    if d <= radius:
        return True
    return False


class Details:

    def ask(self, msg):
        self.root = tk.Tk()
        self.root.geometry('220x120')
        label = tk.Label(self.root, text=f'{msg}', font=('Calibri', 12))
        label.grid(row=3, column=0, pady=2)
        entry = tk.Entry(self.root)
        entry.grid(row=4, column=0, pady=2)
        button = tk.Button(self.root, height=1, width=10, text="Enter", command=lambda: self._ask(entry.get().upper()))
        button.grid(row=5, column=0, pady=2)
        self.root.mainloop()
        return int(self._var/5)

    def _ask(self, value):
        try:
            value = int(value)
            self._var = value
            self.root.destroy()
        except:
            self.message('Invalid name','Entry is not valid.\nRadius must be an integer')
        self.root.mainloop()

    @staticmethod
    def message(subject, content):
        win = tk.Tk()
        win.attributes('-topmost', True)
        win.withdraw()
        messagebox.showinfo(subject, content)
        try:
            win.destroy()
        except:
            pass


try:
    det = Details()
    radius = det.ask('Enter the Radius of circle in mm')
    l = det.ask('Enter the length of box in mm')-1
    w = det.ask('Enter the width of box in mm')-1
    if l > w:
        pass
    else:
        pass
        l, w = w, l
    circle_area = pi*(radius**2)
    shape_area = l*w
    total_shapes = int(circle_area/shape_area)
    lower_limit = int((sqrt(2) * radius) / l) ** 2
except:
    sys.exit()

width = int(radius*2.3)
height = int(radius*2.3)
origin = Point(int(width/2), int(height/2))
pygame.init()
screen = pygame.display.set_mode((width+200, height))
font = pygame.font.SysFont('monospace', 35)
label_font = pygame.font.SysFont('monospace', 22)
pygame.draw.circle(screen, (155, 0, 0), (origin.x, origin.y), radius)
num = int((sqrt(2) * radius) / l)

if total_shapes>10:
    ip = Point(origin.x - radius+2, origin.y - radius+2)
else:
    ip = Point(int(origin.x - l * num / 2), int(origin.y - l * num / 2))
    while valid_point(ip):
        ip = Point(ip.x, ip.y-1)
    ip = Point(ip.x, ip.y+1)
x = ip.x
y = ip.y
c = 0
d = 0
disx = 2

count=0
while d<total_shapes:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    c += 1
    d += 1
    ptl = Point(int(x + (c-1) * (l + 1)), int(y))
    ptr = Point(int(x + c * (l+1)), int(y))
    pbl = Point(int(x + (c-1) * (l + 1)), int(y+w))
    pbr = Point(int(x + c * (l+1)), int(y+w))
    disx += l
    if valid_point(ptl) == valid_point(ptr) == valid_point(pbl) == valid_point(pbr) == True:
        count += 1
        pygame.draw.rect(screen, (200, 200, 200), (int(x + (c-1)*(l + 1)), int(y), int(l), int(w)))
    else:
        if disx > radius:
            disx = 2
            c = 0
            y += (w+1)
    pygame.display.update()

if count != 0:
    label = label_font.render(f'Total boxes: {count}', 1, (255, 0, 0))
    screen.blit(label, (int(width - radius / 2), 10))
else:
    det.message('Box too big !', 'Box can\'t fit in this circle')

pygame.display.update()
pygame.image.save(screen, "Image.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
