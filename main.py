import shapefile
f = shapefile.Reader("E:/Agung/agung.shp")
shapes = f.shapes()
print len (shapes)