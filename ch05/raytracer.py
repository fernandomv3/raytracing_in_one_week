#!/usr/bin/env python3

from vec3 import Vec3
from ray import Ray
from math import sqrt
from hitable import Sphere
from hitable import HitableList

def color(r,world):
  rec = world.hit(r,0.0,float('inf'))
  if rec is not None:
    return 0.5 * (rec["normal"] +1)
  else:
    unit_direction = Vec3.unit_vector(r.direction)
    t = 0.5*(unit_direction.y +1.0)
    return (1.0-t)*Vec3(1.0,1.0,1.0) + t*Vec3(0.5,0.7,1.0)

def main():
  nx = 200
  ny = 100
  print("P3\n",nx," ",ny,"\n255")
  
  lower_left_corner = Vec3(-2.0,-1.0,-1.0)
  horizontal = Vec3(4.0,0.0,0.0)
  vertical = Vec3(0.0,2.0,0.0)
  origin = Vec3(0.0,0.0,0.0)

  l = []
  l.append(Sphere(Vec3(0,0,-1),0.5))
  l.append(Sphere(Vec3(0,-100.5,-1),100))

  world = HitableList(l)

  for j in reversed(range(ny)):
    for i in range(nx):
      u = i/nx
      v = j/ny
      r = Ray(origin,lower_left_corner + u*horizontal + v* vertical)

      p = r.point_at_parameter(2.0)
      col = color(r,world)

      ir = int(255.99*col[0])
      ig = int(255.99*col[1])
      ib = int(255.99*col[2])
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()