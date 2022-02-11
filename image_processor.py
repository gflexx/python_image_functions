#!/usr/bin/env python
# coding: utf-8

import os, argparse
from PIL import Image, ImageOps

def valid_image(file):
    # check if file is an image
    name, extention = os.path.splitext(file)
    images = {'.jpg', '.png', '.jpeg', '.tiff', '.bmp', '.gif'}
    
    # check if file extention is accepted
    if extention.lower() in images:
        return True
    else:
        return False

def change_to_grayscale(file):
    # get file name and extention
    name, extention = os.path.splitext(file)
    f_name = name.split('/')
    fl_name = f_name[-1]
    print('Processing: {}'.format(fl_name))
    
    # open image, convert to grayscale and save
    img = Image.open(file) 
    gray_img = ImageOps.grayscale(img)
    new_img_name = '{}-bw{}'.format(fl_name, extention)
    new_img = gray_img.save(new_img_name)
    print('File {} saved in grayscale'.format(new_img_name))
    
    return new_img 

def main(args):
    action = args.action
    files = r"{}".format(args.file)
    
    # check if path exists if not raise exception
    exists = os.path.exists(files)
    if not exists:
        raise Exception('Path entered does not exist')
    
    # check if file is image else raise exception
    if not valid_image(files):
        raise Exception('File entered is not a supported file type')
        
    if action == 'bw':
        img = change_to_grayscale(files)
    
    
if __name__ == '__main__':
    # parse arguements
    parser = argparse.ArgumentParser(
        description='Process images to various states.'
    )
    parser.add_argument(
        '-a', '--action',
        choices=['bw', 'other'],
        help='Action to be perfomed by script',
        required=True
    )
    parser.add_argument(
        '-f', '--file',
        help='File to be processed',
        required=True,
        type=str
    )
    args = parser.parse_args()
    main(args)
