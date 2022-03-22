from pathlib import Path
import os.path
import new
dict = new.cli()


path = dict["path"]

def dirSize(path_root):
    directory_size = 0
    for file in os.listdir(path_root):
        if os.path.isdir(path_root + '/' + file):
            path_root_2 = path_root + '/' + file
            directory_size += dirSize(path_root_2)
        if os.path.isfile(path_root + '/' + file):
            Path(path_root).stat()
            file_size = Path(path_root).stat().st_size
            directory_size += file_size
    return directory_size

def readable(size, listBit, index):
    type = listBit[index]
    if size < 1024 :
        result = "The folder weighs " + str(round(size, 2)) + " " + type
        return result
    else :
        size = size / 1024
        result = readable(size, listBit, index + 1)
    return result


listBit = ["byte", "KB", "MB", "GB", "TB"]
directory_size = dirSize(path)
if dict['readable'] == True :
    print(readable(directory_size, listBit, 0))
else :
    print("The folder weighs " + str(directory_size) + " bytes")


