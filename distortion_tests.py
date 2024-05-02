import numpy as np
from PIL import Image

def mse(cover_image, stego_image):
    """
    Mean Square Error (MSE)
    """
    height, weight = cover_image.shape[1], cover_image.shape[0]
    mse = np.sum((cover_image - stego_image) ** 2) / (height * weight) # formula
    return mse

def psnr(mse):
    """
    Peak-Signal-to-Noise Ratio (PSNR)
    """
    psnr = 10 * np.log10((255 ** 2) / mse) # formula
    return psnr

def ssim(cover_img, stego_img, K1=0.01, K2=0.03, L=255):
    """
    Structural Similarity Index Measurement (SSIM)
    """
    cov = np.cov(cover_img.flatten(), stego_img.flatten()) # covariance
    mean_cover = np.mean(cover_img) # mean
    mean_stego = np.mean(stego_img)
    var_cover = np.var(cover_img) # variance
    var_stego = np.var(stego_img)
    covar = cov[0, 1]
    c1 = (K1 * L) ** 2
    c2 = (K2 * L) ** 2

    num = (2 * mean_cover * mean_stego + c1) * (2 * covar + c2) # formula numerator
    deno = (mean_cover ** 2 + mean_stego ** 2 + c1) * (var_cover + var_stego + c2) # formula denominator

    ssim_index = num / deno
    return ssim_index

# Example usage
if __name__ == "__main__":
    cover_image = Image.open("assets/cover/burger.jpeg")
    cover_array = np.array(cover_image)
    stego_image = Image.open("assets/stego_results/stretch_burger.jpeg")
    stego_array = np.array(stego_image)

    # PSNR
    mse = mse(cover_array, stego_array)
    print("MSE:", mse)
    psnr = psnr(mse)
    print("PSNR:", psnr, "dB")

    # SSIM
    ssim = ssim(cover_array, stego_array)
    print("SSIM:", ssim)

