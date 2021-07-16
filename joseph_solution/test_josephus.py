from logging import exception
import unittest
import joseph_02 as joseph

class StrategyFactoryTest(unittest.TestCase):
    def setUp(self):
        self.strategy = joseph.StrategyFactory()

    def test_strategy(self):
        try:
            self.assertIsNone(self.strategy)
        except Exception as e:
            print("Strategy is not exist!")
        
class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = joseph.Student("1", "2", "3", "4")

    def test_student(self):
        try:
            self.assertIsNone(self.strategy)
        except Exception as e:
            print("return content error!")

class ReaderParentTest(unittest.TestCase):
    def setUp(self):
        self.path = "F:\python\python - program\joseph-01\student_info.csv"
        self.reader = joseph.ReaderParent(self.path)

    def test_reader(self):
        try:
            self.assertEqual(self.reader, self.path)
        except Exception as e:
            print("path is not exist!")
       
class CsvReaderTest(unittest.TestCase):
    def setUp(self):
        self.csv_reader = joseph.CsvReader().reader()

    def test_csv_reader(self):
        for student in self.csv_reader:
            self.assertIsNone(student)
            self.assertEqual(len(student), "4")

class ExcelReaderTest(unittest.TestCase):
    def setUp(self):
        self.excel_reader = joseph.ExcelReader().reader()

    def test_excel_reader(self):
        for student in self.excel_reader:
            self.assertIsNone(student)
            self.assertEqual(len(student), "4")

class ZipReaderTest(unittest.TestCase):
    def setUp(self):
        self.zip_reader = joseph.ZipReader().reader()

    def test_zip_reader(self):
        for student in self.zip_reader:
            self.assertIsNone(student)
            self.assertEqual(len(student), "4")

class JosephusRingTest(unittest.TestCase):
    def setUp(self):
        list = ["1", "2", "3"]
        self.josephus = joseph.JosephusRing(list, len(list), 2)

    def test_solve_josephus(self):
        try:
            self.assertEqual(self.josephus.solve_josephus_problem(), "3")
        except Exception as e:
            print("josephus ring operation error!")

if __name__ == '__main__':
      unittest.main(verbosity=2)
