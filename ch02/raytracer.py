#!/usr/bin/env python3

from vec3 import Vec3

def main():
  nx = 200
  ny = 100
  print("P3\n",nx," ",ny,"\n255")

  for j in reversed(range(ny)):
    for i in range(nx):
      col = Vec3(i/nx,j/ny,0.2)

      ir = int(255.99*col[0])
      ig = int(255.99*col[1])
      ib = int(255.99*col[2])
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()