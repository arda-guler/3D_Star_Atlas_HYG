import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

import keyboard

from graphics import *
from loader import *
from star import *
from camera import *
from ui_text import *

def main():
    star_data = read_data("hygdata_v3.csv")

    window_x = 1000
    window_y = 600
    near_clip = 1
    far_clip = 20000
    fov = 70
    point_size = 1
    
    cam_strafe_speed = 5
    cam_rotate_speed = 5
    cam_pitch_down = "W"
    cam_pitch_up = "S"
    cam_yaw_left = "A"
    cam_yaw_right = "D"
    cam_roll_ccw = "Q"
    cam_roll_cw = "E"
    cam_strafe_up = "U"
    cam_strafe_down = "O"
    cam_strafe_right = "L"
    cam_strafe_left = "J"
    cam_strafe_forward = "I"
    cam_strafe_backward = "K"

    incr_dist = "T"
    decr_dist = "G"
    
    glfw.init()
    window = glfw.create_window(int(window_x),int(window_y),"HYG 3D Star Atlas", None, None)
    glfw.set_window_pos(window,100,100)
    glfw.make_context_current(window)
    
    gluPerspective(fov, int(window_x)/int(window_y), near_clip, far_clip)
    glEnable(GL_CULL_FACE)
    glPointSize(point_size)

    cam = camera("main_cam", [0,0,0], [[1,0,0],[0,1,0],[0,0,1]], True)
    cam.move([0,0,-10])

    max_dist = 64

    while not glfw.window_should_close(window):
        cam.rotate([(keyboard.is_pressed(cam_pitch_down) - keyboard.is_pressed(cam_pitch_up)) * cam_rotate_speed,
                    (keyboard.is_pressed(cam_yaw_left) - keyboard.is_pressed(cam_yaw_right)) * cam_rotate_speed,
                    (keyboard.is_pressed(cam_roll_ccw) - keyboard.is_pressed(cam_roll_cw)) * cam_rotate_speed])

        cam.move([(keyboard.is_pressed(cam_strafe_left) - keyboard.is_pressed(cam_strafe_right)) * cam_strafe_speed,
                  (keyboard.is_pressed(cam_strafe_down) - keyboard.is_pressed(cam_strafe_up)) * cam_strafe_speed,
                  (keyboard.is_pressed(cam_strafe_forward) - keyboard.is_pressed(cam_strafe_backward)) * cam_strafe_speed])

        if keyboard.is_pressed(incr_dist):
            max_dist *= 2
        elif keyboard.is_pressed(decr_dist):
            max_dist *= 0.5
        
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawOrigin()
        drawStars(star_data, cam, max_dist)
        render_numbers(str(max_dist), [0,1,0], [-11,6], cam, 0.2)
        glfw.swap_buffers(window)

main()
