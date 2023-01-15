''' Jeff Heaton
 
https://www.youtube.com/watch?v=EaXy-m2I5hs&list=PLjy4p-07OYzstXSMLnVY18PHlm1b_eQOf&index=2
https://github.com/jeffheaton/present/tree/master/youtube/blender/intro


7:00
21:00
'''




import bpy
from math import pi, radians
from mathutils import Euler
import os
import random
import sys

p = os.path.dirname(__file__)
PATH = os.path.dirname(p) #os.getcwd()
OUTPUT_PATH = os.path.join(PATH,"output")

print(f"Path:==> {PATH}")

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

def reset_blend():
    bpy.ops.wm.read_factory_settings()

    for scene in bpy.data.scenes:
        for obj in scene.objects:
            scene.objects.unlink(obj)

    # only worry about data in the startup scene
    for bpy_data_iter in (
            bpy.data.objects,
            bpy.data.meshes,
            bpy.data.lamps,
            bpy.data.cameras,
    ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)

def removeAll(type=None):
    # Possible type: ‘MESH’, ‘CURVE’, ‘SURFACE’, ‘META’, ‘FONT’, ‘ARMATURE’, ‘LATTICE’, ‘EMPTY’, ‘CAMERA’, ‘LAMP’
    if type:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=type)
        bpy.ops.object.delete()
    else:
        # Remove all elements in scene
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=False)
        
   
def lamp(location, type='POINT', energy=1, color=(1,1,1), target=None):
    # Lamp types: 'POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'
    print('createLamp called')
    bpy.ops.object.add(type='LIGHT', location=location)
    obj = bpy.context.object
    obj.data.type = type
    obj.data.energy = energy
    obj.data.color = color

    if target: trackToConstraint(obj, target)
    return obj

# http://web.purplefrog.com/~thoth/blender/python-cookbook/load-image-texture.html
def material_for_texture(name, path):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(path)
    mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    return mat

def camera(location,rotation):
    bpy.ops.object.add(type='CAMERA', location=location)
    cam = bpy.context.object
    cam.rotation_euler = Euler((radians(rotation[0]), 
        radians(rotation[1]), radians(rotation[2])), 'XYZ')
    bpy.context.scene.camera = cam
    return cam

def floor(mat):
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0,0,0))
    pl = bpy.context.object
    pl.name = 'ground'
    pl.scale = (100, 100, 0.1)
    pl.data.materials.append(mat)
    bpy.ops.rigidbody.object_add(type='PASSIVE')
    

### base_block
#####################################
def base_block(mat, rotation, location, scale, is_cube):
    location2 = [location[0] - 6, location[1] + 7, location[2]]
    footprint = scale[:]
    
    if rotation[0]:
        footprint = (footprint[0],footprint[2],footprint[1])
        
    if rotation[1]:
        footprint = (footprint[2],footprint[1],footprint[0])
    
    if rotation[2]:
        footprint = (footprint[1],footprint[0],footprint[2])
    
    x = location2[0] + (footprint[0]/2)
    y = location2[1] - (footprint[1]/2) 
    z = location2[2] + (footprint[2]/2)

    if is_cube:
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 4
        bpy.context.object.modifiers["Bevel"].profile = .8
    else:    
        bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=1, enter_editmode=False, 
            align='WORLD', location=(x, y, z))

    bpy.ops.rigidbody.object_add()
    block1 = bpy.context.object
    block1.rigid_body.type = 'ACTIVE'    
    block1.scale = scale
    block1.data.materials.append(mat)
    
    rotation2 = [(radians(90) if c else 0) for c in rotation]
        
    block1.rotation_euler = Euler(rotation2, 'XYZ')

def red_block(location, rotation):
    base_block(red_mat, rotation, location, (4,2,1), True)
    
def yellow_block(location, rotation):
    base_block(yellow_mat, rotation, location, (8,2,1), True)

def blue_block(location, rotation):
    base_block(blue_mat, rotation, location, (2,2,1), True)
    
def green_block(location, rotation):
    base_block(green_mat, rotation, location, (4,1,1), True)
    
def orange_block(location, rotation):
    base_block(orange_mat, rotation, location, (2,1,1), True)

    
def purple_block(location, rotation):
    base_block(purple_mat, rotation, location, (1,1,2), False)

def yellow_round_block(location, rotation):
    base_block(yellow_mat, rotation, location, (1,1,4), False) 
    
def house():
    blue_block((0,0,0), (True, False, True) )
    blue_block((0,0,2), (True, False, True) )
    blue_block((0,2,0), (True, False, True) )
    blue_block((0,2,2), (True, False, True) )
    
    blue_block((3,0,0), (True, False, True) )
    blue_block((3,0,2), (True, False, True) )
    blue_block((4,0,0), (True, False, True) )
    blue_block((4,0,2), (True, False, True) )
    
    blue_block((7,0,0), (True, False, True) )
    blue_block((7,0,2), (True, False, True) )
    blue_block((7,2,0), (True, False, True) )
    blue_block((7,2,2), (True, False, True) )
    
    red_block((0,0,4), (False, False, False) )
    red_block((4,0,4), (False, False, False) )
    yellow_block((0,2,4), (False, False, False) )
    
    blue_block((1,-1,0), (True, False, False) )

def overhead():
    blue_block((6,0,0), (False, False, True) )
    red_block((0,0,0), (False, False, False) )
    yellow_block((0,-3,0), (False, False, False) )
    green_block((4,-6,0), (False, False, False) )
    orange_block((0,-6,0), (False, False, False) )
    purple_block((0,-8,0), (True, False, True) )
    yellow_round_block((4,-8,0), (True, False, True) )
    
def lineup():
    blue_block((8,0,0), (True, False, False) )
    red_block((0,0,0), (True, True, False) )
    yellow_block((1,-3,0), (False, False, False) )
    green_block((6,-0,0), (False, True, True) )
    orange_block((0,-6,0), (False, True, True) )
    purple_block((9,-6,0), (False, False, True) )
    yellow_round_block((3,0,0), (False, False, True) )
  
def render(filename):
    rnd = bpy.data.scenes['Scene'].render
    rnd.resolution_x = 1280
    rnd.resolution_y = 720
    rnd.resolution_percentage = 100
    rnd.filepath = os.path.join(OUTPUT_PATH, filename)
    bpy.ops.render.render(animation=False, write_still=True)
    

def init():
    removeAll()
    #reset_blend()

    # Create camera
    camera(location=(25, -30, 20),rotation=(70,0,30))

    # Light
    lamp((21.249, -8.4169, 20),energy=10000)
    
    floor(floor_mat)

# Create a material.
floor_mat = material_for_texture("Mat-red", os.path.join(PATH,"wood-floor.jpg"))
red_mat = material_for_texture("Mat-red", os.path.join(PATH,"wood-red.png"))
blue_mat = material_for_texture("Mat-blue", os.path.join(PATH,"wood-blue.png"))
yellow_mat = material_for_texture("Mat-yellow", os.path.join(PATH,"wood-yellow.png"))
orange_mat = material_for_texture("Mat-orange", os.path.join(PATH,"wood-orange.png"))
green_mat = material_for_texture("Mat-green", os.path.join(PATH,"wood-green.png"))
purple_mat = material_for_texture("Mat-purple", os.path.join(PATH,"wood-purple.png"))

init()
house()

"""
1. overhead()
2. lineup()


print(" sys.version ==>", sys.version)
print("sys.api_version   ==>", sys.api_version )
print(" sys.version_info   ==>", sys.version_info  )"""