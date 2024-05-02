from PIL import Image
import numpy as np

def rqp(image):
    """
    Raw Quick Pair(RQP) steganalysis technique
    Calculates ratio of close pairs of colors to the total number of unique colors in the image
    """
    image_array = np.array(image)

    height, width, channels = image_array.shape
    flat_image = image_array.reshape(height * width, channels) # reshape to 2D array

    unique_colors, counts = np.unique(flat_image, axis=0, return_counts=True)

    rqp = 0 # number of close pairs
    for count in counts:
        if count >= 2:
            rqp += count * (count - 1) / 2

    num_unique_colors = len(unique_colors)
    ratio = rqp / num_unique_colors    # ratio of close pairs to total unique colors

    return ratio

# Example usage
if __name__ == "__main__":
    img = Image.open('assets/stego_results/stretch_woman.jpeg')
    ratio = rqp(img)
    print("Ratio of close pairs:", ratio)
