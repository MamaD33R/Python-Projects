import shutil, os, glob, datetime
import tkinter as Tk
from tkinter import *
from datetime import timedelta
from tkinter import filedialog

sourc = 'C:/Users/space/OneDrive/Documents/GitHub/Python-Projects/File Transfer Shutil/Files'
dest = 'C:/Users/space/OneDrive/Documents/GitHub/Python-Projects/File Transfer Shutil/Updated'

files = os.listdir(sourc) 
files.sort()
time = os.path.getmtime(sourc)
datetime = datetime.datetime.fromtimestamp(time)

def filechecking(files):
    for f in files:
        print(f)
        src = sourc+f
        dst = dest+f
        try:
            if datetime.now() - timedelta(hours=24):
                path = os.path.join(src, f)
                shutil.move(path,dest)
        except OSError:
            pass

root = Tk()
root.title("File Check")
root.geometry('500x400')
root.resizable(False, False)
lbl = Label(root, text="Browse folders...", font=("Arial Bold", 15))
lbl.grid(row=1, column=4, pady=20,padx=20)

btn1 = Button(root, text="Browse Unchecked", command=lambda:browse_button())
btn1.grid(column=4,row=7,padx=5,pady=5)

btn1 = Button(root, text="Browse Receiving Folders", command=lambda:browse_button())
btn1.grid(column=4,row=8,padx=5,pady=5)

btn1 = Button(root, text="Check for updated files", command=lambda:filechecking(files))
btn1.grid(column=4,row=9,padx=5,pady=5)

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)



if __name__ == "__main__":
    root.mainloop()
