from vec3 import Vec3
from ray import Ray
from random import random
import math

class Material:
  def scatter(self,r_in,rec):
    pass

  @classmethod
  def random_in_unit_sphere(cls):
    while True:
      p = 2.0*Vec3(random(),random(),random()) - Vec3(1,1,1)
      if Vec3.dot(p,p) < 1.0:
        return p

class Lambertian(Material):
  def __init__(self, a = Vec3()):
    self.albedo = a

  def scatter(self, r_in,rec):
    target = rec["p"] + rec["normal"] + Material.random_in_unit_sphere()
    scattered = Ray(rec["p"],target - rec["p"])
    attenuation = self.albedo
    return attenuation,scattered

class Metal(Material):
  def __init__(self,a = Vec3(),f = 0.0):
    self.albedo = a
    self.fuzz = min(f, 1.0)

  def scatter(self, r_in,rec):
    reflected = Vec3.reflect(Vec3.unit_vector(r_in.direction),rec["normal"])
    scattered = Ray(rec["p"],reflected + self.fuzz * Material.random_in_unit_sphere())
    attenuation = self.albedo
    if Vec3.dot(scattered.direction,rec["normal"]) > 0:
      return attenuation,scattered
    else:
      return None,None