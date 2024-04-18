from tkinter import filedialog
from tkinter import Tk
from tkinter import *
root=Tk()
root.filename=filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All Files","*.*")))
text1=open(root.fileName).read()
T = Text(root, height=25, width=80)
T.pack()
T.insert(END,text1)
root.mainloop()
