from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import pi, cos, sin,sqrt
N1=50
N2=50
a = 0
def f(i,j):
     y=((i*2/(N1-1))**2)
     theta= 2*pi*j/(N2-1)
     z =(y**(1/2))*sin(theta)
     x = (y**(1/2))*cos(theta)          
     return x,y,z
def mesh():
    glPushMatrix()     
    glRotatef(a,1.0,0.0,0.0)  
    for i in range(0, N1):
        glBegin(GL_QUAD_STRIP)
        for j in range(0,N2):
            glColor3fv(((1.0*i/(N1-1)),0,1 - (1.0*i/(N1-1))))
            x, y, z = f(i,j)
            glVertex3f(x,y,z)
            glColor3fv(((1.0*(i+1)/(N1-1)),0,1 - (1.0*(i+1)/(N1-1))))
            x, y, z = f(i+1, j)
            glVertex3f(x,y,z)
        glEnd()
    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh()
    a+=1.5
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1024,1024)
glutCreateWindow("PARABOLOIDE CIRCULAR DE REVOLUCAO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(10,timer,1)
glutMainLoop()
