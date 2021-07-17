# https://www.youtube.com/watch?v=EBeboI59g_s&list=PLefCvatS_7TyRbFXdbE8vfIdacknoL1ub
# Objects that will move along sine waves
# Go to timeline  and press  paly


import bpy
from math  import sin, pi

for obj in bpy.data.objects:
    print(obj.name)

bpy.ops.mesh.primitive_cube_add(size=2)
red = bpy.context.selected_objects[0]
red.name = "red" 

bpy.ops.mesh.primitive_cube_add(size=4,location = (0,10,0))
blue = bpy.context.selected_objects[0]
blue.name = "blue" 

 
 

bpy.ops.mesh.primitive_cube_add(size=6,location = (0,20,0))
yellow = bpy.context.selected_objects[0]
yellow.name = "yellow" 
 

frame_number = 0
for i in range(0,101):
     bpy.context.scene.frame_set(frame_number)
    
     #red cube
     xr = i/2 * pi 
     yr = sin(xr) * 10
     zr = 0#10:54
     
     red.location =(xr, yr, zr)
     red.keyframe_insert(data_path = 'location', index= -1)

     #blue cube
     xb = i/3 * pi 
     yb = 10 + sin(xb) * 5
     zb = sin(xb) * 10 

     blue.location =(xb, yb, zb)#16:15
     blue.keyframe_insert(data_path = 'location', index= -1)

     #yellow cube
     yy = i/4 * pi  +20
     xy = sin(yy) * 5
     zy = 0

     yellow.location =(xy, yy, zy)# 
     yellow.keyframe_insert(data_path = 'location', index= -1)




     frame_number += 5# 12:30