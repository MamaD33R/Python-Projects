
import webbrowser
import tkinter as Tk
from tkinter import *

window = Tk()
# GUI resizable window
window.title("Web Page Generator")
window.geometry('600x350')
# label details of program
lbl = Label(window, text="Greetings! Go ahead and get started!", font=("Arial Bold", 15))
lbl.grid(row=1, column=4, pady=20, padx=20)
lbl2 = Label(window, text="HTML Text Here: ")
lbl2.grid(row=2, column=2)
# the entry textbox for the body text
txt = Entry(window,width=50)
txt.grid(column=4, row=6, padx=20, pady=15)
# button to submit the new text to generated webpage
btn1 = Button(window, text="CREATE", bg="lightgreen", command=lambda:CREATE())
btn1.grid(column=4, row=7, padx=5, pady=5)
# the function to generate the html body text and open in new tab
def CREATE():
    entryText = txt.get()
    htmlCode = "<!DOCTYPE html><head><title>Generated Webpage</title></head><body> {} </body></html>".format(entryText)

    f = open("webpage.html", "w")
    f.write(htmlCode)
    f.close()

    webbrowser.open_new_tab("C:/Users/space/OneDrive/Documents/GitHub/Python-Projects/Web Page Generator/webpage.html")



if __name__ == "__main__":
    window.mainloop()
