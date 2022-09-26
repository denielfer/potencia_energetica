from osgeo import gdal

def valor_medio(filename) -> int:
    return gdal.Open(filename).ReadAsArray().sum()