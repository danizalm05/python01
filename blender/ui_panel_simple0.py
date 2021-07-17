import bpy

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hell"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'm name'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello wortld!", icon='WORLD_DATA')
        row.operator('') 
        

class SHADER_OT_NEON(bpy.types.Operator):
    bl_label = "Add Neon Shader"
    bl_idname = 'shader.neon.operator'
     #4:44
    def execute(self, context):
        ###########
          
            #Creating a New Shader and calling it Neon
        material_neon = bpy.data.materials.new(name= "Neon")
            #Enabling Use Nodes
        material_neon.use_nodes = True
            #removing the Principled Node
        material_neon.node_tree.nodes.remove(material_neon.node_tree.nodes.get('Principled BSDF'))
            #Create a reference to the Material Output
        material_output = material_neon.node_tree.nodes.get('Material Output')
            #Set location of node
        material_output.location = (400,0)
        
            #Adding Glass1 Node
        emiss_node = material_neon.node_tree.nodes.new('ShaderNodeEmisson')
            #Set location of node
        emiss_node.location = (200,0)
            #Setting the Default Color
        emiss_node.inputs[0].default_value = (0.526541, 0.299214, 1, 1)
            #Setting the Default IOR Value
        emiss_node.inputs[2].default_value = 1.446
        
        ######
        
        ##############
        
        return('FINISHED')

def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
