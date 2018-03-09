# Piece Check - Text Editing Application
## The Saving Part of the System
### Os Revisited

Os is the library that handles all the saving process of the system. If you want to have a in-depth read of 'Os', then check out the Libraries documentation. Recalling from the Libraries documentation, a simple way to save a file using 'Os' is shown below - 

```Python

import tkinter
import os.path


master = Tk()
Label(master, text="File Name").grid(row=0)
Label(master, text="File Address").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.pack()
e2.pack()

def Save():
  data1 = e1.get()
  data2 = e2.get()
  
  replace(data2, '\', '\\')
  completeName = str(data2) + str(data) + '.txt'
  print('completeName')
  
  file = open(completeName, 'w')
  Text = 'Welcome to the Os library!'
  file.write(Text)
  file.close()
  
Button(text = 'Save', option = Save)
Button.pack()

mainloop( )
```

### How to get the Text

So, how do you get the text? With the get command from tkinter, any text can be grabbed, copied and pasted into the file. If you haven't read about Tkinter or you do not understand, check out the Libraries documentation or the README 'overview'. The code for this is -

```Python

import tkinter

master =  Tk()
T = Text(master, length = 200, width = 100)
T.pack()

def get():
  Text = T.get('1.0', END)
  print(str(Text))
  
Button(master, text = 'Get Text', option = get)
Button.pack(side = BOTTOM)

master.mainloop()
```
