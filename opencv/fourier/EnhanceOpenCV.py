 """
 Enhancements using Fourier Transform
 How to remove unnecessary objects or artifacts in images?

 https://medium.com/swlh/image-processing-with-python-fourier-transform-for-digital-images-bc918786e375
 """
 import os
 import getpass

 import numpy as np
 import matplotlib.pyplot as plt
 from skimage.io import imread, imshow
 from skimage.color import rgb2gray



 USER = getpass.getuser()
 IMAGE_NAME = 'lena.jpg' #'2.jpg'
 BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
 IMAGE = BASE_FOLDER + IMAGE_NAME

 print(IMAGE)
 path = BASE_FOLDER
 file_list = os.listdir(path)

 for (image) in os.listdir(path):  # iterate through each file to perform some action
     print(image)

 cargoship_rgb = imread(IMAGE)
 cargoship_gray = rgb2gray(cargoship_rgb)
 #plt.imshow(cargoship_gray, cmap='gray')
 #plt.title('org Grayscale')


 cargoship_fft = np.fft.fftshift(np.fft.fft2(cargoship_gray))
 cargoship_fft2 = cargoship_fft.copy()
 cargoship_fft2[0:243,  0: 648] = 1

 fft =np.log(abs(cargoship_fft))

 f, axarr = plt.subplots(2, 3, figsize=(15, 16))
 axarr[0,0].imshow(cargoship_rgb)

 axarr[0,0].set_title("Original")

 axarr[0,1].imshow(cargoship_gray, cmap='gray')
 axarr[0,1].set_title("gray")

 axarr[0,2].imshow(abs(np.fft.ifft2(cargoship_fft2)),  cmap='gray')
 axarr[0,2].axis('off')
 axarr[0,2].set_title("ifft2")

 axarr[1,0].imshow(np.log(abs(cargoship_fft)), cmap='gray')
 axarr[1,0].set_title("fft")


 axarr[1,1].imshow(abs(np.fft.ifft2(cargoship_fft)),  cmap='gray')
 axarr[1,1].axis('off')
 axarr[1,1].set_title("ifft2")

 axarr[1,2].imshow(np.log(abs(cargoship_fft2)), cmap='gray')
 axarr[1,2].set_title("ft2")
 plt.subplots_adjust(hspace=0.3)

 plt.show()