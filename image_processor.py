#!/usr/bin/env python
# coding: utf-8

import os, argparse, math
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

def get_name_and_extention(file):
    full_path, extention = os.path.splitext(file)
    f_name = full_path.split('/')
    file_name = f_name[-1]
    print('Processing: {}'.format(file))
    return file_name, extention

def change_to_grayscale(file):
    # get file name and extention
    file_name, extention = get_name_and_extention(file)
    
    # open image, convert to grayscale and save
    print('Changing to greyscale')
    img = Image.open(file) 
    gray_img = ImageOps.grayscale(img)
    new_img_name = '{}-bw{}'.format(file_name, extention)
    new_img = gray_img.save(new_img_name)
    print('File saved in grayscale')
    return True

def compress_image(file, quality=None):
    # get file name and extention
    file_name, extention = get_name_and_extention(file)

    # open image, get original size, compress and save
    print('Compressing  image: {}'. format(file))
    original_size = os.path.getsize(file)
    img = Image.open(file)
    new_img_name = '{}-compressed{}'.format(file_name, extention)
    new_img = img.save(new_img_name,optimize=True, quality=quality)

    # get new size, calculate percentage compression
    final_size = os.path.getsize(new_img_name)
    saved_percentage = ((original_size - final_size)/original_size) * 100
    print('Compressed by: {}% '.format(math.ceil(saved_percentage)))
    return True

def main(args):
    action = args.action
    files = r"{}".format(args.file)
    quality = args.quality
    
    # check if path exists if not raise exception
    exists = os.path.exists(files)
    if not exists:
        raise Exception('Path entered does not exist')
    
    # check if file is image else raise exception
    if not valid_image(files):
        raise Exception('File entered is not a supported file type')
        
    if action == 'bw':
        img = change_to_grayscale(files)
    if action == 'rd':
        img = compress_image(file=files, quality=quality)
    
    
if __name__ == '__main__':
    # parse arguements
    parser = argparse.ArgumentParser(
        description='Process images to various states.'
    )
    parser.add_argument(
        '-a', '--action',
        choices=['bw',  'rd', 'other'],
        help='Action to be perfomed by script',
        required=True
    )
    parser.add_argument(
        '-f', '--file',
        help='File to be processed',
        required=True,
        type=str
    )
    parser.add_argument(
        '-q', '--quality',
        help='Quality of image, for compression(90 default)',
        required=False,
        type=int
    )
    args = parser.parse_args()
    main(args)
