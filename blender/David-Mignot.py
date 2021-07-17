#https://www.youtube.com/watch?v=r8hqLh_HE08
# Artistic Coding in Blender by David Mignot
import   bpy
from  bpy  import  context
import random

mat1 = bpy.data.materials.new(name="Material001") #set new material to variable
mat2 = bpy.data.materials.new(name="Material002")  
mat3 = bpy.data.materials.new(name="Material003")  
spacing  = 2.2
for x in  range(8):  
    for y in  range(4):
       s = (1, 1, 5*random.random())
       location=(x * spacing, y * spacing,random.random()*2) 
       bpy.ops.mesh.primitive_cube_add(location=location,scale = s)
               
       item = bpy.context.active_object #Set active object to variable
    
       if random.random()<=0.2:
            item.data.materials.append(mat1) #add the material to the object
            bpy.context.object.active_material.diffuse_color = (0 ,0, 1,0.4) #change color
         
       elif ( 0.2< random.random() <=0.3  ):
            item.data.materials.append(mat2) #add the material to the object
            bpy.context.object.active_material.diffuse_color = (0 ,8, 150,0.3) #change color
       else: 
             item.data.materials.append(mat3) #add the material to the object
             bpy.context.object.active_material.diffuse_color = (50,0 ,250,0.5) #change color   
              
 
 

 
l= len  (bpy.context.window.scene.objects)#number of  objects
print ("number of  objects = ", l)

for i in range(l): #Print  names of objectas

   obj = bpy.context.window.scene.objects[i]
   bpy.context.view_layer.objects.active = obj    # 'obj' is the active object now
   print(i,":", bpy.context.object.name)       

m = bpy.data.objects["Cube"]  #Search for  spacific  object 
print(m.name)  
 