# MarlinCancelObject script - Inject M486 G-code commands for Marlin's Cancel Object support
# Runs with the PostProcessingPlugin which is released under the terms of the AGPLv3 or higher.
# This script is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# By Aapo Saaristo, aapo.saaristo@protonmail.com
# https://github.com/shinmai/cura-M486

from ..Script import Script

class MarlinCancelObject(Script):
  def __init__(self):
      super().__init__()

  def getSettingDataString(self):
    return """{
      "name": "Marlin M486 - Cancel Object support",
      "key": "MarlinCancelObject",
      "metadata": {},
      "version": 2,
      "settings": {}
    }"""

  def execute(self, data):
    meshes=[] # array to hold meshnames for indexing

    for index, layer in enumerate(data):
      lines = layer.split("\n")
      for lindex, line in enumerate(lines):
        if ";MESH:" in line:
          meshname = line[6:]
          idx=-1 # default to non-object features that shouldn't be skipped
          if(meshname in meshes):
            idx=meshes.index(meshname)
          elif(meshname != "NONMESH"):
            meshes.append(meshname)
            idx=meshes.index(meshname)
          gcode_to_add = "\nM486 S%d ;Marlin Cancel Object support" % idx
          lines[lindex] = line + gcode_to_add
      data[index] = "\n".join(lines)
    
    # second loop through to insert number of objects
    for index, layer in enumerate(data):
      lines = layer.split("\n")
      for lindex, line in enumerate(lines):
        if ";LAYER_COUNT:" in line:
          gcode_to_add = "\nM486 T%d ;Marlin Cancel Object support" % len(meshes)
          lines[lindex] = line + gcode_to_add
          break
      data[index] = "\n".join(lines)
    return data