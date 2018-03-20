# Piece Check - Text Editing Application
## Graphical User Interfaces
### What is it?

----------------------------------------------------------------------------------------------------------------------------------------

Graphical User Interfaces, or when abbreviated GUIs, are mainly used to make the application user-friendly. They are everywhere! Nearly all operating systems use GUIs to communicate with the user conveniently and effieciently. One of those operating systems is Windows, by Microsoft.

----------------------------------------------------------------------------------------------------------------------------------------

### Examples

----------------------------------------------------------------------------------------------------------------------------------------

I mentioned that GUIs are usec everywhere, so, where are they used. You are probably familiar with Windows and its convenience and relaxation.bYou can change the settings at any time. All you ave to do it click these icons, click these buttons... it goes on until you have saved the settings. That is a GUI! If you add a window or widget, add some buttons and made some operations for the buttons so that they actually work, then you have just created a GUI. But the GUI has to be appropriate for your app. GUIs are used in operating systems such as Windows, games such as Clash of Clans or even online, as long as the interface allows the user to add their desired commands.

----------------------------------------------------------------------------------------------------------------------------------------

### Connections

----------------------------------------------------------------------------------------------------------------------------------------

In this case, tkinter manages the GUI for the system and allows the user to type, check and save the texts as needed. So I cerated the GUI so that it works with the application well.

Recalling on how to make a widget from the Libraries documentation, we can make several widgets, each for their own purpose -

```Python

import tkinter

master = Tk()

T = Text(master, length = 100, width = 75)
T.pack()
T.insert(END, 'Hello and this is my window')

master.mainloop()

```

----------------------------------------------------------------------------------------------------------------------------------------

### A Mix Up

So, what is the difference between GUI and API. This discusion is mentioned over in the API documentation. Basically, GUI is used for interfaces between the user and the application and the API is used between two different applications.

To find out more about GUI, check out the link in the just below -

https://www.youtube.com/watch?v=XIGSJshYb90

----------------------------------------------------------------------------------------------------------------------------------------
