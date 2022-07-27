# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)

import atexit

# class FileHandler:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(self.filename, "r")
#         self.line_generator = self.file.readlines()

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         self.file.close()

#     def get_line(self):
#         return self.file.readline()

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "r")
        atexit.register(self.file.close)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

    def get_line(self):
        return self.file.readline()

    def __del__(self):
        atexit.unregister(self.file.close)
        self.file.close()

# Assumptions:
# - context manager == has to open the file and close it after it's finished (_del_? atexit?)
# - but without using "with" statement?
# - supposed to use a generator but the file object is already a generator


# Using 'with' statement
with FileHandler("trees.csv") as f:
    for i in range(10):
        print(f.get_line())

# Using a variable
handler = FileHandler("trees.csv")
for i in range(20):
    print(handler.get_line())
