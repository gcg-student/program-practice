import re
import tkinter as tk
from tkinter import filedialog
import enchant

word_list = enchant.Dict("en_US")
word_correct = []

def get_file_path():
    windows = tk.Tk()
    windows.withdraw()
    filePath = filedialog.askopenfilename()

    file = open(filePath, 'r')
    text = file.read()
    statistic_word(text)
    return text

def check_the_word(words):
    for element in words:
        if word_list.check(element) is not False:
            word_correct.append(words)
    print(word_correct)
        
def statistic_word(text):
    words = re.findall('[a-zA-Z]+', text)
    check_the_word(words)
    return words

if __name__ == '__main__':
    get_file_path()
