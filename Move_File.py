import os
import shutil

source = "C:/Users/Downloads"
destination = "C:/Users/Downloaded"
allfiles = os.listdir(source)

for file in allfiles:
    name,extension = os.path.splitext(file)

    if extension == '':
        continue

    if extension == ['.txt', '.doc', '.pdf', '.docx']:
        path1 = source + '/' + file
        path2 = source = '/' + "Document_Files"
        path3 = source = '/' + "Document_Files" + '/' + file
        
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
              


    
    

