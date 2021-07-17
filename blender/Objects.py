# Objects From Scratch - Olav3D Tutorials
 
# https://www.youtube.com/watch?v=tsmkqU25_As&list=PLunr0YiKm4r4OqzEfMrGSPYS1WuvaSRu5
# 
# be in object mode with nothing selected. 
 
import bpy
  
verts = [(0,0,0),(0,2,0),(2,2,0),(2,0,0)] # 4 vrtixes
faces = [(0,1,2,3)]# each number is a number of a vertex in the 'verts' list
edges = []
   

    
 
mesh = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Plane",mesh)
bpy.context.collection.objects.link(object)
 
mesh.from_pydata(verts, edges, faces)  
                    
object.location =(0,0,5) 
#mesh.update(calc_edges = True)
  