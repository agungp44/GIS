import shapefile
f = shapefile.Reader("E:/Kuliah/GIS/Agung/agung.shp")
shapes = f.shapes()
print len (shapes)