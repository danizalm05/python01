#Stairs - Olav3D Tutorials
 
# https://www.youtube.com/watch?v=ky2Mp5yDGDA
#  

import bpy
from math  import sin, pi
 
 
for i in range(0,10):
   #  bpy.ops.mesh.primitive_cube_add(size=2,  location=(i, 0, 0), scale=(1, i*2, i*2))
      bpy.ops.mesh.primitive_cube_add(size=2,  location=(0, i*2, i*2)   )
      bpy.ops.transform.resize(value=(10, 1, 1))



 
from random import randint 
# Generate 50 cubes in random locations
for i in range(50): 
      l = [ randint( -30, 0 )  for axis in 'xyz' ]
      bpy.ops.mesh.primitive_cube_add(     location = l )
      
      
      
from math import sin 
# Generate 50 cubes along a sin curve 
for i in range(50):
    x, y, z = 10, i+22, sin( i )+15 
    bpy.ops.mesh.primitive_cube_add( location = (x, y, z) )
    
    
    
  
           