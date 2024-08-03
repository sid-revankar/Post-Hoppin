import typer
from models import FileHandling

def main():
    path = input("Enter the path: ")
    file_handle = FileHandling(path)
    
    folders_path = file_handle.getPath()
    path_dir_list = file_handle.getSubDir(folders_path)
    path_file_list = file_handle.getSubDir_file(folders_path)

    file_handle.putFiles(path_dir_list,path_file_list)

if __name__ == "__main__":
    typer.run(main)
