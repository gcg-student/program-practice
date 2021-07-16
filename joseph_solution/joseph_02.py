from logging import exception
import tkinter as tk
from tkinter import filedialog
import csv, re, xlrd, zipfile
import unittest

class StrategyFactory(object):

    file_read_strategy = {}
    @classmethod
    def get_strategy_by_type(cls, type):

        return cls.file_read_strategy.get(type)

    @classmethod
    def register(cls, strategy_type, strategy):
        if strategy_type == "":
            Exception("strategyType can't be null")
        cls.file_read_strategy[strategy_type] = strategy

class Student(object):
    def __init__(self, id, name, sex, age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

    def __repr__(self):
        return self.id + self.name + self.sex + self.age

class ReaderParent(object):
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return self.path

class CsvReader(ReaderParent):
    def __init__(self):
        ReaderParent.__init__(self, path)

    def reader(self):
        file = open(self.path, 'r')
        file_content = list(csv.reader(file))

        student_list = []
        for file_line in file_content:
            line_division = re.findall("\S* ", file_line[0])
            student = Student(line_division[0], line_division[1], 
                line_division[2], line_division[3])
            #print(line_division)
            student_list.append(student)
        
        return student_list

    def set_strategy_type(self):
        return ".csv"

    def add_strategy_to_factory(self):
        StrategyFactory.register(self.set_strategy_type(), CsvReader)

class ExcelReader(ReaderParent):
    
    def __init__(self):
        ReaderParent.__init__(self, path)

    def reader(self):
        data = xlrd.open_workbook(self.path)
        sheet = data.sheet_by_name('Sheet1')

        student_list = []
        for num in range(sheet.nrows):
            student_data = sheet.row_values(num)
            student_object = Student(
                student_data[0], student_data[1], 
                student_data[2], student_data[3])

            student_list.append(student_object)

        return student_list

    def set_strategy_type(self):
        return ".xlsx"

    def add_strategy_to_factory(self):
        StrategyFactory.register(self.set_strategy_type(), ExcelReader)

class ZipReader(ReaderParent):
    
    def __init__(self):
        ReaderParent.__init__(self, path)

    def reader(self):
        file_zip = zipfile.ZipFile(self.path, 'r')
        file_zip = file_zip.read(file_zip.namelist()[0]).decode('gbk')

        student_list = []
        for line in file_zip.split("\n"):
            line_division = re.findall('\S* ', line)
            student = Student(line_division[0], line_division[1], 
                line_division[2], line_division[3])
                
            student_list.append(student)

        return student_list

    def set_strategy_type(self):
        return ".zip"

    def add_strategy_to_factory(self):
        StrategyFactory.register(self.set_strategy_type(), ZipReader)

class JosephusRing():
    def __init__(self, container, total, delete):
        assert(len(container) > 0)

        self.container = container
        self.total = total
        self.delete = delete

    def solve_josephus_problem(self):
        list_finally = []
        num_temporary = 0

        if self.total <= 0 or self.delete <= 0:
            return -1

        print("学生总量为：", self.total)
        while True:
            if len(self.container) > 1:
                num_temporary = ((self.delete 
                                - 1 
                                + num_temporary) 
                                % len(self.container))
                print("被淘汰的学生信息：" + str(self.container[num_temporary].__dict__))
                list_finally.append(self.container[num_temporary])
                del self.container[num_temporary]
            else:
                break;
        print("最后留下的学生信息：" + str(self.container[0].__dict__))

        return self.container[0]

def init_all_strategy():
    CsvReader().add_strategy_to_factory()
    ZipReader().add_strategy_to_factory()
    ExcelReader().add_strategy_to_factory()

def file_interface(file_path):
    ReaderParent(file_path)
    print("文件地址：", file_path)
    type = re.findall("\.\S*$", file_path)
    print("文件类型：", type)
    init_all_strategy()
    strategy = StrategyFactory().get_strategy_by_type(type[0])
    print("策略类型：", strategy)

    if not strategy:
        raise Exception("type invalied!")
    print(strategy().reader())
    
    return strategy().reader()

def get_file_path():
    windows = tk.Tk()
    windows.withdraw()

    path = filedialog.askopenfilename()

    return path

if __name__ == '__main__':
    path = get_file_path()
    file_data = file_interface(path)
    print("测试输出")
    JosephusRing(file_data, len(file_data), 3).solve_josephus_problem()
    #print(file_interface())
    #a.reader()
  
