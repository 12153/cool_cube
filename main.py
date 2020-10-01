import pygame
from pygame.locals import *
import pyramid
import random

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),  # 0
    (1, 1, -1),  # 1
    (-1, 1, -1),  # 2
    (-1, -1, -1),  # 3
    (1, -1, 1),  # 4
    (1, 1, 1),  # 5
    (-1, 1, 1),  # 6
    (-1, -1, 1),  # 7
)

second_vert = [(i[0]-2, i[1]-2, i[2]-4) for i in verticies]
third_vert = [(i[0]+2, i[1]-2, i[2]-4) for i in verticies]

cubes = [verticies, second_vert, third_vert]

edges = (
    (0, 1), (0, 3), (0, 4),
    (2, 1), (2, 3), (2, 6),
    (5, 1), (5, 4), (5, 6),
    (7, 3), (7, 4), (7, 6),
)

surfaces = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (4, 0, 3, 7),
    (2, 3, 6, 5),
    (0, 1, 5, 4),
    (3, 2, 6, 7),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
)


def cube(n, verticies):
    l = len(colors)
    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(colors[((n//50)+i) % l])
            glVertex3fv(verticies[vertex])

    glEnd()

    glBegin(GL_LINES)
    for i, edge in enumerate(edges):
        for vertex in edge:
            glColor3fv(colors[(n//25) % len(colors)])
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1440, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(60, (display[0]/display[1]), 0.1, 100)
    i = 0
    x = 0
    glTranslatef(0, 0, -5)
    glRotatef(0, 0, 0, 0)
    i = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube(i, cubes[0])
        pyramid.pyramid()
        i += 1
        glRotatef(1, 0, 1, -1)
        glTranslatef(0, 0, 0)
        pygame.display.flip()
        pygame.time.wait(10)


main()
