#https://www.youtube.com/watch?v=XqX5wh4YeRw

import bpy
from math  import radians

# Create cube
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object
so.location[0] =  2# x coordinate
so.location[2] =  3# z coordinate

 
so.rotation_euler[0] += radians(45)
# create  a  modifier 
modif_sbsurf = so.modifiers.new("my modifier",'SUBSURF')
modif_sbsurf.levels = 3

# Smooth short way   
#bpy.ops.object.shade_smooth()

  
# Smooth long  way
mesh = so.data            
for face in mesh.polygons:
    face.use_smooth =True
    
#Displacment modifier   
mod_displace = so.modifiers.new("my displace",'DISPLACE')
#Create   the  texture
new_tex = bpy.data.textures.new("my textures",'DISTORTED_NOISE')
#https://docs.blender.org/api/blender_python_api_current/info_quickstart.html 
new_tex.noise_scale = 1.5
mod_displace.texture = new_tex #Apply the texture

new_mat = bpy.data.materials.new(name="my matrial")
so.data.materials.append(new_mat)
new_mat.use_nodes= True
#bpy.data.materials["my matrial.008"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.655773, 0.8, 0.0724783, 1)
nodes = new_mat.node_tree.nodes# shortcut  variable
material_output = nodes.get("Material Output")
node_emission = nodes.new(type = 'ShaderNodeEmission')
node_emission.inputs[0].default_value =(0.0,0.3,1.0,1)#color
node_emission.inputs[1].default_value =500#strength

###########
 

 
links = new_mat.node_tree.links
#Create  new  link node emission output to material input
new_link = links.new(node_emission.outputs[0], material_output.inputs[0])      
bpy.context.scene.eevee.bloom_intensity = 0.136798
