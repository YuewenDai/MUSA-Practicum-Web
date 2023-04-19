from osgeo import gdal

# Open the image that we want to copy the transform info from
ds_src = gdal.Open("D:/0MUSA/MUSA801/MUSA-Practicum-Web/county_page/data/port_51740_landcover_2014.tif")

# Get the projection and store it in a variable named "crs"
crs = ds_src.GetProjection()
print(crs)

# Get the georeference (geotransform or "affine transformation") information
# and store it in a variable named "gt". You can either get the info from the
# source image (line 15), or you can set it manually (lines 17-24). Learn more
# about these values at: https://gdal.org/tutorials/geotransforms_tut.html

# gt = ds_src.GetGeoTransform()

gt = (
    1717795,  # top left x
    10,       # horizontal pixel size
    0,        # row rotation
    1720779,  # top left y
    0,        # column rotation
    -10,      # vertical pixel size
)

print(gt)

# Open the image you want to copy the transform info to
ds_dst = gdal.Open("D:/0MUSA/MUSA801/MUSA-Practicum-Web/county_page/data/test2.tif")

# Set the crs and geotransform from the source image
ds_dst.SetProjection(crs)
ds_dst.SetGeoTransform(gt)

# Save a new copy of the destination image
gdal.GetDriverByName('GTiff').CreateCopy(
    'D:/0MUSA/MUSA801/MUSA-Practicum-Web/county_page/data/port-test-with-geoinfo.tif',  # New image file name
    ds_dst,
)
