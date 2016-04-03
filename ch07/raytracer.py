#!/usr/bin/env python3

from vec3 import Vec3
from ray import Ray
from math import sqrt
from random import random
from hitable import Sphere
from hitable import HitableList
from camera import Camera

def random_in_unit_sphere():
  while True:
    p = 2.0*Vec3(random(),random(),random()) - Vec3(1,1,1)
    if Vec3.dot(p,p) < 1.0:
      return p

def color(r,world):
  rec = world.hit(r,0.0,float('inf'))
  if rec is not None:
    target = rec["p"]+rec["normal"] + random_in_unit_sphere()
    return 0.5 * color(Ray(rec["p"],target-rec["p"]),world)
  else:
    unit_direction = Vec3.unit_vector(r.direction)
    t = 0.5*(unit_direction.y +1.0)
    return (1.0-t)*Vec3(1.0,1.0,1.0) + t*Vec3(0.5,0.7,1.0)

def main():
  nx = 200
  ny = 100
  ns = 100
  print("P3\n",nx," ",ny,"\n255")

  l = []
  l.append(Sphere(Vec3(0,0,-1),0.5))
  l.append(Sphere(Vec3(0,-100.5,-1),100))

  world = HitableList(l)
  cam = Camera()
  for j in reversed(range(ny)):
    for i in range(nx):
      col = Vec3(0,0,0)
      for s in range(ns):
        u = (i+random())/nx
        v = (j+random())/ny
        r = cam.get_ray(u,v)
        p = r.point_at_parameter(2.0)
        col += color(r,world)

      col /= ns
      col = Vec3(sqrt(col[0]),sqrt(col[1]),sqrt(col[2]))
      ir = int(255.99*col[0])
      ig = int(255.99*col[1])
      ib = int(255.99*col[2])
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()