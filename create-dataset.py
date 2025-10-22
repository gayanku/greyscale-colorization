# pip install opencv-python

import os
import cv2

# Set the path to your image folder
input_folder = 'Samples_REF'
output_folder = 'OUTPUT'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

# Get list of image files
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]
image_files.sort()  # Optional: sort alphabetically

# Process each image
for idx, filename in enumerate(image_files, start=1):
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Skipping invalid image: {filename}")
        continue

    # Save color image
    color_name = f"C_{idx}.jpg"
    cv2.imwrite(os.path.join(output_folder, color_name), img)

    # Convert to grayscale and save
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_name = f"G_{idx}.jpg"
    cv2.imwrite(os.path.join(output_folder, gray_name), gray_img)

    print(f"Processed {filename} → {color_name}, {gray_name}")
