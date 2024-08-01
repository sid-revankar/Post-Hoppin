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
            root_dir.append(entry)
        return root_dir

    def putFiles(self, root_dir):
        self.root_dir = root_dir
        dest = Path('G:/Projects/Post-Hoppin/posthoppin/config')
        dest.mkdir(exist_ok=True)
        for key in self.root_dir:
            # src = Path(key)
            if os.path.isdir(key):
                if key.name == ".git":
                    print(".git already exists!")
                else:
                    shutil.copytree(key, dest.joinpath(key.name), dirs_exist_ok=True)
            else:
                shutil.copyfile(key, dest)