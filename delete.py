import os
import shutil
import time
days=30
path = "C:/Users/arjun/Downloads/3"
seconds = time.time() - (days * 24 * 60 * 60)
listofFiles= os.listdir(path)

def remover():
    if(seconds>=listofFiles):
        os.remove(listofFiles)

listofFiles= os.listdir(path)
if(os.path.exists(path)):
    remover()





    





			