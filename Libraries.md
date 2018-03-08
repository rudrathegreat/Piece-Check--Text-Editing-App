# Libraries
There are several libraries in this application, each handling a different part of the system. Let's look into them.

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
