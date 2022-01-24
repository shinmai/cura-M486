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
    meshes=[]
    for index, layer in enumerate(data):
      lines = layer.split("\n")
      for lindex, line in enumerate(lines):
        if ";MESH:" in line:
          meshname = line[6:]
          idx=-1
          if(meshname in meshes):
            idx=meshes.index(meshname)
          elif(meshname != "NONMESH"):
            meshes.append(meshname)
            idx=meshes.index(meshname)
          gcode_to_add = "\n;Marlin Cancel Object support: \nM486 S%d" % idx
          lines[lindex] = line + gcode_to_add
      data[index] = "\n".join(lines)
    return data