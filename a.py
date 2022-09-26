from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open('H:\\materias\\imagens\\apresentaççao\\potencia_energetica\seções cor\\BlackMarble_2012_A1_geo.tif')
# ds = gdal.Open('H:\\materias\\imagens\\apresentaççao\\potencia_energetica\\BlackMarble_2012_3km_geo.tif')
imarray = ds.ReadAsArray()
# print(imarray)
imarray = imarray.astype(np.uint16)

r = imarray[0]
g = imarray[1]
b = imarray[2]
f = np.add(np.add(r,g),b)
f = f/3
print(f.max())
f = f.astype(np.uint8)
for a in [r,g,b,f]:
    print(a.dtype, a.max())
print(f)

a = f>9
print(a)
a = a.astype(int) *255
print(a)
from PIL import Image
img = Image.fromarray(a)
img.show()