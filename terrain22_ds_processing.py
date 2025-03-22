import os
import pandas as pd
import sklearn as skt
import matplotlib.pyplot as plt
import rasterio
import numpy as np
from shapely.geometry import box
from pyproj import Transformer
import geopandas as gpd
from rasterio.plot import show

file_path = "D:/Users/Nipun/Projects/HeightGAN/tiffs/Ras_74_terrain22_by_Gcluster15_Sinks.tif"

# "mountains", "plain", "plateau", "valley", "cliff", "highlands", "hills",
classes = {
    1: "plain",
    2: "mountains",
    3: "cliff",
    4: "highlands",
    5: "highlands",
    6: "plateau",
    7: "plateau",
    8: "valley",
    9: "plateau",
    10: "hills",
    11: "plateau",
    12: "cliff",
    13: "hills",
    14: "valley",
    15: "plain",
}

regions = {terrain: [] for terrain in classes.values()}

with rasterio.open(file_path) as src:
    terrain_band = src.read(1)
    metadata = src.meta.copy()
    transform = src.transform
    print(terrain_band[:5])

print(metadata)

# Convert the terrain band into a NumPy array for analysis
terrain_data = np.array(terrain_band)
# print(terrain_data)

# transformer = Transformer.from_crs(metadata.crs, "EPSG:4326", always_xy=True)
# Convert pixel coordinates to bounding boxes
for class_id, class_name in classes.items():

    rows, cols = np.where(terrain_band)
    X, Y = rasterio.transform.xy(transform, rows, cols, offset="ul")
    # X_max, Y_max = rasterio.transform.xy(transform, rows + 1, cols + 1, offset="ul")
    visited = np.zeros((len(rows), len(cols)))

    for i in range(len(rows)):
        for j in range(len(cols)):
            




print(classes[int(terrain_band[0,0])]) 


for label, box in regions.items():
    gdf = gpd.GeoDataFrame(geometry=box, crs="EPSG:4326")
    gdf.to_file(f"{label}.geojson", driver="GeoJSON")
    print(f"Extracted {len(regions)} regions for terrain class {label}.")

    


    

    

