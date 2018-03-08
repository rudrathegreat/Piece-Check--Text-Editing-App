# Piece Check - Text Editing Application
## Libraries
There are several libraries in this application, each handling a different part of the system. Let's look into them.

### Tkinter

Tkinter is a built-in library that have the functions to create widgets, windows and button, so the system uses Tkinter to manage all the display and the GUI 
interface.

This code below allows you to create a widget - 

```Python

import tkinter

master = Tk()
T = Text(length = 200, width = 100)
T.pack()

master.loop()

```
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

### Os

Os is another library with the capability to save and create files. With this functionality, 'Os' and another manually-made class called
'File_Management' together do the saving of the system. The path module located inside the 'Os' library is what nainly everybody uses.

```Python

import os.path
```
