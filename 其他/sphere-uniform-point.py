## Description
## Evenly distributed points on sphere
## 在单位球面上随机取点, 保证随机取到的点是均匀的 (Packing Problem 密铺问题)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

## Normal Distribution
# for i in range(80):
#   x = random.normalvariate(0,1) # 服从标准正态分布的随机数
#   y = random.normalvariate(0,1)
#   z = random.normalvariate(0,1)
#   r = (x * x + y * y + z * z) ** (1/2)
#   ax.scatter(x/r, y/r, z/r, marker='o')
#    # print('x = ', x/r, 'y = ', y/r, 'z = ', z/r)
# plt.show()


## Spiral Approximation
from math import cos, sin, pi, sqrt

def sphereUniformPoint(num=80):
  dlong = pi*(3.0 - sqrt(5.0))
  dz = 2.0/num
  long = 0.0
  z = 1.0 - dz/2.0
  list_of_points = []
  for i in range(num):
    r = sqrt(1.0 - z**2)
    pt = (cos(long)*r, sin(long)*r, z)
    list_of_points.append(pt)
    z = z - dz                         # 竖坐标成等差数列，分成厚度相同的层
    long = long + dlong
  return list_of_points



if __name__ == '__main__':
  pts = sphereUniformPoint(80)
  for pt in pts:
    ax.scatter(pt[0], pt[1], pt[2], marker='o', c='b')
  plt.show()
