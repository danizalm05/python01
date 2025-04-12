
'''
VGG-Image-Annotator: Parsing the JSON file
The code in this repository is used to parse the JSON file generated 
after annotating the images through the VGG Image Annotator tool designed by
 Visual Geometry Group.

https://towardsdatascience.com/generating-image-segmentation-masks-the-easy-way-dd4d3656dbd1/?gi=21e4686bceed


https://www.youtube.com/watch?v=G-JYJaQmhwM
https://github.com/nikhilroxtomar/VGG-Image-Annotator-Process-JSON-file/blob/main/process_data.py
https://jsonformatter.org/json-viewer

'''


import os
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
import json
 

""" Creating a directory """
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        


if __name__ == "__main__":
    """ Dataset path """
    dataset_path = "dataset"
    dataset = glob(os.path.join(dataset_path, "*"))
    print(dataset)
    """
    glob is used to return all file paths names that match a 
    specific pattern. 
    
    """        