from typing import Sized
import cv2 as cv
import numpy
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import pygame

def main(image):
    image_PIL = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    font = ImageFont.truetype("e:\\vscode\\20090701\\NotoSansCJK-Black.otf", 60)
    myfont = pygame
    fontColor = (255, 0, 0)
    fontPostion = (200, 10)
    background = ImageDraw.Draw(image_PIL)

    background.text(fontPostion, u"6", font=font, fill=fontColor)
    img_OpenCV = cv.cvtColor(numpy.asarray(image_PIL), cv.COLOR_RGB2BGR)
    cv.imshow("image_show", img_OpenCV)
    cv.waitKey()
    cv.destoryAllWindows()

def img_adjustment(image):
    image = cv.resize(image, (241, 261))
    
    return image

def obtain_file_path():
    root = tk.Tk()
    root.withdraw()

    FolderPath = filedialog.askdirectory()
    FilePath = filedialog.askopenfilename()

    return FilePath

if __name__ == '__main__':
    image = cv.imread(obtain_file_path())
    main(img_adjustment(image))
