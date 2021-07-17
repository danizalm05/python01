#Spiral Staircase - Olav3D Tutorials
 
# https://www.youtube.com/watch?v=xZ8hDKb51Y0
#  
#Spiral Staircase - Olav3D Tutorials
 
# https://www.youtube.com/watch?v=xZ8hDKb51Y0
#  

import bpy
import math    as m 
 
n = 80
r = 4
z = 0 
for i in range(1,n+1):
  angle = ((i-1)*4*m.pi)/n
  x = r*m.cos(angle)
  y = r*m.sin(angle)

  bpy.ops.mesh.primitive_cube_add(size=2, location=(x, y, z), scale=(1, 1, 1))
  bpy.ops.transform.resize(value=(2, 1, 0.2))
  
  
  bpy.context.object.rotation_euler[2] = angle

  z +=   0.4#5.43
#create  the  main  pole
a = z/2  
bpy.ops.mesh.primitive_cylinder_add(radius= r-1, depth = z, location=(0, 0, a))

bpy.ops.object.editmode_toggle()
