import os

def get_file_size(file_path):
    return os.path.getsize(file_path)  # in bytes

def compression_ratio(input_size, output_size):
    return output_size / input_size

def bpc(input_size, output_size):
    return (output_size / input_size) * 8

# Example usage
if __name__ == "__main__":
    input_file_path = "assets/cover/jolly.wav"  # Input audio file path
    output_file_path = "assets/stego_results/stego_jolly.wav"  # Output audio file path
    message_length = len("Hello, this is a secret message!!")  # Number of samples (length of the secret message)

    input_file_size = get_file_size(input_file_path)
    output_file_size = get_file_size(output_file_path)

    compression_ratio = compression_ratio(input_file_size, output_file_size)
    bpc = bpc(input_file_size, output_file_size, message_length)

    print("Compression ratio:", compression_ratio)
    print("Bits per character (BPC):", bpc)