# Extrude in Blender Along Function Graphs Using Python
 
# https://www.youtube.com/watch?v=Tk2-RIYSMEw
# Draw  y= x**2  on xy plane with extrude_region_move

import bpy
import numpy as np
# put avertex at the  point (-3,9,0) 
# press 7 on numpad and run 

xcoords = np.linspace(-3, 3, 100)
ycoords = [x**3 for x in xcoords]
 
 
 
for n, x in enumerate( xcoords ):
    if  (n < 99):
       dx = xcoords[n+1] - xcoords[n]  
       dy = ycoords[n+1] - ycoords[n]  
       
       bpy.ops.mesh.extrude_region_move(
       TRANSFORM_OT_translate={"value":(dx, dy, 0)}
       ) 
       
 

   