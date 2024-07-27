import typer
import os
import shutil
from models import FileHandling
import time


def main():
    path = input("Enter the path: ")
    file_handle = FileHandling(path)

    avg_time = 0.0
    for _ in range(10):
        if os.path.exists("/home/fastaf/cli project/posthoppin/.config"):
            shutil.rmtree(
                "/home/fastaf/cli project/posthoppin/.config", ignore_errors=True
            )

    start_time = time.time()
    folders_path = file_handle.getPath()
    path_list = file_handle.getSubDir(folders_path)

    file_handle.putFiles(path_list)

    end_time = time.time() - start_time
    avg_time += end_time

    print(f"execution compelete: {(avg_time*1000)/10:.2f}'s ")


if __name__ == "__main__":
    typer.run(main)
