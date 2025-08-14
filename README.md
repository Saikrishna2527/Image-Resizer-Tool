Import Libraries: The script imports the os module to interact with the file system and the Image class from Pillow to work with images.

Function Definition: A function batch_resize_images is defined with parameters:

folder_path: Path to the folder containing the input images.

output_folder: Path where resized images will be saved.

size: A tuple (width, height) specifying the target dimensions for resizing.

Create Output Folder: Inside the function, it checks if the specified output folder exists. If not, it creates the folder using os.makedirs. This ensures resized images have a place to be saved.

Iterate Over Images: The function lists all files in the input folder using os.listdir. It then loops through each filename.

Filter Images by Extension: For each file, it checks if the file extension matches common image types such as PNG, JPG, JPEG, BMP, GIF, or TIFF. This avoids processing non-image files.

Open and Resize Image: For each valid image, it opens the file with Image.open(), then resizes it to the target size using the resize() method.

Save Resized Image: The resized image is saved to the output folder with the same filename but now resized to the specified dimensions.

Completion Message: After processing all images, the script prints a message indicating that all images have been resized and saved successfully.
