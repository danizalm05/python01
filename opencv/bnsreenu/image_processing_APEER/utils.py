# utils.py
import cv2
import numpy as np
from scipy.fft import fft2, fftshift, ifft2
from scipy.ndimage import gaussian_filter

def apply_fourier_transform(image):
    """
    Apply Fourier Transform to the image and return the magnitude spectrum.
    """
    # Fourier Transform
    f_transform = fft2(image)
    f_shift = fftshift(f_transform)
    magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)  # Use log scale for better visualization
    return magnitude_spectrum

def apply_filter(image, filter_type='gaussian', sigma=1):
    """
    Apply filtering to the image as a signal processing step.
    """
    if filter_type == 'gaussian':
        return gaussian_filter(image, sigma=sigma)
    elif filter_type == 'median':
        return cv2.medianBlur(image, 5)
    elif filter_type == 'sobel':
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        return cv2.magnitude(sobelx, sobely)
    else:
        print("Unsupported filter type.")
        return image