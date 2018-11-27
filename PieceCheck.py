# PieceCheck.py

# Start-----------------------------------------------------------------------------------------------------------------
from future.moves.tkinter import scrolledtext

from File_Management.Management import File
from tkinter import *
import tkinter.scrolledtext as scrolledText
import os.path
from gingerit.gingerit import GingerIt
#from time import sleep

global master1
file = File()
master = Tk()
master.title("PieceCheck - Spelling & Grammar Checker")
master.configure(bg= 'SlateGray1')
master.state('zoomed')
topFrame = Frame(master)
topFrame.configure(bg= 'SlateGray1')
topFrame.pack()
labelTitle = Label(topFrame, text='Hello and welcome to PieceCheck',font=('Verdana', 20), bg= 'OliveDrab1', foreground='royal blue')
labelTitle.pack(side=TOP)
middleFrame = Frame(master)
middleFrame.configure(bg= 'SlateGray1')
middleFrame.pack()

bottomframe = Frame(master)
bottomframe.configure(bg= 'SlateGray1')
bottomframe.pack( side = BOTTOM )

textBoxEnteredText = Text(middleFrame,  height=35, width=100, wrap=WORD)
textBoxEnteredText.focus_set()
textBoxEnteredText.pack(padx=20,pady=15,side=LEFT)

labelCorrectionsWidget = Label(middleFrame, text='Corrections',font=('Verdana', 20), bg= 'SlateGray1', foreground='royal blue')
labelCorrectionsWidget.pack(padx=10,pady=5, side=TOP)

textBoxCorrections = scrolledText.ScrolledText(middleFrame,  height=28, width=50, wrap=WORD)
textBoxCorrections.config(state=DISABLED)
textBoxCorrections.pack(padx=20,pady=5, side=RIGHT)

# Define Methods and Functions------------------------------------------------------------------------------------------


def save(widget_text):  # This is the saving process
    master1 = Tk()

    def create_file():  # This creates the file and saves it there
        file.save_file(widget_text, get_file_path())
        master1.destroy()

    Label(master1, text="File Path").grid(row=0)
    Label(master1, text="File Name").grid(row=1)
    global e1
    global e2
    e1 = Entry(master1, width=40)
    e2 = Entry(master1, width=40)
    e1.insert(END, 'D:\\temp')
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(master1, text='Save File', command=create_file).grid(row=3, column=1, sticky=W, pady=4)
    master1.mainloop()
    

def get_file_path():  # This creates the file path
    return os.path.join(e1.get(), e2.get() + ".txt")
    

def save_as_it_is():  # Saves what is currently on the main window
    save(get_input_text())
    


def save_without_corrections():  # This saves the text with no corrections
    save(response['text'])
    


def save_with_corrections():  # This saves the text with corrections
    textBoxEnteredText.delete(1.0, END)
    textBoxEnteredText.insert(END, response['result'])
    save(response["result"])
    


def parse():  # This checks for any mistakes or corrections and presents it based on the different situations
    master3 = Tk()
    global correctionsWidget
    correctionsWidget = scrolledText.ScrolledText(master3, height=30, width=60,wrap=WORD)
    correctionsWidget.pack()
    parser = GingerIt()
    global response
    response = parser.parse(get_input_text())
    global without_correction_text

    if len(response['corrections']) < 1:
        correctionsWidget["bg"] = 'yellow'
        correctionsWidget.insert(END, 'Good Job Champion!!!\n', ('no_error'))
        correctionsWidget.tag_configure('no_error', font=('Verdana', 20, 'bold'), foreground='green')
        correctionsWidget.insert(END, 'Your Text is correct: ' + str(textBoxEnteredText.get(1.0, END)))
        
    else:
        correctionsWidget["bg"] = 'light blue'
        correctionsWidget.insert(END, 'You have got some error(s).\n', ('error_heading'))
        correctionsWidget.tag_configure('error_heading', font=('Verdana', 20, 'bold'), foreground='red')
        correctionsWidget.insert(END, 'Your Text: ' + str(textBoxEnteredText.get(1.0, END)) + '\n')
        correctionsWidget.insert(END,
                  '\nShould it be this?: ''' + response['result'] + '\n')
        

    Button(master3, text=' Save Without Corrections ', command=save_without_corrections).pack(side=LEFT)
    Button(master3, text=' Save With Corrections ', command=save_with_corrections).pack(side=LEFT)
    Button(master3, text=' Show All Corrections ', command=find_num_of_corrections).pack(side=LEFT)
    master3.mainloop()
    


def find_num_of_corrections():  # Finds out the number of mistakes and presents them in a friendly way.
    data = response['corrections']

    for i in range(len(data)):  # A loop
        correctionsWidget.insert(END, '\nYour Mistake: ' + data[i]['text'], ('mistakes'))
        correctionsWidget.tag_configure('mistakes', foreground='red')
        correctionsWidget.insert(END, '\nCorrection: ' + data[i]['correct'], ('corrections'))
        correctionsWidget.tag_configure('corrections', foreground='green')

        textBoxCorrections.config(state=NORMAL)
        textBoxCorrections.insert(END, '\nYour Mistake: ' + data[i]['text'], ('mistakes'))
        textBoxCorrections.tag_configure('mistakes', foreground='red')
        textBoxCorrections.insert(END, '\nCorrection: ' + data[i]['correct'], ('corrections'))
        textBoxCorrections.tag_configure('corrections', foreground='green')
        textBoxCorrections.config(state=DISABLED)
        


def get_input_text():  # This grabs the text which the user has written
    return textBoxEnteredText.get(1.0, END).rstrip('\n')
    

# Main System-----------------------------------------------------------------------------------------------------------
textBoxEnteredText.insert(END, 'Type your text here', 'font')
textBoxEnteredText.tag_configure('font', font=('Verdana', 10), foreground='royal blue')


saveButton = Button(bottomframe, text='     Save     ', command=save_as_it_is, bg="Lightblue1", foreground='royal blue', font=('Verdana', 12))
checkMyWorkButton = Button(bottomframe, text='  Check My Work  ', command=parse, bg="Lightblue1", foreground='royal blue', font=('Verdana', 12))
quitButton = Button(bottomframe, text='     Quit     ', command=master.quit, bg="Lightblue1", foreground='red', font=('Verdana', 12))
saveButton.pack(side=LEFT)
checkMyWorkButton.pack(side=LEFT)
quitButton.pack(side=RIGHT)


mainloop()
# End-------------------------------------------------------------------------------------------------------------------
