#!/usr/bin/env python3

from vec3 import Vec3
from ray import Ray

def color(r):
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

  for j in reversed(range(ny)):
    for i in range(nx):
      u = i/nx
      v = j/ny
      r = Ray(origin,lower_left_corner + u*horizontal + v* vertical)
      col = color(r)
      ir = int(255.99*col[0])
      ig = int(255.99*col[1])
      ib = int(255.99*col[2])
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()