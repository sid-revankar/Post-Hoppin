import typer
import os
import shutil
from models import File_Handling
import time

def main():
    path = input("Enter the path: ")
    file_handle = File_Handling(path)

    avg_time = 0.0
    for _ in range(10):
        if os.path.exists("/home/fastaf/cli project/posthoppin/.config"):
            shutil.rmtree(
                "/home/fastaf/cli project/posthoppin/.config", ignore_errors=True
            )

    start_time = time.time()
    folder_path = file_handle.get_path()
    path_list = file_handle.dir_sort(folder_path)

    File_Handling.dir_keyValuePair = file_handle.passTree(path_list)

    end_time = time.time() - start_time
    avg_time += end_time


    print(f"execution compelete: {(avg_time*1000)/10:.2f}'s ")

if __name__ == "__main__":
    typer.run(main)