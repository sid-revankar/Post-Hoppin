"""
File handling module for the Post-Hoppin application.

This module provides functionality for copying dotfiles and directories
to the user's .config directory. It includes methods for listing subdirectories
and files, and copying them to the destination.

Classes:
    FileHandling: Handles file and directory operations.

Dependencies:
    os, shutil, pathlib.Path, rich.console, rich.theme
"""

import os
import shutil
from pathlib import Path
import config
from rich.console import Console
from rich.theme import Theme

# Define color themes for console output
themes = Theme(
    {
            "info": "dim cyan",
            "warning": "yellow",
            "Alert": "bold red",
            "Highlight": "#7FFFD4",
    }
)
console = Console(theme=themes)
class FileHandling:

    """
    A class for handling file and directory operations.

    This class provides methods for getting file paths, listing subdirectories
    and files, and copying files and directories to the user's .config directory.

    Attributes:
        path (str): The base path for file operations.
    """
    
    def __init__(self, path):
        self.path = path

    def getPath(self):
        f_path = Path(self.path)
        return f_path
    
    def getSubDir(self, f_path):
        """
        Get a list of subdirectories in the given path.

        Args:
            f_path (Path): The path to scan for subdirectories.

        Returns:
            list: A list of directory entries.
        """
        root_dir = []
        self.f_path = f_path
        folders = os.scandir(self.f_path)
        for entry in folders:
            if entry.is_dir():
                root_dir.append(entry)
        return root_dir
     
    def getSubDir_file(self, f_path):
        """
        Get a list of files (not directories) in the given path.

        Args:
            f_path (Path): The path to scan for files.

        Returns:
            list: A list of file entries.
        """
        root_dir_file = []
        self.f_path = f_path
        folders = os.scandir(self.f_path)
        for entry in folders:
            if entry.is_file():
                root_dir_file.append(entry)
        return root_dir_file
    
    
    def putFiles(self, src_dir_list,src_file_list):
        """
        Copy directories and files to the .config directory.

        Args:
            src_dir_list (list): List of source directories to copy.
            src_file_list (list): List of source files to copy.
        """
        self.src_dir_list = src_dir_list
        self.src_file_list = src_file_list
        dest = Path(os.environ['HOME'] + "/.config")
        # Create destination directory if it doesn't exist
        if os.path.exists(dest):
                pass
        else:
            os.mkdir(dest)
            
        try:
            # Copy directories
            for key_dir in self.src_dir_list:
                src = r"{}".format(Path(key_dir))
                base_dir = os.path.basename(src)
                dest_subdir = dest.joinpath(base_dir)
                if key_dir:
                    if os.path.exists(config.GITPATH) and key_dir.name == config.GIT_DIR: # if .git exists skip and continue  
                        console.print(
                            f"{key_dir.name} found!", end=" ", style="Highlight"
                        )
                        console.print("skipping >>", style="info")
                        continue
                    else:
                        if os.path.exists(dest / dest_subdir):
                            console.print(
                                f"{key_dir.name} found!", end=" ", style="Highlight"
                            )
                            console.print("skipping >>", style="info")
                        else:
                            shutil.copytree(src,dest_subdir, dirs_exist_ok=True)
                            
            # Copy files
            for key_file in self.src_file_list:
                src = r"{}".format(Path(key_file))
                if key_file:
                    if os.path.exists(dest / dest_subdir):
                        console.print(
                            f"{key_dir.name} found!", end=" ", style="Highlight"
                        )
                        console.print("skipping >>", style="info")
                    else:
                        shutil.copyfile(src, dest.joinpath(key_file.name))
                    
        except Exception as e:
            return print(f"Something went wrong!, error: {e}")

    def putSingleFiles(self,dotfiles):
        """
        Copy a single file to the .config directory.

        Args:
            dotfiles (str): Path to the file to be copied.
        """
        src = Path(dotfiles)
        basename = os.path.basename(src)
        dest = Path(os.environ['HOME'] + "/.config")
        if os.path.exists(dest):
            pass
        else:
            os.mkdir(dest)
            
        try:
            if src.is_dir():
                pass
            else:
                if os.path.exists(dest / basename):
                    console.print(f"{basename} found!", end=" ", style="Highlight")
                    console.print("skipping >>", style="info")                
                else:
                    shutil.copyfile(src, dest.joinpath(basename))
        except Exception as e:
            return print(f"Something went wrong!, error: {e}")
        
    def putSingleDir(self,dotDir):
        """
        Copy a single directory to the .config directory.

        Args:
            dotDir (str): Path to the directory to be copied.
        """
        src = Path(dotDir)
        basename = os.path.basename(src)
        dest = Path(os.environ["HOME"] + "/.config")
        if os.path.exists(dest):
            pass
        else:
            os.mkdir(dest)
            
        try: 
            if src.is_file():
                pass
            else:
                if os.path.exists(dest / basename):
                    console.print(f"{basename} found!", end=" ", style="Highlight")
                    console.print("skipping >>", style="info")
                else:
                    shutil.copytree(src, dest.joinpath(basename))
        except Exception as e:
            return print(f"Something went wrong!, error: {e}")