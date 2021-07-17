import arcpy  
from arcpy import env

  
env.workspace = 'c:/temp/'
fname = "us_boundaries.shp"   #   dbf: dbf     shp: FeatureClass

path = "C:/Users/rockman/Documents/ArcGIS/samples-data/itom/Geog485/Lesson1/"
pFile = path + fname
print "--------------------------"
pDesc = arcpy.Describe(pFile)
print ("pDesc.featureType:  " + pDesc.featureType)
print ("pDesc.shapeType:  " + pDesc.shapeType)
print ("pDesc.DatasetType = %s" % pDesc.DatasetType)
print ("pDesc.File Name = %s" % pDesc.Name)
print ("pDesc.CatalogPath: " + pDesc.catalogPath)
print ("pDesc.dataElementType = %s" % pDesc.dataElementType)
print ("pDesc.children = %s" % pDesc.children)
print "--------------------------"

spatialRef = pDesc.spatialReference

print ("spatialRef.Name = %s" % spatialRef.Name)
pExtent = pDesc.Extent

# and here
print "Extent of shape :\nXMin: %f, YMin: %f, \nXMax: %f, YMax: %f" % \
      (pExtent.XMin, pExtent.YMin, pExtent.XMax, pExtent.YMax)

