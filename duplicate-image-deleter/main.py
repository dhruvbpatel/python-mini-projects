import os, hashlib
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path


if __name__ == '__main__':

    Tk().withdraw()
    path = askdirectory(title =  "select a folder")
    
    files = os.listdir(path)

    unique = dict()
    
    for file in files:
        filename = Path(os.path.join(path, file))

        if filename.is_file():

            fileHash = hashlib.md5(open(filename,'rb').read()).hexdigest()

            if fileHash not in unique:
                unique[fileHash] = filename
            else:
                os.remove(filename)
                print("Successfully deleted {file_name} !!")
        else:
            print("Operation Unsuccessful !!")






    