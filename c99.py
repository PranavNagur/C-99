import os
import shutil
source=input('Enter source folder')
destination=input('Enter folder destination:')
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)