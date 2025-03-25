import requests
import geojson
import os
from geotiff_to_png import geotiff_to_png

regions = [
    "mountains",
    "valleys",
    "plains",
    "hills",
    "plateaus",
    "highlands",
    "cliffs",
]
# OpenTopography API endpoint and key
key = os.getenv("API_KEY")
url = "https://portal.opentopography.org/API/globaldem"
api_key = key


# Loop through each region and download the DEM
for class_name in regions:
    print(class_name)
    with open(f"Kaggle Output/{class_name}.geojson") as file:
        geojs = geojson.load(file)
    output_folder = f"./{class_name}/"
    print("output folder variable created")
    idx=-1

    for region in geojs["features"]:
        idx+=1
        bounds = region["geometry"]["coordinates"][0]  # (minx, miny, maxx, maxy)
        params = {
            "demtype": "SRTMGL3",  # DEM type
            "south": bounds[2][1],
            "north": bounds[0][1],
            "west": bounds[2][0],
            "east": bounds[0][0],
            "outputFormat": "GTiff",
            "API_Key": api_key
        }

        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # File name for saving
        filename = f"{class_name}_{idx}"
        file_path = os.path.join(output_folder, filename)

        response = requests.get(url, params=params)
        print("api get request completed")

        if response.status_code == 200:
            
            geotiff_to_png(response.content, output_folder, filename)
            print(f"Downloaded heightmap for region {idx}.")
        else:
            print(f"Failed to download region {idx}: {response.status_code}\n{response.content}")
        
        # print(f"Bounding box: {bounds[0]}, {bounds[1]}, {bounds[2]}, {bounds[3]}")

