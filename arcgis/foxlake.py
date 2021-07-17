# This script uses map algebra to find values in an
#  elevation raster greater than 3500 (meters).
'''
Traceback (most recent call last):
  File "D:/python/arcgis/foxlake.py", line 23, in <module>
    outRaster.save(inRaster+foxfile)
RuntimeError: ERROR 999998: Unexpected Error.


'''
import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True

  

fname = ""

inRaster = "C:\\Users\\rockman\\Documents\\ArcGIS\\samples-data\\itom\\Geog485\\Lesson1"
pFile = inRaster + "\\foxlake"


cutoffElevation =  500
# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")
outRaster = Raster(pFile) > cutoffElevation
foxfile = "foxlake_hi_10"

outRaster.save(inRaster+foxfile)

# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")