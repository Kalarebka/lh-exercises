# Create Object FileCounter() that will count every folder and file in given path
# Function return nested dict with numbers of folders and files in tree
# There should be key result which will contain whole searched tree
# Use pathlib module and recursion

# Result dictionary should have this structure:
# {
#     files: x,
#     folders: y,
#     results: {}
# }

# not counting the given path in number of folders (only counting contents of the path)

from pathlib import Path


class FileCounter:
    def __init__(self, path: str):
        self.path = Path(path)
        self.num_files = 0
        self.num_folders = 0

    def _create_tree(self, path):
        files = []
        dirs = []
        for item in path.iterdir():
            if item.is_dir():
                self.num_folders += 1
                dirs.append(self._create_tree(item))
            else:
                self.num_files += 1
                files.append(item.name)
        return {"dir_name": path.name, "dirs": dirs, "files": files}

    def get_result(self):
        if not self.path.is_dir():
            return {}
        tree = self._create_tree(self.path)
        return {"files": self.num_files, "folders": self.num_folders, "results": tree}


counter = FileCounter("/home/ika/code/lh-exercises/OOP/test_file_counter")
print(counter.get_result())
