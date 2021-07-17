'''

Sreenivas Bhattiprolu
https://www.youtube.com/watch?v=Wka_XhcZAcQ
https://github.com/bnsreenu/python_for_microscopists/blob/master/106_image_filters_using_fourier_transform_DFT.py
'''

import cv2
import numpy as np
import glob
import ImageTable

usr1 ="rockman"
usr2 ="gilfm"
 
BASE_FOLDER = 'C:/Users/'+usr1 +'/Pictures/Saved Pictures/'

img_name = "lena.png"
path = BASE_FOLDER + img_name
print (path)

img1 = cv2.imread(path) # load an image
img  = cv2.imread(path, 0)

#Output is a 2D complex array. 1st channel real and 2nd imaginary
#For fft in opencv input image needs to be converted to float32
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

#Rearranges a Fourier transform X by shifting the zero-frequency
#component to the center of the array.
#Otherwise it starts at the tope left corenr of the image (array)
dft_shift = np.fft.fftshift(dft)
#print(dft_shift.shape)
#Magnitude of the function is 20.log(abs(f))
#For values that are 0 we may end up with indeterminate values for log.
#So we can add 1 to the array to avoid seeing a warning.
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))


# Circular HPF mask, center circle is 0, remaining all ones
#Can be used for edge detection because low frequencies at center are blocked
#and only high frequencies are allowed. Edges are high frequency components.
#Amplifies noise.

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.ones((rows, cols, 2), np.uint8)
r = 80
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 0
# Circular LPF mask, center circle is 1, remaining all zeros
# Only allows low frequency components - smooth regions
#Can smooth out noise but blurs edges.
#

# apply mask and inverse DFT
fshift = dft_shift * mask

fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

cv2.imshow("original",img1)
scale = 0.6
img_array = ([img1, magnitude_spectrum ], [fshift_mask_mag , img_back])
imgStack = ImageTable.stackImages(scale, img_array)

cv2.imshow("table", img_back)
cv2.imshow("fshift_mask_mag",fshift_mask_mag )





cv2.waitKey(0)
cv2.destroyAllWindows()