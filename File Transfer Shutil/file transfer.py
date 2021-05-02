import shutil, os, glob, datetime
import tkinter as Tk
from tkinter import *
from datetime import timedelta
from tkinter import filedialog

root = Tk()

srcEntry = Entry(root)
srcEntry.grid(column=4, row=3)

destEntry = Entry(root)
destEntry.grid(column=5, row=3)

def filechecking():
    #grabs list of files from source path this way
    files = os.listdir(srcEntry.get())
    for file in files:
        fullFilePath = srcEntry.get() + '/' + file
        # getting mtime of full file path and name
        time = os.path.getmtime(fullFilePath)
        modtime = datetime.datetime.fromtimestamp(time)
        if modtime > (datetime.datetime.now() - timedelta(hours = 24)):
            shutil.move(fullFilePath, destEntry.get())
            # any modtime within 24 hours will be moved to dest folder


root.title("File Check")
root.geometry('500x400')
root.resizable(False, False)
lbl = Label(root, text="Browse folders...", font=("Arial Bold", 15))
lbl.grid(row=1, column=4, pady=20,padx=20)

btn1 = Button(root, text="Browse Unchecked", command=lambda:browse_button())
btn1.grid(column=4,row=7,padx=5,pady=5)

btn1 = Button(root, text="Browse Receiving Folders", command=lambda:browse_button2())
btn1.grid(column=4,row=8,padx=5,pady=5)

btn1 = Button(root, text="Check for updated files", command=lambda:filechecking())
btn1.grid(column=4,row=9,padx=5,pady=5)

# gets paths of folders with these functions
def browse_button():
    source = filedialog.askdirectory()
    srcEntry.delete(0, END)
    srcEntry.insert(END, source)

def browse_button2():
    dest = filedialog.askdirectory()
    destEntry.delete(0, END)
    destEntry.insert(END, dest)
    



if __name__ == "__main__":
    root.mainloop()
