"""
https://www.youtube.com/watch?v=Ox79FqcFi6E&list=PLp4SJ1Ujrh7O1YrQs6UY05cQAmEpw9uK0&index=4
Python Scripting In Blender 
"""
 
import bpy  
from  bpy  import  context
#page 9 
def boxgroup():
 for k in range(2):
   for j in range(2):
    for i in range(2):
     bpy.ops.mesh.primitive_cube_add( size=0.6, location=(i, j, k)) 
 return
#boxgroup


boxgroup()

scene =  context.scene
print(scene)
print(scene.objects)#  Print  all  objects in the  scene

# Loop through  all objects
print(" all object in scene ")
for obj in scene.objects:
      print( obj,obj.location)

active_obj =context.active_object    
print("active_obj ",active_obj)  

#Change x location  of  active  object
active_obj.location.x += 2

#bpy.ops.object.select_all(action ='SELECT')#select all

#bpy.ops.object.select_all(action ='DESELECT')#deselect all
bpy.data.objects['Cube.001'].select_set(True) #select   'Cube.001'

bpy.ops.object.delete()# delete   'Cube.001'

bpy.ops.mesh.primitive_cylinder_add(  location=(0, 6, 0), scale=(1.9, 1, 1),depth =14)   

active_object =context.active_object    
print("active_object ",active_object)  
active_object.rotation_euler = (0,360 ,0) # rotate around y aix
active_object.scale.xyz =(1.22,1,1)
print("active_object.type ",active_object.type)  

#Create  new  material
mat = bpy.data.materials.new(name = 'MMMM')

active_object.data.materials.append(mat)  #Add new   material to active   object
#set color  to new  material
bpy.context.object.active_material.diffuse_color = (1,0,0,0.7)

# Change mode from object to edit , how to subdivide an object
bpy.ops.mesh.primitive_cube_add( size=2.6, location=(6, 2, 2)) 
bpy.ops.object.mode_set(mode='EDIT') 

bpy.ops.mesh.subdivide(number_cuts = 4)
bpy.ops.object.mode_set(mode='OBJECT')  
# add  subdivide surface modifiers 
bpy.ops.mesh.primitive_cube_add(  location=(0, 6, 0)  )

active_obj =context.active_object    
print("active_obj ",active_obj)#  2:16

# modifiers
mod = active_obj.modifiers.new('mmy_mod','SUBSURF') 
mod.levels = 2
mod.quality = 4
mod.render_levels = 4

#copy  and paste
newg_obj = active_obj.copy()
scene = context.scene
scene.collection.objects.link(new_obj)