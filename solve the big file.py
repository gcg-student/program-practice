import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import re

def get_file_path():
    windows = tk.Tk()
    windows.withdraw()

    FilePath = filedialog.askopenfilename()
    return FilePath

def read_file_by_line(file):
    while True:
        for line in range(10):
            text = file.readline(10)
            if not text:
                break;
            print(text, '-----', '\n')
        break;

def read_file_by_size(file):
    while True:
        for line in range(10):
            text = file.read(10)
            if not text:
                break;
            print(text, '-----', '\n')
        break;

def check_file_name(filePath):
    if re.search('.txt$', filePath) is not None:
        return filePath
    else:
        show_warning_box()
        return False

def show_warning_box():
    windows = tk.Tk()
    windows.withdraw()
    tkinter.messagebox.showerror(title = '错误提示框', message = '文件为非法类型')

if __name__ == '__main__':
    filepath = get_file_path()
    file = open(filepath, 'r')
    if check_file_name(filepath) is not False:
        read_file_by_size(file)
