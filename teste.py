import glfw
from OpenGL.GL import *


def init():
    glClearColor(1,0,1,0)


def render():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0) 
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.2)
    glVertex2f(-0.5, 0.2)
    glEnd()

    
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0) 
    glVertex2f(-0.6, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0, 0.7)
    glEnd()

    
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0) 
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.1)
    glVertex2f(-0.1, -0.1)
    glEnd()


def main():
    glfw.init() 
    window = glfw.create_window(800, 600, "Minha primeira janela OpenGL", None, None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
    glfw.terminate()



if __name__ == "__main__":
    main()