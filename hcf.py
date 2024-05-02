import numpy as np
from PIL import Image

def adjacency_histogram(image):
    """
    Calculates the adjacency histogram
    """
    adjacency_hist = np.zeros(256) # initialize
    width, height = image.size

    for i in range(width - 1):
        for j in range(height):
            diff = abs(image.getpixel((i, j)) - image.getpixel((i + 1, j))) # formula
            adjacency_hist[diff] += 1

    return adjacency_hist

def com(image):
    """
    Calculates the center of mass (COM)
    """
    total_mass = 0
    COM = 0
    width, height = image.size

    for i in range(width): # com formula
        for j in range(height):
            total_mass += image.getpixel((i, j))
            COM += (image.getpixel((i, j)) * (i * height + j + 1))  # pixel intensities weighted sum

    return COM / total_mass

def hcf(image_path, stego_img_path):
    cover_image = Image.open(image_path).convert("L") # grey cover
    stego_image = Image.open(stego_img_path).convert("L") # grey stego

    cover_adjacency_hist = adjacency_histogram(cover_image) # cover img
    stego_adjacency_hist = adjacency_histogram(stego_image) # stego img

    cover_com = com(cover_image) # cover com
    stego_com = com(stego_image) # stego com
    com_diff = abs(cover_com - stego_com) # com difference

    hist_diff = np.sum(np.abs(cover_adjacency_hist - stego_adjacency_hist)) # adj histogram diff

    threshold = 1000 # hcf formula
    if com_diff > threshold or hist_diff > threshold:
        print("LSB Detected!")
    else:
        print("No LSB Detected!")

# Example usage
hcf("assets/cover/parrots.jpeg", "assets/stego_results/stretch_parrots.jpeg")
