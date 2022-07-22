# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)


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


# with FileHandler("trees.csv") as f:
#     for i in range(10):
#         print(f.readline())


# Assumptions:
# - context manager == has to open the file and close it after it's finished
# - but without using "with" statement?
# - supposed to use a generator but the file object is already a generator
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "r")

    def get_line(self):
        return self.file.readline()

    def __del__(self):
        print("Closing file")
        self.file.close()


handler = FileHandler("trees.csv")
for i in range(20):
    print(handler.get_line())
