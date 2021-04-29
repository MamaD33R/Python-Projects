
import shutil, os, glob, time
def moveAll(srcDir, dstDir):
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        for filePath in glob.glob(srcDir + '\*'):
            shutil.move(filePath, dstDir);      # moving files from folder A to folder B
    else:
        print("srcDir & dstDir should be Directories")

source = '/python_projects/FolderA'
destination =  '/python_projects/FolderB'
    
moveAll(source,destination)
#________________________

sourc = '/python_projects/Files'
dest = '/python_projects/Updated'

files = os.listdir(sourc) # Transfering updated files to Updated folder
files.sort()

for f in files:
    print(f)
    src = sourc+f
    dst = dest+f
    try:
        if os.stat(src).st_mtime < os.stat(dst).st_mtime: 
            continue
    except OSError:
        pass
    
