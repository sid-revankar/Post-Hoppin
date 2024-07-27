import os
import shutil
from pathlib import Path


class FileHandling:
    def __init__(self, path):
        self.path = path

    def getPath(self):
        f_path = Path(self.path)
        return f_path

    def getSubDir(self, f_path):
        root_dir = []
        self.f_path = f_path

        folders = os.scandir(self.f_path)
        for entry in folders:
            if entry.is_dir():
                root_dir.append(entry)
        return root_dir

    def putFiles(self, list_dir):
        self.list_dir = list_dir
        for key in self.list_dir:
            src = r"{}".format(Path(key))
            cur_dir = os.path.basename(src)
            dest = os.environ['HOME']
            if os.path.exists():
                pass
            else:
                shutil.copytree(src, dest + cur_dir)
