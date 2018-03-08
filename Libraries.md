# Piece Check - Text Editing Application
## Libaries
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
