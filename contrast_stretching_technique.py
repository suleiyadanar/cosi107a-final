from PIL import Image
import numpy as np

def contrast_stretching(image, new_max):
    """
    contrast stretching formula as proposed in the paper
    """
    img_array = np.array(image)
    min_intensity = np.min(img_array)
    max_intensity = np.max(img_array)

    # formula
    stretched_image = (((img_array - min_intensity) / (max_intensity - min_intensity)) * (new_max - min_intensity)) + min_intensity

    stretched_image = Image.fromarray(stretched_image.astype(np.uint8))
    return stretched_image

def contrast_compression(image, new_max):
    """
    contrast compression formula as proposed in the paper
    """
    img_array = np.array(image)
    min_intensity = np.min(img_array)
    max_intensity = np.max(img_array)

    # formula
    compressed_image = (((img_array - min_intensity) / (max_intensity - min_intensity)) * (new_max - min_intensity)) + min_intensity

    compressed_image = Image.fromarray(compressed_image.astype(np.uint8))
    return compressed_image

def embed_message(image, text):
    """
    Hide message in the LSB of pixels
    """
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    text_index = 0

    for i in range(image.height):
        for j in range(image.width):
            if text_index < len(binary_message):
                pixel = list(image.getpixel((j, i)))
                pixel[-1] = int(binary_message[text_index])
                image.putpixel((j, i), tuple(pixel))
                text_index += 1
            else:
                break

    return image

def extract_message(image, text_length):
    """
    Read message from the LSB of pixels
    """
    binary_message = ''

    for i in range(image.height):
        for j in range(image.width):
            pixel = image.getpixel((j, i))
            binary_message += str(pixel[-1])
            if len(binary_message) == text_length * 8:
                return ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return ''

def stego_encoding(cover_image, input_text, new_max):
    cover_image_compressed = contrast_compression(cover_image.copy(), new_max) # compress
    stego_image = embed_message(cover_image_compressed.copy(), input_text) # embed
    stego_image = contrast_stretching(stego_image.copy(), new_max) # stretch
    return stego_image

def stego_decoding(stego_image, text_length, new_max):
    stego_image_compressed = contrast_compression(stego_image.copy(), new_max) # compress
    output_message = extract_message(stego_image_compressed.copy(), text_length) # extract
    return output_message

# example
if __name__ == "__main__":
    cover_image = Image.open('assets/cover/burger.jpeg')  # Load cover image
    input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    new_max = 250  # new max value for compression

    # embedding
    stego_image = stego_encoding(cover_image, input_text, new_max)
    stego_image.save('assets/stego_results/stretch_burger.jpeg')  # Save stego image

    # extracting
    decoded_text = stego_decoding(stego_image, len(input_text), new_max)
    print("Decoded Text:", decoded_text)

