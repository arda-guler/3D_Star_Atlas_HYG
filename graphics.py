import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

from math_utils import *

def drawOrigin():
    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,1000,0)
    glColor(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(1000,0,0)
    glColor(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1000)
    glEnd()

def drawStars(stars, cam, max_dist=None):
    
    for star in stars:
        if max_dist and float(star.dist) > max_dist:
            pass
        elif float(star.dist) >= 100000:
            pass
        else:
            x = float(star.x)
            y = float(star.z)
            z = float(star.z)

            lum = float(star.lum)
            bright = max(min(lum, 10), 0.1) / 10

            if star.spect:
                main_spect = star.spect[0]

                if main_spect == "O":
                    glColor(0, bright * 0.1, bright)
                elif main_spect == "B":
                    glColor(0, bright * 0.4, bright)
                elif main_spect == "A":
                    glColor(bright * 0.85, bright * 0.85, bright)
                elif main_spect == "F":
                    glColor(bright, bright, bright)
                elif main_spect == "G":
                    glColor(bright, bright * 0.8, bright * 0.8)
                elif main_spect == "K":
                    glColor(bright, bright * 0.6, bright * 0.6)
                elif main_spect == "M":
                    glColor(bright, bright * 0.2, bright * 0.2)
                else:
                    glColor(bright, bright, bright)
                    
            else:
                glColor(bright, bright, bright)
            
            glBegin(GL_POINTS)
            glVertex3f(x, y, z)
            glEnd()
