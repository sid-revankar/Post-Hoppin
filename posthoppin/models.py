import os
import shutil
from pathlib import Path

class File_Handling:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_path(self):
        f_path = Path(self.filepath)
        return f_path

    def dir_sort(self, f_path):
        main_dir = []
        self.f_path = f_path

        folder = os.scandir(self.f_path)
        for entry in folder:
            if entry.is_dir():  # and not entry.is_file():
                main_dir.append(entry)
        return main_dir

    def passTree(self, list_dir):
        self.list_dir = list_dir
        for key in self.list_dir:
            src = r"{}".format(Path(key))
            cur_dir = os.path.basename(src)
            dest = r"/home/fastaf/cli project/posthoppin/.config/"
            if os.path.exists(dest):
                pass
            else:
                shutil.copytree(src, dest + cur_dir)

