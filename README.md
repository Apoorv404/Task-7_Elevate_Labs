# Image Resizer Script

A simple Python script to batch resize images from a source directory to a fixed size. This project was created as part of Task 7 for the Elevate Labs Internship.

## Overview

This script automates the process of resizing all images within a specified source folder (`./images`) to a hardcoded dimension (800x600 pixels) and saves them into a destination folder (`./resized_images`).

**Note:** This script forces all images into the specified dimensions and does **not** maintain the original aspect ratio, which may cause distortion.

## Features

- Batch resizes all images in the `./images` directory.
- Supports multiple image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`).
- Saves resized images with a `_resized` suffix to the `./resized_images` directory.
- Automatically creates the destination directory if it doesn't exist.

## Requirements

- Python 3.x
- Pillow (PIL)

## Installation

1.  **Clone the repository or download the script.**
2.  **Install the required package:**
    ```bash
    pip install pillow
    ```

## Usage

1.  Create a folder named `images` in the same directory as the `main.py` script.
2.  Place all the images you want to resize into the `images` folder.
3.  Run the script from your terminal:
    ```bash
    python main.py
    ```
4.  The resized images will be created and saved in the `resized_images` folder.

## Configuration

To change the output dimensions, source folder, or destination folder, you must edit the following lines in `main.py`:

```python
# On line 11
new_size = (800, 600)

# On line 12
source_folder = "./images"

# On line 13
destination_folder = "./resized_images"
```
