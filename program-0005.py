import tkinter as tk
from tkinter import filedialog
from os import listdir
import os,numpy
import re
import cv2 as cv

folder_path = ""
subdirectory_name = "save the picture"

def get_all_file_path():
    windows = tk.Tk()
    windows.withdraw()

    folder_path = filedialog.askdirectory()
    all_file_path = listdir(folder_path)
    path_names = [os.path.join(folder_path, filename) for filename in all_file_path]
    check_file_path(path_names)
    #print(pathnames)
    #os.mkdir(folder_path + subdirectory_name)

def check_file_path(all_file_path):
    for file in all_file_path:
        if re.findall('.jpg$', file) is None:
             all_file_path.remove(file)

    adjust_picture_size(all_file_path)

def adjust_picture_size(all_file_path):
    os.mkdir()
    for file in all_file_path:
        image = cv.imread(file)
        image = cv.resize(image, (1136, 640), )
        numpy.save(file, image)

if __name__ == '__main__':
    get_all_file_path()
