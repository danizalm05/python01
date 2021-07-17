import arcpy  
from arcpy import env  
env.workspace = 'c:/temp/'  
  
zPath = "C:/Users/rockman/Documents/ArcGIS/samples-data/itom/Geog485/Lesson1/us_boundaries.shp"

pDesc = arcpy.Describe(zPath)  
print"totofffff" 