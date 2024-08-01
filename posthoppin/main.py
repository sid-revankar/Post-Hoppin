import typer
from models import FileHandling


def main():
    path = input("Enter the path: ")
    file_handle = FileHandling(path)

    folders_path = file_handle.getPath()
    path_list = file_handle.getSubDir(folders_path)

    file_handle.putFiles(path_list)


if __name__ == "__main__":
    typer.run(main)
