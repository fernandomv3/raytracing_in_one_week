#!/usr/bin/env python
from __future__ import print_function, division
from vec3 import Vec3
from ray import Ray
from math import sqrt
from random import random
from hitable import Sphere
from hitable import HitableList
from camera import Camera
from material import Lambertian
from material import Metal
from material import Dielectric

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

def random_scene():
  l = []
  l.append(Sphere(Vec3(0,-1000,-1),1000,Lambertian(Vec3(0.5,0.5,0.5))))
  for a in range(-11,11):
    for b in range(-11,11):
      choose_mat = random()
      center = Vec3(a+0.9*random(),0.2,b+0.9*random())
      if (center -Vec3(4,0.2,0)).length() > 0.9:
        if choose_mat < 0.8: #diffuse
          l.append(Sphere(center,0.2,Lambertian(Vec3(random()*random(),random()*random(),random()*random()))))
        elif choose_mat < 0.95: #metal
          l.append(Sphere(center,0.2,Metal(Vec3(0.5*(1+random()),0.5*(1+random()),0.5*(1+random())),0.5*random())))
        else: #glass
          l.append(Sphere(center,0.2,Dielectric(1.5)))
  l.append(Sphere(Vec3(0,1,0),1.0,Dielectric(1.5)))
  l.append(Sphere(Vec3(-4,1,0),1.0,Lambertian(Vec3(0.4,0.2,0.1))))
  l.append(Sphere(Vec3(4,1,0),1.0,Metal(Vec3(0.7,0.6,0.5),0.0)))
  return HitableList(l)
def main():
  nx = 200
  ny = 100
  ns = 100
  print ("P3\n",nx," ",ny,"\n255")

  world = random_scene()

  lookfrom = Vec3(15,2,5)
  lookat = Vec3(0,0,0)
  dist_to_focus = (lookfrom-lookat).length()
  aperture = 0.125
  cam = Camera(lookfrom,lookat,Vec3(0,1,0),20,nx/ny,aperture,dist_to_focus)
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
      print (ir," ",ig," ",ib)

if __name__ == '__main__':
  main()