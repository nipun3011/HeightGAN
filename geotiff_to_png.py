from PIL import Image
import numpy as np
import rasterio
import os
from io import BytesIO

def geotiff_to_png(file, output_folder, filename):
    """
    Convert all GeoTIFF files in a folder to PNG images.
    
    Args:
    - input_folder: Folder containing GeoTIFF files.
    - output_folder: Folder to save PNG files.
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Read the GeoTIFF file
    with rasterio.open(BytesIO(file)) as src:
        data = src.read(1)  # Read the first band
        data = (data - np.min(data)) / (np.max(data) - np.min(data)) * 255  # Normalize to 0-255
        data = data.astype(np.uint8)  # Convert to 8-bit

    # Convert to PNG and save
    png_path = os.path.join(output_folder, f"{filename}.png")
    img = Image.fromarray(data)
    img.save(png_path)
    print(f"Converted and saved: {png_path}")

