"""
From a Photo to a 3D Model with Python and Blender Python API
https://www.youtube.com/watch?v=Q41QxPK5xzM
https://github.com/armindocachada/create-3d-model-using-python/tree/master 
 55:06
 
 """ 
import bpy  
vertices= []
edges = []
faces = []   

(X,W) = (300 , 300)
DX=1
DY=1

for X in range(0,W,DX):
    vertices.append((X,0,0))
#Create  a new  mash
new_mesh=bpy.data.meshes.new("new_mesh")
new_mesh.from_pydata(vertices,edges,faces)
new_mesh.update()
# make objec from the mesh
new_object = bpy.data.objects.new("new_object",new_mesh)

# Add  the new object  to  view layer
view_layer=bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)





"""
vertices=[(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),      (1,1,1),(1,-1,1),(-1,1,1),(-1,-1,1)]
# list of vertixs 0 to 7 (eight vertixs)
 
edges=[(0,4)]# Each number is a number of a vertix
faces=[(3,1,0,2),(7,5,4,6),(3,1,5,7)]


"""