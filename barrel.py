import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_barrel(x, y, radius, height, color):
    glBegin(GL_POLYGON)
    glColor3f(*color)
    glVertex2f(x-(radius/3), y)
    glVertex2f(x, y + height)
    glVertex2f(x + radius-(radius/3), y + height)
    glVertex2f(x + radius, y)
    glEnd()

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(-5, 5, -5, 5)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # draw_wheel(0, 0, 2, 12, 0.27, 0.13, 0.07)  # Example: wheel with radius 2 and 12 spokes
    draw_barrel(0, 0, 1, 4, (0.4, 0.4, 0.4))  # Example: barrel with radius 1 and height 2

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()

sys.modules['draw_barrel'] = draw_barrel