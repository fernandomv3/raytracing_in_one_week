#!/usr/bin/env python3

from vec3 import Vec3
from ray import Ray
from math import sqrt
from random import random
from hitable import Sphere
from hitable import HitableList
from camera import Camera
from material import Lambertian
from material import Metal

def color(r,world,depth):
  rec = world.hit(r,0.001,float('inf'))
  if rec is not None:
    if depth >= 50:
      return Vec3(0,0,0)
    attenuation,scattered =rec["material"].scatter(r,rec)
    if attenuation is not None:
      return attenuation * color(scattered,world,depth +1)
    else:
      return Vec3(0,0,0)
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
  l.append(Sphere(Vec3(0,0,-1),0.5,Lambertian(Vec3(0.8,0.3,0.3))))
  l.append(Sphere(Vec3(0,-100.5,-1),100,Lambertian(Vec3(0.8,0.8,0.0))))
  l.append(Sphere(Vec3(1,0,-1),0.5,Metal(Vec3(0.8,0.6,0.2),1.0)))
  l.append(Sphere(Vec3(-1,0,-1),0.5,Metal(Vec3(0.8,0.8,0.8),0.3)))

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
        col += color(r,world,0)

      col /= ns
      col = Vec3(sqrt(col[0]),sqrt(col[1]),sqrt(col[2]))
      ir = int(255.99*col[0])
      ig = int(255.99*col[1])
      ib = int(255.99*col[2])
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()