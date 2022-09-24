from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open("BlackMarble_2012_3km_gray_geo.tif")
ar = ds.ReadAsArray()
print(ar.shape)