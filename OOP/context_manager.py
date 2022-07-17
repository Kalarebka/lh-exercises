# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()


with FileHandler("trees.csv") as f:
    for i in range(10):
        print(f.readline())

