#!/usr/bin/env python

__author__ = "gomgum  pokla"
__license__ = " Microscopists"
'''
Pillow (PIL) is an image manipulation and processing library 
https://www.youtube.com/watch?v=uDNqNv2N-pY
https://github.com/bnsreenu/python_for_microscopists/blob/master/018-image_processing_in_pillow.py
https://pillow.readthedocs.io/en/stable/reference/Image.html
 '''


from PIL import Image

BASE_FOLDER = 'C:/Users/gilfm/Pictures/Saved Pictures/'
img_name = "p1.jpg"
path = BASE_FOLDER + img_name
print(path)

img = Image.open(path) #Not a numpy array
print(type(img))
# show Images on external default viewer. This can be paint or photo viewer on Windows
#img.show()

print(img.format)# prints format of image
print(img.mode) # prints mode of image RGB or CMYK
print(img. size)  #prints the size of image (wodth, height)

# Resize images
small_img = img.resize((200, 300))
small_img.save(BASE_FOLDER+"p1_small.jpg")  #squished image


# resize() method resizes images to exact value whether it makes sense or not.
#aspect ratio is not maintained so images are squished.
#if you want to keep the aspect ration then use thumbnai() method

img.thumbnail((200, 200))
img.save(BASE_FOLDER+"thumbnail-p1_small.jpg")

print("img.size",img.size)

#Cropping images

img = Image.open( BASE_FOLDER +"p2.jpg")
cropped_img = img.crop((0, 0, 300, 300))  #crops from (0,0) to (300,300)
cropped_img.save(BASE_FOLDER+"p2cropped_img.jpg")

# Paste image on another image
#this involves copying original image and pasting a second image on it

img1 = Image.open(BASE_FOLDER+"p1.jpg")
print(img1.size)
img2 = Image.open(BASE_FOLDER+"p2.jpg")
print(img2.size)
img2.thumbnail((200, 200))  #Resize in case the image is very large.
print(img2.size)

img1_copy = img1.copy()   #Create a copy of the large image
img1_copy.paste(img2, (50, 50))  #Paset the smaller imager image at specified location
img1_copy.save(BASE_FOLDER+"pasted_image.jpg")

# Rotating images

img = Image.open(BASE_FOLDER+"p3.jpg")

img_90_rot = img.rotate(90)
img_90_rot.save(BASE_FOLDER+"rotated90.jpg")  #keeps original aspect ratio and dimensions

img_45_rot = img.rotate(45)
img_45_rot.save(BASE_FOLDER+" rotated45.jpg")  #keeps original aspect ratio and dimensions

img_45_rot = img.rotate(45, expand=True)  #Dimensions are expanded to fir the entire image
img_45_rot.save(BASE_FOLDER+"expandedrotated45.jpg")

# Flipping or transposing images


img = Image.open(BASE_FOLDER+"p3.jpg")

img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save(BASE_FOLDER+"lrp3.jpg")

img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipTB.save(BASE_FOLDER+"TBp3.jpg")

# Color transforms, convert images between L (greyscale), RGB and CMYK


img = Image.open(BASE_FOLDER+"p4.jpg")
grey_img = img.convert('L')  #L is for grey scale
grey_img.save(BASE_FOLDER+"grey_img.jpg")

# Many other tasks can be performed. Here is full documentation.
