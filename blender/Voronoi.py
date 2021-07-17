# Blender 2.8 Tutorial | Parametric Voronoi Sphere 
# https://www.youtube.com/watch?v=NMpGmFNXSKI&list=PL95vjV728MLe9-w5SVMyL3wQKIGvWYmCh&index=6


import bpy, bmesh
import numpy as np
from time import time
from mathutils import Vector

bpy.ops.mesh.primitive_cube_add(  location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 5
bpy.context.object.modifiers["Subdivision"].render_levels = 5

bpy.ops.object.modifier_add(type='CAST')

bpy.ops.object.modifier_add(type='DECIMATE')
bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
bpy.context.object.modifiers["Decimate"].angle_limit = 0.349066
bpy.context.object.modifiers["Decimate"].use_dissolve_boundaries = True
 
bpy.ops.object.modifier_add(type='WIREFRAME')
bpy.context.object.modifiers["Wireframe"].thickness = 0.2

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision.001"].levels = 4

bpy.ops.object.modifier_add(type='CAST')
bpy.context.object.modifiers["Cast.001"].factor = 4
 