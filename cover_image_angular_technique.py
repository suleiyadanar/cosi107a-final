import numpy as np
from PIL import Image

def embed_message(cover_image, message, stego_file):
    """
    Hide message into LSB of the pixels of the cover image
    """

    def binarize(msg): # convert message to binary string
        binary_data = ''.join(format(ord(char), '08b') for char in msg)
        return binary_data

    cover_image = Image.open(cover_image)  # read cover image
    cover_img_array = np.array(cover_image)

    cover_size = cover_img_array.shape[0] * cover_img_array.shape[1] * 3 # cover image size

    binarized_message = binarize(message)
    if cover_size < len(binarized_message): # check if cover image is big enough
        print("Cover image will be distorted after embedding")
        return

    cover_rotated = np.rot90(cover_img_array) # rotate image 90 degrees

    """
    Embed message in LSB of pixels with 3-3-2 RGB rule
    """
    msg_index = 0  # track bit index of message
    pixels = 0  # number of pixels used
    for i in range(cover_rotated.shape[0]): # row
        for j in range(cover_rotated.shape[1]): # column
            if msg_index < len(binarized_message):
                red, green, blue = cover_rotated[i, j] # RGB values of a pixel
                # Red: 3LSBs
                red_binary = format(red, '08b') # convert to binary
                red_embedded = red_binary[:-3] + binarized_message[msg_index:msg_index+3]
                cover_rotated[i, j][0] = int(red_embedded, 2)   # convert binary to int
                msg_index += 3
                # Green: 3LSBs
                green_binary = format(green, '08b')
                green_embedded = green_binary[:-3] + binarized_message[msg_index:msg_index+3]
                cover_rotated[i, j][1] = int(green_embedded, 2)
                msg_index += 3
                # Blue: 2LSBs
                blue_binary = format(blue, '08b')
                blue_embedded = blue_binary[:-2] + binarized_message[msg_index:msg_index+2]
                cover_rotated[i, j][2] = int(blue_embedded, 2)
                msg_index += 2

                pixels += 1


    last_pixel = cover_rotated[-1, -1] # last pixel to store num of pixels used
    cover_rotated[-1, -1][0] = (last_pixel[0] & ~1) | (pixels & 1) # red
    cover_rotated[-1, -1][1] = (last_pixel[1] & ~1) | ((pixels >> 1) & 1) # green
    cover_rotated[-1, -1][2] = (last_pixel[2] & ~3) | ((pixels >> 2) & 3) # blue

    cover_rotated = np.rot90(cover_rotated, k=-1) # rotate back to original

    cover_rotated = cover_rotated.astype(np.uint8)     # 24-bit color stego image
    stego_image = Image.fromarray(cover_rotated, mode='RGB')
    stego_image.save(stego_file, format='PNG')

    return stego_file

def extract_message(stego_image_path):
    """
    Extract hidden message from cover image
    """
    stego_image = Image.open(stego_image_path) # read stego image
    stego_array = np.array(stego_image)

    transformed_stego_array = np.rot90(stego_array) # rotate 90 degrees

    last_pixel = transformed_stego_array[-1, -1]
    embedded_pixels = (last_pixel[0] & 1) | ((last_pixel[1] & 1) << 1) | ((last_pixel[2] & 3) << 2)

    """
    Extract the embedded message using 3-3-2 rule
    """
    extracted_data = ''
    secret_index = 0
    for i in range(transformed_stego_array.shape[0]):   # row
        for j in range(transformed_stego_array.shape[1]): # column
            if secret_index < embedded_pixels * 8:
                red, green, blue = transformed_stego_array[i, j] # RGB values of a pixel
                extracted_data += format(red, '08b')[-3:] # 3 LSBs of red
                extracted_data += format(green, '08b')[-3:] # 3 LSBs of green
                extracted_data += format(blue, '08b')[-2:] # 3 LSBs of blue

                secret_index += 8
            else:
                break

    secret_message = '' # extracted message
    for i in range(0, len(extracted_data), 8): # convert back to ascii text
        secret_message += chr(int(extracted_data[i:i+8], 2))

    return secret_message

# example
if __name__ == "__main__":
    # embedding
    message = "CoverImage"
    embed_message("assets/cover/woman.jpeg", message, "assets/stego_results/cover_woman.jpeg")

    # extracting
    extracted_data = extract_message("assets/stego_results/cover_woman.jpeg")
    print("Extracted secret data:", extracted_data)




