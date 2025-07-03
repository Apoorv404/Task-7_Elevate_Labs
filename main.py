from PIL import Image
import os

# image = Image.open("images/mango_dry_leaf.jpg")
# image = image.resize((800, 600))  # Resize the image to 800x600 pixels
# image.save("resized_images/resized_image.jpg")  # Save the resized image
# print("Image resized and saved successfully.")


new_size = (800, 600)
source_folder = "./images"
destination_folder = "./resized_images"

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Create new filename
        name, ext = os.path.splitext(filename)
        save_path = os.path.join(destination_folder, f"{name}_resized{ext}")

        # Save the resized image
        resized_img.save(save_path)
        print(f"Saved: {f"{name}_resized{ext}"}")

print("All images resized and saved successfully.")
