from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0



cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
def piramide():
    raio = 2
    raio2 = 2
    N = 5
    H = 4.0
    pontosBase = []
    pontosBase1 = []
    angulo =(2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3f(1,0,0)

    # BASE INFERIOR
    
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)       
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()
    glColor3f(0.5,0.5,0.5)
    # BASE SUPERIOR
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x1 = raio2 * math.cos(i*angulo)
        y1 = raio2 * math.sin(i*angulo)       
        pontosBase1 += [ (x1,y1) ]
        glVertex3f(x1,y1,H)
    glEnd()

    # LATERAL
    glBegin(GL_QUADS)  
   
    for i in range(0,N): 
        
        glColor3fv(cores[(i+1)%len(cores)])       
        glVertex3f(pontosBase1[i][0],pontosBase1[i][1],H)
        glVertex3f(pontosBase1[(i+1)%N][0],pontosBase1[(i+1)%N][1],H)        
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        glVertex3f(pontosBase[(i)][0],pontosBase[(i)][1],0.0)
        
    glEnd()

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    piramide()
    a+=0.5
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()
