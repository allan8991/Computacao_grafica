import math
import png
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

width, height = 500.0, 500.0
screen_translate = 0.5
pause_rotation = False
pespective = 60

n_points = 60

x0 = -1
y0 = -1
xf = 1
yf = 1
dx = 0.05
dy = 0.05
a = 0


def LoadTextures():
    global texture
    texture = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture)
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo,
                 GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def mapa(r, t, f):
    x = r*math.cos(t)*math.sin(f)
    y = r*math.sin(t)*math.sin(f)
    z = r*math.cos(f)
    return x, y, z

v = []
subdivisoes = 7
dr = .1
dt = math.pi / subdivisoes

fmin = 0
fmax = math.pi
dfi = math.pi / (subdivisoes * 2)

r = 1

t = 0
t_max = 2*math.pi
while t <= t_max:
    fi = fmin
    while fi <= fmax:
        x, y, z = mapa(r, t, fi)
        v += [[x, y, z]]
        fi += dfi
    t += dt


def myMap(v, b1, t1, b2, t2):
    return (v - b1)/(t1 - b1) * (t2 - b2) + b2


def desenhando():

    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_TRIANGLES)

    t = 0
    while t <= t_max:
        fi = fmin
        while fi <= fmax:
            x, y, z = mapa(r, t, fi)
            vertex = [x, y, z]
            glTexCoord2f(t/t_max, fi/fmax)
            glVertex3fv(vertex)

            glTexCoord2f(t/t_max, (fi+dfi)/fmax)
            glVertex3fv(mapa(r, t, fi+dfi))

            glTexCoord2f((t+dt)/t_max, (fi+dfi)/fmax)
            glVertex3fv(mapa(r, t+dt, fi+dfi))
            glTexCoord2f(t/t_max, fi/fmax)
            glVertex3fv(vertex)

            glTexCoord2f((t+dt)/t_max, fi/fmax)
            glVertex3fv(mapa(r, t+dt, fi))

            glTexCoord2f((t+dt)/t_max, (fi+dfi)/fmax)
            glVertex3fv(mapa(r, t+dt, fi+dfi))
            fi += dfi
        t += dt
    glEnd()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glRotatef(-a, 0, 0, 1)
    desenhando()
    glPopMatrix()

    glutSwapBuffers()
    if not pause_rotation:
        a += 1
    return




def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_MULTISAMPLE)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0., 0., 0., 1.)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, Width/Height, 0.1, 100.0)
    glTranslatef(0.0, -0.4, -6)


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA |
                        GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(int(width), int(height))
    window = glutCreateWindow("planeta terra")
    glutDisplayFunc(desenha)

    InitGL(width, height)

    glutTimerFunc(10, timer, 1)
   
    glutMainLoop()
main()
