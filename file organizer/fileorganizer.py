import os
import shutil

def organize_dir(path):
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file) #basically text.txt -> text    .txt
        extension = extension[1:] # .txt --> txt

        if os.path.exists(path + "/" + extension) == True: 
            shutil.move(path + "/" + file , path + "/" + extension + "/" + file)
        elif os.path.exists(path + "/" + extension) == False:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)


path = "C:\\Users\\shouv\\Downloads"  

organize_dir(path)

# coming soon...
def restorepathorder():
    pass


