# Create object FileHandler, which will serve as context manager for csv files
# This manager should serve one line at a time on demand (use generator)


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def get_line(self):
        eof = False
        while not eof:
            line = self.file.readline()
            if line:
                yield line
            else:
                eof = True

    def __exit__(self):
        self.file.close()


with FileHandler("trees.csv", "r") as f:
    for i in range(10):
        print(f.get_line())

