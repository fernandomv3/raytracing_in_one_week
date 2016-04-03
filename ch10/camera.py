from ray import Ray
from vec3 import Vec3
import math
import random

class Camera:
  def __init__(self,lookfrom,lookat,vup,vfov,aspect):
    theta = vfov * math.pi/180
    half_height = math.tan(theta/2)
    half_width = aspect * half_height
    self.origin = lookfrom
    self.w = Vec3.unit_vector(lookfrom -lookat)
    self.u = Vec3.unit_vector(Vec3.cross(vup,self.w))
    self.v = Vec3.cross(self.w,self.u)
    self.lower_left_corner = self.origin - half_width*self.u -half_height*self.v -self.w
    self.horizontal = 2*half_width*self.u
    self.vertical = 2*half_height*self.v

  def get_ray(self,s,t):
    return Ray(self.origin,self.lower_left_corner + s*self.horizontal + t*self.vertical -self.origin)