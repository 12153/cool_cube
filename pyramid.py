import pygame
from pygame.locals import *
import random

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),
)


def pyramid():
    glBegin(GL_POLYGON)
    for edge in edges:
        for v in edge:
            glVertex3fv(vertices[v])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for v in edge:
            glColor3f(1, 1, 0)
            glVertex3fv(vertices[v])
    glEnd()
