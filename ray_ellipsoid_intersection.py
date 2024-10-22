# ray_sphere_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
# Output:
#  Print the x, y, and z coordinates of the intersection if it exists
#
# Written by Evan Schlein
# Other contributors: None

import math # math module
import sys # argv  
# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# initialize script arguments
d_l_x= float('nan') # x-component of origin-referenced ray direction
d_l_y= float('nan') # y-component of origin-referenced ray direction
d_l_z= float('nan') # z-component of origin-referenced ray direction
c_l_x= float('nan') # x-component offset of ray origin
c_l_y= float('nan') # y-component offset of ray origin
c_l_z= float('nan') # z-component offset of ray origin

# parse script arguments
if len(sys.argv)==7:
  d_l_x = float(sys.argv[1])
  d_l_y = float(sys.argv[2])
  d_l_z = float(sys.argv[3])
  c_l_x = float(sys.argv[4])
  c_l_y = float(sys.argv[5])
  c_l_z = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

# write script below this line
a = d_l_x**2+d_l_y**2+(d_l_z**2)/(1-E_E**2)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-E_E**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E_KM**2
discr = b*b-4.0*a*c

# solution logic
if discr >= 0.0:
    d = (-b - math.sqrt(discr))/(2*a)
    if d < 0.0:
        d = (-b + math.sqrt(discr))/(2*a)
    if d >= 0.0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])
