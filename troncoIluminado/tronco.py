from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from OpenGL.GL import *
from math import *
import math
g1 = 0
g2 = 1
g3 = 2
cores = ( (0.8,0.8,0.2),(0.5,0.5,0.5),(0.5,1,0),(0.5,1,1),(0.5,0.5,1),(1,0.5,1),(0.8,0.5,0.5),(0.5,0.5,0.4) )
def troncoIluminado():
    glPushMatrix()
    glTranslatef(0,-1.2,0)
    glRotatef(-110,1.0,0.0,0.0)
    base = []
    base2 = []
    raio = 3
    raio1 = 1
    lados = 7
    ang = (2*math.pi)/lados
    altura = 3
    glBegin(GL_POLYGON)
    for k in range(lados):
        x1 = raio1 * math.cos(k*ang)
        y1 = raio1 * math.sin(k*ang)
        base += [ (x1,y1) ]
        glVertex3f(x1,y1,0.0)
    a2 = (base[0][0],base[0][1],0.0)
    b2 = (base[1][0],base[1][1],0.0)
    c2 = (base[2][0],base[2][1],0.0)
    glNormal3fv(normal(a2,b2,c2))
    glEnd()

    glBegin(GL_POLYGON)
  
    for i in range(lados):
            x2 = raio * math.cos(i*ang)
            y2 = raio * math.sin(i*ang)
            base2 += [ (x2,y2) ]
            glVertex3f(x2,y2,altura)
    a1 = (base2[0][0],base2[0][1],altura)
    b1 = (base2[1][0],base2[1][1],altura)
    c1 = (base2[2][0],base2[2][1],altura)
    glNormal3fv(normal(a1,b1,c1))
    glEnd()
    glBegin(GL_QUADS)
    for i in range(lados):
        
        a = (base2[i][0],base2[i][1],altura)
        b = (base[i][0],base[i][1],0.0)
        c = (base[(i+1)%lados][0],base[(i+1)%lados][1],0.0)
        d = (base2[(i+1)%lados][0],base2[(i+1)%lados][1],altura)
        glNormal3fv(normal(a,b,d))
        glVertex3fv(a)
        glVertex3fv(b)
        glVertex3fv(c)
        glVertex3fv(d)
    glEnd()
    
    glPopMatrix()


def desenhar():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    troncoIluminado()
    glutSwapBuffers()

def normal(p0,p1,p2):
    global g1,g2,g3
    k = ( p2[g1]-p0[g1], p2[g2]-p0[g2], p2[g3]-p0[g3] )
    l = ( p1[g1]-p0[g1], p1[g2]-p0[g2], p1[g3]-p0[g3] )
    normal = ( ((k[g2]*l[g3])-(k[g3]*l[g2])),((k[g3]*l[g1])-(k[g1]*l[g3])),((k[g1]*l[g2])-(l[g2]*l[g1])))
    normalAltura = sqrt((normal[g1]*normal[g1])+(normal[g2]*normal[g2])+(normal[g3]*normal[g3]))
    return ( normal[g1]/normalAltura, normal[g2]/normalAltura, normal[g3]/normalAltura)

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def initin():
    mat_ambient = (0.5, 0.0, 0.0, 1.0)
    mat_diffuse = (0.8, 0.0, 0.0, 1.0)
    mat_specular = (0.8, 0.5, 0.5, 1.0)
    mat_shininess = (48,)
    light_position = (5, 0, 0)
    glClearColor(1.0,1.0,0.0,0.0)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
def res(weigth,height):
    glViewport(0,0,weigth,height)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(70,float(weigth)/float(height),0.1,40.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0.5,10,0,0,0,0,0.5,0)

def principal():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(1500,1500)
    glutCreateWindow("iluminando o tronco de uma pirâmide")
    initin()
    glutDisplayFunc(desenhar)
    glutReshapeFunc(res)   
    glutTimerFunc(50,timer,1)
    glutMainLoop()

principal()
