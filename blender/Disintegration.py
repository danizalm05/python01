#https://www.youtube.com/watch?v=XqX5wh4YeRw

import bpy
from math  import radians

bpy.context.scene.render.engine = 'CYCLES'#Change  to  cycle



loca = (0, 0, 0)
scal=(1, 1, 1)
bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location= loca, scale=scal)

#bpy.ops.mesh.primitive_cube_add(align='WORLD', location= loca, scale=scal)
bpy.ops.object.editmode_toggle() #  toggle edit mode

bpy.ops.mesh.edge_split(type='EDGE')#Split by edges alt M

so = bpy.context.active_object# selected  object 

new_mat = bpy.data.materials.new(name="my matrial")#Create new  matrial
so.data.materials.append(new_mat)#append to the selected object
new_mat.use_nodes= True# Show the marials  node

#bpy.data.materials["my matrial.008"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.655773, 0.8, 0.0724783, 1)
nodes = new_mat.node_tree.nodes# shortcut  variable

bsdf = nodes.get("Principled BSDF")  
bsdf.location = (400,-10)


material_output = nodes.get("Material Output")
material_output.location = (700,-30)

#Add  vector displacment  node
node_vec_disp = nodes.new(type = 'ShaderNodeVectorDisplacement')
node_vec_disp.inputs[0].default_value =(0.78,0.3,1.0,55)#color
node_vec_disp.inputs[1].default_value = 1#strength
node_vec_disp.location = (130,60)#node   location 

#Add  texture cordinate node 
node_TexCoord = nodes.new(type = 'ShaderNodeTexCoord') 
node_TexCoord .location = (-200,-50) 

 #Add  texture value node 
node_Val = nodes.new(type="ShaderNodeValue") 
node_Val.location = (-80,-410) 

#add math node  subtruct
node_math = nodes.new(type="ShaderNodeMath") 
node_math.inputs[0].default_value =1
node_math.operation = 'SUBTRACT'


node_math.location = (110,-270)

#Links
links = new_mat.node_tree.links

#Create  new  link vector displacment  output to material_output
new_link = links.new(node_vec_disp.outputs[0], material_output.inputs[2])      
#bpy.context.scene.eevee.bloom_intensity = 0.136798

new_link = links.new(node_TexCoord.outputs[0], node_vec_disp.inputs[0])      
#3:35 

new_link = links.new(node_Val.outputs[0], node_vec_disp.inputs[2])      
#4:22
new_link = links.new(node_math.outputs[0],  bsdf.inputs[19]) 
new_link = links.new(node_Val.outputs[0],  node_math.inputs[1]) 
bpy.context.object.active_material.cycles.displacement_method = 'BOTH'
#change merial pro/setting/Displacement  to  displacment and bump 


#bpy.ops.node.add_node(type="ShaderNodeBsdfPrincipled", use_transform=True)






bpy.ops.object.editmode_toggle()#return to  object  mode
