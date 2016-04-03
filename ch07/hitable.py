from vec3 import Vec3
from math import sqrt

class Hitable:
  def hit(self,r,t_min,t_max):
    pass

class Sphere(Hitable):
  def __init__(self, cen = Vec3(), r = 1.0):
    self.center = cen
    self.radius = r

  def hit(self,r,t_min,t_max):
    rec = None
    oc = r.origin - self.center
    a = Vec3.dot(r.direction,r.direction)
    b = Vec3.dot(oc,r.direction)
    c = Vec3.dot(oc,oc) - (self.radius*self.radius)
    discriminant = (b*b) - (a*c)
    if discriminant > 0:
      rec = {}
      temp = (-b - sqrt(discriminant)) / a
      if t_min < temp < t_max:
        rec["t"] = temp
        rec["p"] = r.point_at_parameter(rec["t"])
        rec["normal"] = (rec["p"] - self.center) / self.radius
        return rec
      temp = (-b + sqrt(discriminant)) / a
      if t_min < temp < t_max:
        rec["t"] = temp
        rec["p"] = r.point_at_parameter(rec["t"])
        rec["normal"] = (rec["p"] - self.center) / self.radius
        return rec
    return None

class HitableList(Hitable):
  def __init__(self,l = []):
    self.list = l

  def hit(self,r,t_min,t_max):
    result = {}
    hit_anything = False
    closest_hit = t_max
    for h in self.list:
      temp_rec = h.hit(r,t_min,closest_hit)
      if temp_rec is not None:
        hit_anything = True
        closest_hit = temp_rec["t"]
        result = temp_rec
    if hit_anything:
      return result
    return None