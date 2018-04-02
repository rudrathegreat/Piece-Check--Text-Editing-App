# Piece Check - Text Editing Application
## Libraries

There are several libraries in this application, each handling a different part of the system. Let's look into them.

### Tkinter

----------------------------------------------------------------------------------------------------------------------------------------

Tkinter is a built-in library that have the functions to create widgets, windows and button, so the system uses Tkinter to manage all the display and the GUI 
interface.

#### Text Widgets

This code below allows you to create a widget - 

```Python

import tkinter

master = Tk()
T = Text(length = 200, width = 100)
T.pack()

master.loop()

```

#### Buttons

This code below will allow you to create buttons in the 'Frame' widget - 

```Python

import tkinter # Imports Tkinter into the program

master = Tk()
Frame = Text(master, length = 50, width = 30) # The text widget
Frame.pack() # Tells where to be in the 'Frame' Widget

button = Button(Frame, text="QUIT", command=quit) # Creates the button
button.pack(side = LEFT)

master.mainloop() # Keeps the 'master' widget system running
```
Along with other manually-made methods like -

```Python

import tkinter # Imports Tkinter into the program

master = Tk()
Frame = Text(master, length = 50, width = 30) # The text widget
Frame.pack() # Tells where to be in the 'Frame' Widget

def Say_Hello(): # Define Method
  T.insert(END, 'Hello and this is my app') # This inserts text into the widget
  print('Hello and this is my app')

button = Button(Frame, text="QUIT", command=Say_Hello) # Creates the button
button.pack(side = LEFT)

master.mainloop() # Keeps the 'master' widget system running
```
----------------------------------------------------------------------------------------------------------------------------------------

### Os

----------------------------------------------------------------------------------------------------------------------------------------

Os is another library with the capability to save and create files. With this functionality, 'Os' and another manually-made class called
'File_Management' together do the saving of the system. The path module located inside the 'Os' library is what mainly everybody uses.

```Python

import os.path
```

#### How to Save Using Python

The code below will allow you to save simple, text files using Os and Python 3.6 - 

```Python

import os.path

Name = input("What is the name of the file: ")
CompleteName = Name + ".txt"
#Alter this line in any shape or form it is up to you.
File = open(CompleteName , "w")

toFile = raw_input("Write what you want into the field")

File.write(toFile)

File.close()
```
----------------------------------------------------------------------------------------------------------------------------------------

#### Adding Entry Widgets

----------------------------------------------------------------------------------------------------------------------------------------

Adding Tkinter's functionality to accept entries, we can create a GUI way to interact with the user so that it can give the file name and address - 

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
----------------------------------------------------------------------------------------------------------------------------------------

### Ginger It, REST API

----------------------------------------------------------------------------------------------------------------------------------------

The Ginger It open-source library for Python allows you to check for any mistakes in the user's text. It uses and API known as Ginger It and sends requests to the API and receives a response. If you want to learn more about the API, the you can check out the API documentation.

#### The Parse Command

There are two methods you can use but the one which we are going to use is the parse command -

```Python

from gingerit.gingerit import GingerIt

text = 'My namr is Rudra. Eye lik to plai socer and I luv yuo.'

parse(text)

print(parse(text))

```

Make sure that your text has some errors in it. The correct sentence was - 

*'My name is Rudra. I like to play soccer and I love you.'*

---------------------------------------------------------------------------------------------------------------------------------------
