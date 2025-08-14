import os
from PIL import Image


def batch_resize_images(folder_path, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all image files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                # Resize image to the specified size (width, height)
                resized_img = img.resize(size)
                # Save the resized image to the output folder
                resized_img.save(os.path.join(output_folder, filename))

    print(f"All images resized to {size} and saved to {output_folder}.")

batch_resize_images('C:/Users/chitt/OneDrive/Pictures/Screenshots', 'C:/Users/chitt/Pictures/output_images', (800, 600))
