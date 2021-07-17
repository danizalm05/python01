 #-----     Blender Quick Tutorial No. 9 – Dynamic Mountains   --------
#https://www.christoph-werner.de/2019/08/13/blender-quick-tutorial-no-9-dynamic-mountains/

import bpy


bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.editmode_toggle()# Change to  edit mode


for x in range(4):
  bpy.ops.mesh.subdivide()


bpy.ops.object.editmode_toggle()# Change to  object mode
 
bpy.ops.object.modifier_add(type='DISPLACE')#displament  modifier

bpy.ops.texture.new( 0)

 






mat = bpy.data.materials['Material']
tex = bpy.data.textures.new("Texture", 'CLOUDS')
tex.noise_scale = 0.42
slot = mat.texture_slots.add()
#slot.texture = tex
 