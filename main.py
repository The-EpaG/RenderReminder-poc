from lib import PluginInterface, BlenderObject
from plugin import *

classes = PluginInterface.__subclasses__()

# Creation
print("# Creation")
blender_object = BlenderObject(classes)
print()

# Execution
print("# Draw")
blender_object.draw()
print(blender_object.layout)
print()

# Execution
print("# Execution")
blender_object.execute()