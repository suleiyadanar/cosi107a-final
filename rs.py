from PIL import Image
import numpy as np

def rs_steganalysis(image, block_size=8, threshold=0.1):
    """
    Reversible Skeleton (RS) steganalysis technique to detect stego images
    """
    img_array = np.array(image)

    if len(img_array.shape) == 3: # convert to grayscale in 2D
        img_array = np.mean(img_array, axis=2)

    height, width = img_array.shape
    regular = 0

    for i in range(0, height - block_size + 1, block_size): # block iteration
        for j in range(0, width - block_size + 1, block_size):
            block = img_array[i:i+block_size, j:j+block_size]
            block = block.astype(np.uint8) # convert to bit
            flipped_block = np.bitwise_xor(block, 1)  # do XOR
            flipped_block = flipped_block.astype(img_array.dtype) # convert to original

            noise_original = np.mean(np.abs(np.diff(block))) # noise in original image
            noise_flipped = np.mean(np.abs(np.diff(flipped_block))) # noise in flipped image

            if abs(noise_flipped - noise_original) > threshold:
                regular += 1 # classify regular or singular

    total_groups = ((height // block_size) * (width // block_size))
    regular_group = regular / total_groups # regular group

    return regular_group

# Example usage
if __name__ == "__main__":
    image = Image.open('assets/stego_results/stretch_parrots.jpeg')
    rs = rs_steganalysis(image)
    print("RS", rs)




