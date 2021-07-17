"""
Data Visualization in Blender and Python
https://www.youtube.com/watch?v=Xrixs_XuDQo&feature=emb_logo
"""
import csv
import bpy  

bar_width = 1

bar_spacing = 1.5
with open('D://blender//prj//Bar_Graph_Resource_Files//sample.csv') as f:
    readout = list(csv.reader(f)) 

 
i=0
for a in readout:
    placement = readout.index(a) 
     
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
   
    for vert in new_bar.data.vertices: #scan 4 verix of the object
        vert.co[1] += 0.5 # Move  y coordinateup by 0.5
        vert.co[0] += bar_spacing *  placement + 0.5 # move  x coordinateup by
        
    #new_bar.scale = (bar_width, float(a[1]), 1)    
    new_bar.scale = (bar_width,   float(a[1]), 1) # scale by (x,y,z) 3d 
    print (a[1])  #20:00
    bpy.ops.object.text_add()
    bpy.context.object.data.align_x = 'RIGHT'
   
    bpy.context.object.data.align_y = 'CENTER'
    bpy.ops.transform.rotate(value = -1.5708)
    bpy.ops.transform.translate(value=(bar_spacing *  placement + 0.5, -0.5, 0))
    bpy.context.object.data.body = a[0]
print(dir(bpy.context.object.data.body))