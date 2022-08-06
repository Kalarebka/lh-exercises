# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)

import atexit

from os import path


class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "r")
        atexit.register(self.file.close)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        atexit.unregister(self.file.close)
        self.file.close()

    def get_line(self):
        return self.file.readline()

    def __del__(self):
        atexit.unregister(self.file.close)
        self.file.close()


directory = path.dirname(path.realpath(__file__))
file_path = path.join(directory, "trees.csv")

# Using 'with' statement
with FileHandler(file_path) as f:
    for i in range(10):
        print(f.get_line())

# # Using a variable
handler = FileHandler(file_path)
for i in range(20):
    print(handler.get_line())
