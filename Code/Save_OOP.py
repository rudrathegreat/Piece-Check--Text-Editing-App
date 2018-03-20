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
  
  data_1 = e1.get()
  data_2 = e2.get()
  text = T.str((1.0, END))
  
  File_Management.save_text(data_1, data_2, text)
  
  master_1.mainloop()
  
Button(master, text = 'Save Text', option = Get_Data)

master.mainloop()

		
