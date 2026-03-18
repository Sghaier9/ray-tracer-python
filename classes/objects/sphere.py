# classes/objects/sphere.py

import glm
from .object import Object   # import de la classe abstraite

class Sphere(Object):
    def __init__(self, center, radius, color):
        # center : [x,y,z] ou glm.vec3
        self.center = glm.vec3(center[0], center[1], center[2])
        self.radius = radius
        self.color = glm.vec3(color[0], color[1], color[2])

    def hit(self, ray, t_min, t_max):
        """
        Teste l'intersection rayon / sphère.
        Retourne (t, hitPoint) si ça touche, sinon None.
        """
        oc = ray.origin - self.center

        a = glm.dot(ray.direction, ray.direction)
        b = 2.0 * glm.dot(oc, ray.direction)
        c = glm.dot(oc, oc) - self.radius * self.radius

        discriminant = b * b - 4.0 * a * c
        if discriminant < 0.0:
            return None

        sqrt_disc = glm.sqrt(discriminant)

        # plus proche intersection
        t = (-b - sqrt_disc) / (2.0 * a)
        if t < t_min or t > t_max:
            # on essaye la deuxième racine
            t = (-b + sqrt_disc) / (2.0 * a)
            if t < t_min or t > t_max:
                return None

        hitPoint = ray.origin + t * ray.direction
        return t, hitPoint

    def getColor(self, hitPoint):
        return self.color

    def getNormal(self, hitPoint):
        # normale : (P - C) normalisé
        return glm.normalize(hitPoint - self.center)
