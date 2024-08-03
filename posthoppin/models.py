import os
import shutil
from pathlib import Path
import config

# File Handling: takes path input to copy dotFiles into .config directory
class FileHandling:
    def __init__(self, path):
        self.path = path

    def getPath(self):
        f_path = Path(self.path)
        return f_path
    
    # list of directories
    def getSubDir(self, f_path):
        root_dir = []
        self.f_path = f_path
        folders = os.scandir(self.f_path)
        for entry in folders:
            if entry.is_dir():
                root_dir.append(entry)
        return root_dir
    
    # list of files without directory 
    def getSubDir_file(self, f_path):
        root_dir_file = []
        self.f_path = f_path
        folders = os.scandir(self.f_path)
        for entry in folders:
            if entry.is_file():
                root_dir_file.append(entry)
        return root_dir_file
    
    #  puts file into .config
    def putFiles(self, src_dir_list,src_file_list): # input: 2 list containing src directory and files
        self.src_dir_list = src_dir_list
        self.src_file_list = src_file_list
        dest = Path(os.environ['HOME'] + "/.config")
        git_found = False
        
        # if !destination then it will create the directoy 
        if os.path.exists(dest):
                pass
        else:
            os.mkdir(dest)
            
        try:
            # copies entire directory 
            for key_dir in self.src_dir_list:
                src = r"{}".format(Path(key_dir))
                base_dir = os.path.basename(src)
                dest_subdir = dest.joinpath(base_dir)
                if key_dir:
                    if os.path.exists(config.GITPATH) and key_dir.name == config.GIT_DIR: # if .git exists skip and continue
                        git_found = True  # noqa: F841
                        print(f"Git directory found!, skipping >> {key_dir.name}")
                        continue
                    else:
                        shutil.copytree(src,dest_subdir, dirs_exist_ok=True)
                        
            # copies files       
            for key_file in self.src_file_list:
                src = r"{}".format(Path(key_file))
                if key_file:
                    shutil.copyfile(src, dest.joinpath(key_file.name))
                    
        except Exception as e:
<<<<<<< HEAD
            return print(f"Something went wrong!, error: {e}")
            
                
            
        
=======
            return print(f"Something went wrong!, error: {e}")
>>>>>>> c76c2eb (Code Refactor)
