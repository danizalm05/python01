
#  
# Saves the structure of the selected node in a  a file named glossy_rna.xml in 
#  project’s directory.
(specified in the root_rna parameter) to this file.
import bpy
import os
from rna_xml import rna2xml
 
file = open(os.path.dirname(bpy.data.filepath) + os.sep + 'glossy_rna.xml', 'w')
 
rna2xml(file.write, root_node = 'glossy_bsdf', root_rna = bpy.context.active_object.active_material.node_tree.nodes.active)
 
file.close()
    
  