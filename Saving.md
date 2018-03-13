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
  
Button(master, text = 'Save', option = Save)
Button.pack()

master.mainloop( )
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

### GUI

GUI is the term used by computer professionals. GUI stands for Graphical User Interface and is what keeps the system user-friendly. Basically, if you want to save a file, you need some input of the file name and address. But you don't want the user to continually type his/her opinion in the Python Shell, so it is better if we add an entry widget. If you have got no idea of what I was just talking about, check the other documentation on this repository or surf on the internet for the answers. The code for the Entry Widget is - 

```Python

import tkinter


master = Tk()
Label(master, text="File Name").grid(row=0)
Label(master, text="File Address").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.pack()
e2.pack()

master.mainloop()
```

### Combining Them Together

Combining these three key principles of 'Os', Tkinter's 'get' command and Entry Widgets, we put these together to make one big saving process. But before we get into showing the code, it is best to understand the flow of the process and how everything fits in.

When the program is run, there should be a widget where you type your text. It should have a button known as 'save'. If the button is pressed, an entry widget will appear asking for the file name and address. There will also be a button in the entry widget 
known as 'save'. Once the values are given, then it will save the file in the folder with the specific name. When you open the file, you should have your text there.

```Python

import tkinter
import os.path

master = Tk()
T = Text(master, length = 100, width = 75)
T.pack()

def Get_Data():
  master_1 = Tk()
  Label(master_1, text="File Name").grid(row=0)
  Label(master_1, text="File Address").grid(row=1)

  e1 = Entry(master_1)
  e2 = Entry(master_1)
  e1.pack()
  e2.pack()
  
  def Save_Text():
    Text = T.get(1.0, END)
    data1 = e1.get()
    data2 = e2.get()
  
    replace(data2, '\', '\\')
    completeName = str(data2) + str(data) + '.txt'
    print('completeName')

    file = open(completeName, 'w')
    file.write(Text)
    file.close()
  
  Button(master_1, text = 'Save', option = Save_Text)
  
  master_1.mainloop()
   
Button(master, text = 'Save Text', option = Get_Data)

master.mainloop()
```
