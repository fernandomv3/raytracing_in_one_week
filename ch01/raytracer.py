#!/usr/bin/env python3

def main():
  nx = 200
  ny = 100
  print("P3\n",nx," ",ny,"\n255")

  for j in reversed(range(ny)):
    for i in range(nx):
      r = i / nx
      g = j / ny
      b = 0.2
      ir = int(255.99*r)
      ig = int(255.99*g)
      ib = int(255.99*b)
      print(ir," ",ig," ",ib)

if __name__ == '__main__':
  main()