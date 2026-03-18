# main.py
import numpy as np
import glm

from image_utils import save_image_to_file
from classes.camera import Camera, Ray
from classes.objects.sphere import Sphere
from classes.objects.plane import Plane

EPS = 1e-3


def trace(ray, scene_objects, depth, eye_pos=None):
    t_min = 0.001
    t_max = 1000.0

    nearest = t_max
    hit_obj = None
    hit_point = None

    # ---- cherche l'objet le plus proche ----
    for obj in scene_objects:
        res = obj.hit(ray, t_min, nearest)
        if res is not None:
            t, p = res
            nearest = t
            hit_obj = obj
            hit_point = p

    if hit_obj is None:
        return glm.vec3(0.0)  # fond noir

    # ---- si c'est la sphère et qu'elle est "refractive" ----
    if getattr(hit_obj, "material", "") == "refractive":
        # normale + direction
        N = glm.normalize(hit_obj.getNormal(hit_point))
        I = glm.normalize(ray.direction)

        # indices
        air_ior = 1.0
        mat_ior = float(getattr(hit_obj, "ior", 1.33))

        # dot(I, N) < 0 => entrée
        cos_in = glm.dot(I, N)

        if cos_in < 0.0:
            # air -> matériau
            eta = air_ior / mat_ior
            N_use = N
            origin = hit_point - N_use * EPS
        else:
            # matériau -> air (inverse N et ratio)
            eta = mat_ior / air_ior
            N_use = -N
            origin = hit_point - N_use * EPS

        # réfraction
        T = glm.refract(I, N_use, eta)

        # réflexion totale interne -> fallback reflect
        if glm.length(T) < 1e-6:
            new_dir = glm.normalize(glm.reflect(I, N_use))
        else:
            new_dir = glm.normalize(T)

        if depth <= 0:
            return glm.vec3(0.0)

        refr_ray = Ray(origin, new_dir)
        refr_col = trace(refr_ray, scene_objects, depth - 1, eye_pos)

        # “teinte” pour rendre la sphère visible (sinon quasi invisible)
        tint = glm.vec3(*getattr(hit_obj, "tint", (0.35, 1.0, 0.35)))
        trans = float(getattr(hit_obj, "transmittance", 0.90))

        return trans * (refr_col * tint)

    # ---- sinon : couleur simple (planes, etc.) ----
    return hit_obj.getColor(hit_point)


def main():
    width = 800
    height = 600

    cam = Camera(
        fov_y=90.0,
        screen_height=height,
        screen_width=width,
        position=[0.0, 0.0, 0.0],
        target=[0.0, 0.0, -1.0],
    )
    eye = glm.vec3(*cam.position)

    # ---- scène : pièce ----
    scene = []

    # murs (ajuste si ton prof a inversé gauche/droite)
    scene.append(Plane(point=[-5, 0, 0], normal=[1, 0, 0],  color=[1, 0, 0]))  # gauche rouge
    scene.append(Plane(point=[5, 0, 0],  normal=[-1, 0, 0], color=[0, 0, 1]))  # droite bleu
    scene.append(Plane(point=[0, 3, 0],  normal=[0, -1, 0], color=[1, 0, 1]))  # plafond magenta
    scene.append(Plane(point=[0, -3, 0], normal=[0, 1, 0],  color=[1, 1, 0]))  # sol jaune
    scene.append(Plane(point=[0, 0, -5], normal=[0, 0, 1],  color=[0, 1, 0]))  # fond vert
    scene.append(Plane(point=[0, 0, 5],  normal=[0, 0, -1], color=[0, 0, 0]))  # avant noir

    # ---- sphère refractive (sans nouvelle classe) ----
    sphere = Sphere(center=[0.0, 0.0, -4.0], radius=1.0, color=[0.0, 1.0, 0.0])

    # On “tag” la sphère en matériau réfractif
    sphere.material = "refractive"
    sphere.ior = 1.33                 # eau
    sphere.tint = (0.35, 1.0, 0.35)    # léger vert
    sphere.transmittance = 0.90        # + haut = + transparent

    # IMPORTANT : mets la sphère dans la scène (peu importe l'ordre, mais je la mets au début)
    scene.insert(0, sphere)

    # ---- rendu ----
    img = np.zeros((height, width, 3), dtype=np.float32)

    max_depth = 8
    aa_samples = 1  

    for y in range(height):
        for x in range(width):
            col_acc = glm.vec3(0.0)

            for _ in range(aa_samples):
                ox = np.random.rand()
                oy = np.random.rand()
                ray = cam.generateRay(x + ox, y + oy)

                col_acc += trace(ray, scene, max_depth, eye)

            col_acc /= aa_samples

            img[y, x, 0] = col_acc.x
            img[y, x, 1] = col_acc.y
            img[y, x, 2] = col_acc.z

    save_image_to_file(img, "image_refraction.png")


if __name__ == "__main__":
    main()
