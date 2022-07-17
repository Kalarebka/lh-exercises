# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)
import csv

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.mode = "r"
        self.csv_reader = None
        
    def __enter__(self):
        file = open(self.filename, self.mode)
        self.csv_reader = csv.reader(self.file, delimiter=",")
        return self.csv_reader


    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()


with FileHandler("trees.csv", "r") as f:
    for i in range(10):
        print(f.get_line())

