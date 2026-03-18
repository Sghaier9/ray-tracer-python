# classes/objects/plane.py

import glm
from .object import Object

class Plane(Object):
    def __init__(self, point, normal, color):
        # point sur le plan
        self.point = glm.vec3(point[0], point[1], point[2])
        # normale normalisée
        self.normal = glm.normalize(glm.vec3(normal[0], normal[1], normal[2]))
        # couleur fixe du plan
        self.color = glm.vec3(color[0], color[1], color[2])

    def hit(self, ray, t_min, t_max):
        """
        Intersection rayon / plan.
        Retourne (t, hitPoint) si dans [t_min, t_max], sinon None.
        Formule : t = (D - O·n) / (d·n)  avec D = point sur le plan,
        n = normale, O = origine du rayon, d = direction.
        """
        denom = glm.dot(self.normal, ray.direction)
        # ray parallèle au plan ?
        if abs(denom) < 1e-6:
            return None

        t = glm.dot(self.point - ray.origin, self.normal) / denom

        if t < t_min or t > t_max:
            return None

        hitPoint = ray.origin + t * ray.direction
        return t, hitPoint

    def getColor(self, hitPoint):
        return self.color

    def getNormal(self, hitPoint):
        return self.normal
