import os
from pathlib import Path 

class View:
    def fileInput(self) :
        layer = 0 
        filePath = Path(input("Enter the path: ")) 
        if filePath.exists():
            directories = os.walk(filePath)
            for (dirpath, dirname, filenames) in directories:
                print(f"{dirname} \n\n {filenames}")
        else:
            print("Path doesn't exists")

         