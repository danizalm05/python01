"""
 The Blender Python API
  Precision 3D Modeling and Add-on Development
"""
 
import bpy  
#page 9 
def boxgroup():
 for k in range(5):
   for j in range(5):
    for i in range(5):
     bpy.ops.mesh.primitive_cube_add( size=0.1, location=(i, j, k)) 
 return
#boxgroup

def mySelector(objName, additive=False):
  """
  Take  an object name as an argument and selects it,
  clearing all other selections by default
 
  """
  # By default, clear other selections
  if not additive:
      bpy.ops.object.select_all(action='DESELECT')
# Set the 'select' property of the datablock to True
  bpy.data.objects[objName].select = True
 

#boxgroup()



objl = bpy.context.selected_objects 
print(objl )   # Outputs bpy.data.objects datablocks
 
l = [k.name for k in bpy.context.selected_objects]
print(l)# print list names of selected objects
org = [k.location for k in bpy.context.selected_objects]
print  (org)# Return the locations of selected objects

# Selecting Objects  13
# Select only 'Cube'
mySelector('Cube')