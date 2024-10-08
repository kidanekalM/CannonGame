import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
def draw_circle(x, y, radius, color):
    num_segments = 30
    theta = 2 * math.pi / num_segments
    c = math.cos(theta)
    s = math.sin(theta)
    t = 1 - c
    x0 = radius
    y0 = 0
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        x1 = x0
        y1 = y0
        x0 = x0 * c - y0 * s
        y0 = x1 * s + y0 * c
        glVertex2f(x + x0, y + y0)
    glEnd()
def draw_wheel(x,y,radius, spokes,r,g,b):
    draw_circle(x, y,radius,(r,g,b) )
    draw_circle(x, y,(radius*0.4/0.6),(.9,.9,.91) )
    draw_circle(x, y,(radius*0.1/0.6),(r,g,b) )
    glLineWidth(radius*2)
    for i in range(spokes):
        glBegin(GL_LINES)
        glColor3f(r,g,b)
        glVertex2f(x, y)
        x1 = x + math.cos(2 * math.pi * i / spokes) * radius
        y1 = y + math.sin(2 * math.pi * i / spokes) * radius
        glVertex2f(x1, y1)
        glEnd()
def draw_barrel(x, y, radius, height, color):
    # glRotatef(180,0,1,0)
    glBegin(GL_POLYGON)
    glColor3f(*color)

    # glVertex2f(x-(radius/3), y)
    glVertex2f(x-(radius), y)
    glVertex2f(x, y + height)
    glVertex2f(x + radius-(radius/3), y + height)
    glVertex2f(x + radius, y)
    glEnd()

# Function to draw the cannon
def draw_cannon(angle):
    # Rotate around the Z-axis
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    
    x=0
    y=0
    # glTranslatef(0, 0, 0)
    # glTranslatef(x, y, 0.0)
    draw_barrel(x, y, .2, .5, (0.4, 0.4, 0.4))
    draw_wheel(x,y,.2, 12,0.27, 0.13, 0.07) 
    

# Main loop
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle += 6 
            elif event.key == pygame.K_RIGHT:
                angle -= 6 

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset the rotation matrix
    glRotatef(angle, 0.0, 0.0, 1.0)
    draw_cannon(angle)
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
