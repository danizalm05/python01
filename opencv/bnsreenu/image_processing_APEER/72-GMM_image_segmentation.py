"""
 72-GMM_image_segmentation.py
 -----------------------------------------------------
What is Gaussian Mixture Model (GMM) 
 Unsuprvised tecnich
 use it for image segmentation?
https://www.youtube.com/watch?v=__UcukytHuc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=74
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial72-GMM_image_segmentation.py

image:
   https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/images/BSE.tif

NOTE:
Both BIC and AIC are included as built in methods as part of Scikit-Learn's  GaussianMixture. 
Therefore we do not need to import any other libraries to compute these. 
The way you compute them (for example BIC) is by fitting a GMM model and then calling the method BIC. 
15:00
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt
#from scipy import ndimage
#from skimage import measure, color, io
import getpass
from pathlib import Path
import sys
import os
 

IMAGE_NAME =  'BSE.tif' # 'BSE.tif'   'Osteosarcoma_01_transl.tif'  '2.jpg'
USER = getpass.getuser()

if (os.name == "posix"):  #this is a linux  system 
    BASE_FOLDER = "/home/"+USER +'/Pictures/'
    print(BASE_FOLDER)
else: #this is a windows  system 
    BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   
img = cv2.imread(IMAGE)#Gray image
 

plt.imshow(img)
#06:00

img2 = img.reshape((-1,3))  #-1 reshape means, in this case MxN

from sklearn.mixture import GaussianMixture as GMM

numOfSegn = 4
#covariance choices, full, tied, diag, spherical
gmm_model = GMM(n_components = numOfSegn, covariance_type='tied').fit(img2) 
 #tied works better than full
gmm_labels = gmm_model.predict(img2)

#Put numbers back to original shape so we can reconstruct segmented image
original_shape = img.shape
segmented = gmm_labels.reshape(original_shape[0], original_shape[1])
plt.imshow(segmented)


##############################################################
#        How to know the best number of components?
#Using Bayesian information criterion (BIC) to find the best number of components


n = 4
gmm_model = GMM(n, covariance_type='tied').fit(img2)
#The above line generates GMM model for n=2
#Now let us call the bic method (or aic if you want).

bic_value = gmm_model.bic(img2)  #Remember to call the same model name from above)
print(bic_value)  #You should see bic for GMM model generated using n=2.
#Do this exercise for different n values and plot them to find the minimum.


#Now, to explain m.bic, here are the lines I used in the video. 
n_components = np.arange(1,10)
gmm_models = [GMM(n, covariance_type='tied').fit(img2) for n in n_components]
plt.plot(n_components, [m.bic(img2) for m in gmm_models], label='BIC')

plt.show()



def millions(x):
    print ('$%1.1fM' % (x * 1e-6))
    return '$%1.1fM' % (x * 1e-6)
fig, ax = plt.subplots()
print('millions = ',millions)
ax.fmt_ydata = millions
plt.plot(n_components, [m.bic(img2) for m in gmm_models], label='BIC')

# the n value   for th elbow is the better .

plt.show()




#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(4,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')
 
ax2 = fig.add_subplot(4,3,2)
ax2.imshow(segmented)#, cmap='gray')
ax2.title.set_text('segmented')
'''
ax3 = fig.add_subplot(4,3,3)
ax3.hist(image.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range')

ax4 = fig.add_subplot(4,3,4)
ax4.imshow(thresh, cmap='gray')
ax4.title.set_text('thresh')


ax5 = fig.add_subplot(4,3,5)
ax5.imshow(opening1)#,cmap='gray')
ax5.title.set_text('opening1')



ax6 = fig.add_subplot(4,3,6)
ax6.imshow(opening2)#, cmap='gray')
ax6.title.set_text('opening2')

ax7 = fig.add_subplot(4,3,7)
ax7.imshow(sure_bg, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(4,3,8)
ax8.imshow( sure_fg , cmap='gray')
ax8.title.set_text(' sure_fg ')


ax9 = fig.add_subplot(4,3,9)
ax9.imshow(unknown, cmap='gray')
ax9.title.set_text('unknown')

#
ax10 = fig.add_subplot(4,3,10)
ax10.imshow(markers)#, cmap='gray')
ax10.title.set_text('markers')

 

ax11 = fig.add_subplot(4,3,11)
ax11.imshow(markers10,cmap='gray')
ax11.title.set_text('markers10')

 

ax12 = fig.add_subplot(4,3,12)
ax12.imshow(img2,cmap='gray')
ax12.title.set_text('labels are painted over the image.')

'''
plt.show()
 