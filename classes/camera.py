# camera.py

import glm
import numpy as np
from PIL import Image


class Ray:
    def __init__(self, origin, direction):
        self.origin = glm.vec3(origin.x, origin.y, origin.z)
        d = glm.vec3(direction.x, direction.y, direction.z)
        self.direction = glm.normalize(d)


class Camera:

    def __init__(self, fov_y, screen_height, screen_width, position, target):
        self.position = glm.vec3(position[0], position[1], position[2])
        self.up_vector = glm.vec3(0, 1, 0)

        self.fov_y = glm.radians(fov_y)
        self.screen_height = screen_height
        self.screen_width = screen_width

        view = glm.lookAt(
            self.position,
            glm.vec3(target[0], target[1], target[2]),
            self.up_vector
        )
        self.eye_to_world_matrix = glm.inverse(view)

    def generateRay(self, x_pixel, y_pixel):

        # 1) Pixel → NDC [-1,1]
        x_ndc = ((x_pixel + 0.5) / self.screen_width) * 2.0 - 1.0
        y_ndc = ((y_pixel + 0.5) / self.screen_height) * 2.0 - 1.0
        y_ndc = -y_ndc

        # 2) Espace caméra
        aspect = self.screen_width / self.screen_height
        tan_half = glm.tan(self.fov_y * 0.5)

        x_cam = x_ndc * tan_half * aspect
        y_cam = y_ndc * tan_half
        z_cam = -1.0

        dir_camera = glm.vec3(x_cam, y_cam, z_cam)

        # 3) direction → espace monde (w=0)
        dir_world4 = self.eye_to_world_matrix * glm.vec4(dir_camera.x, dir_camera.y, dir_camera.z, 0.0)
        dir_world = glm.vec3(dir_world4.x, dir_world4.y, dir_world4.z)

        return Ray(self.position, dir_world)
