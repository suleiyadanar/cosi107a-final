# Image and Audio Steganography

## COSI 107a: Final Project by Su Lei Yadanar

05/06/2024

This project delves into exploring the implementations of two LSB-based algorithms for image steganography: the Cover Image Angular Transformation Technique and the Contrast Stretching Technique. It also explores different image steganalysis techniques, as well as simple LSB audio steganography.

## 'assets' Folder
#### 'cover' Folder
Includes example cover images and audio files.

#### 'stego_image' Folder
Includes stego images and audio files that were generated using the project's Python scripts.

## Python Scripts
### Image Steganography
#### cover_image_angular_technique.py
- Cover Image Angular Rotation technique using LSB
#### contrast_stretching_technique.py
- Contrast Stretching technique using LSB
#### distortion_tests.py
- Peak-Signal-to-Noise Ratio (PSNR)
- Structural Similarity Index Measurement (SSIM)

### Image Steganalysis Techniques
#### hcf.py
- Histogram Characteristic Function (HCF)
#### rqp.py
- Raw Quick Pair (RQP)
#### rs.py
- Residual Steganalysis (RS)
### Audio Steganography
#### audio_compression.py
- Compression Ratio
- Bits Per Character (BPC)
#### audio_steganography.py
- Simple LSB to embed messages in audio files

### References
- Abu. (2013). An image dithering via TCHEBICHEF moment transform. Journal of Computer Science, 9(7), 811–820. https://doi.org/10.3844/jcssp.2013.811.820
- Baritha Begum, M., & Venkataramani, Y. (2012). LSB based audio steganography based on text compression. Procedia Engineering, 30, 703–710. https://doi.org/10.1016/j.proeng.2012.01.917
- Chervyakov, N., Lyakhov, P., & Nagornov, N. (2020). Analysis of the quantization noise in discrete wavelet transform filters for 3D medical imaging. Applied Sciences, 10(4), 1223. https://doi.org/10.3390/app10041223
- Gnash (2017). File:24 bit.png. Wikimedia Commons. https://commons.wikimedia.org/wiki/Category:Images
- Marshall, D. (2001). 24-bit color image of parrots. Cardiff School of Computer Science and Informatics. https://users.cs.cf.ac.uk/dave/Multimedia/parrots.jpeg
- Molato, M. R., & Gerardo, B. D. (2018). Cover image selection technique for secured LSB-based image steganography. Proceedings of the 2018 International Conference on Algorithms, Computing and Artificial Intelligence. https://doi.org/10.1145/3302425.3302456
- Nissar, A., & Mir, A. H. (2010). Classification of steganalysis techniques: A study. Digital Signal Processing, 20(6), 1758–1770. https://doi.org/10.1016/j.dsp.2010.02.003
- Rajput, G. G., & Chavan, R. (2017). A novel approach for image steganography based on LSB technique. Proceedings of the International Conference on Compute and Data Analysis. https://doi.org/10.1145/3093241.3093247
- Tasheva, A., Tasheva, Z., & Nakov, P. (2017). Image based steganography using modified LSB insertion method with contrast stretching. Proceedings of the 18th International Conference on Computer Systems and Technologies. https://doi.org/10.1145/3134302.3134325
