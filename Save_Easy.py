import tkinter
import os.path

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
