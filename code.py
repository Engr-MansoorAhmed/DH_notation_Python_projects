from Tkinter import *
import tkMessageBox
import numpy as np
import pandas as pd
import math

project = Tk()
class gui:
    def __init__(self, project):
        self.project= project
        self.project.title("DH notation project of robotics")
        self.project.geometry("600x600+500+100")
        textfield1 = Entry(self.project, fg="WHITE", bg="Grey", font=(12))
        textfield1.place(x=170, y=75, width=50, height=30)
        textfield2 = Entry(self.project, fg="WHITE", bg="Grey", font=(12))
        textfield2.place(x=170, y=140, width=50, height=30)
        textfield3 = Entry(self.project, fg="WHITE", bg="Grey", font=(12))
        textfield3.place(x=170, y=205, width=50, height=30)
        textfield4 = Entry(self.project, fg="WHITE", bg="Grey", font=(12))
        textfield4.place(x=400, y=140, width=50, height=30)
        textfield5 = Entry(self.project, fg="WHITE", bg="Grey", font=(12))
        textfield5.place(x=400, y=205, width=50, height=30)
        textBox = Text(self.project, fg="Black", bg="light Yellow" , font =(12))
        textBox.place(x=40, y=260, width=410, height=180 )
        Label(self.project, text="DH NOTATION SOLVER", font=("Yu Gothic UI Semibold", 17)).place(x=90, y=1, width=300, height=50)
        Label(self.project, text="Number of joints=", font=("Yu Gothic UI Semibold", 10)).place(x=35, y=70, width=120,height=50)
        Label(self.project, text="Theta in degrees", font=("Yu Gothic UI Semibold", 10)).place(x=15, y=130, width=150,height=50)
        Label(self.project, text="Alpha in degrees", font=("Yu Gothic UI Semibold", 10)).place(x=15, y=190,width=150, height=50)
        Label(self.project, text="d    ", font=("Yu Gothic UI Semibold", 10)).place(x=250, y=130,width=150, height=50)
        Label(self.project, text="a    ", font=("Yu Gothic UI Semibold", 10)).place(x=250, y=190,width=150, height=50)
        pi = 3.141592653589793238
        self.mylist = []
        self.resultant_matrix = []
        def button1():
            if len(self.mylist) > 1:

                    for n in range(1, len(self.mylist)):
                        self.mylist[0] = np.dot(self.mylist[0] , self.mylist[n])

                    self.resultant_matrix.append(self.mylist[0])
                    textBox.insert(INSERT, "\n\nResult = \n ")
                    textBox.insert(INSERT, self.resultant_matrix[0])
            else:

                    textBox.insert(INSERT, "\n\nResult = \n ")
                    textBox.insert(INSERT, self.resultant_matrix[0])


        def button2():
            angletheta = textfield2.get()
            anglealpha = textfield3.get()
            d = textfield4.get()
            a = textfield5.get()
            dummy= pi/180
            if (len(self.mylist)>=int(textfield1.get()) ) :
                tkMessageBox.showwarning("", "matrices exceed number of joints ")
            else:
                self.mylist.append(np.round((np.array([
                    [
                        math.cos(dummy * float(angletheta)),
                        -1 * math.sin(dummy * float(angletheta)) * math.cos(dummy * float(anglealpha))
                        , math.sin(dummy * float(angletheta)) * math.sin(dummy * float(anglealpha)),
                        float(a) * math.cos(dummy * float(angletheta))

                    ],
                    [
                        math.sin(dummy * float(angletheta)),
                        math.cos(dummy * float(angletheta)) * math.cos(dummy * float(anglealpha)),
                        -1 * math.cos(dummy * float(angletheta)) * math.sin(dummy * float(anglealpha)),
                        float(a) * math.sin(dummy * float(angletheta))],

                    [0, math.sin(dummy * float(anglealpha)), math.cos(dummy * float(anglealpha)), float(d)],

                    [0, 0, 0, 1]]

                )), 3))
            textfield2.delete(0, END)
            textfield3.delete(0, END)
            textfield4.delete(0, END)
            textfield5.delete(0, END)

        def button3():
            textBox.delete('1.0' , END)
            textfield1.delete(0 , END)
            self.mylist = []
            self.resultant_matrix = []
            tkMessageBox.showinfo("" , "the program is reset")

        Button(self.project
               , text="Solve", fg="Blue", bg="Grey",
               activebackground="Yellow", activeforeground="Red", command=button1,
               font=("Yu Gothic UI Semibold", 14)).place(x=130, y=450, width=200, height=30)
        Button(self.project
               , text="Add", fg="Blue", bg="Grey",
               activebackground="Yellow", activeforeground="Red", command=button2,
               font=("Yu Gothic UI Semibold", 14)).place(x=340, y=450, width=70, height=30)
        Button(self.project
               , text="Reset", fg="Blue", bg="Grey",
               activebackground="Yellow", activeforeground="Red", command=button3,
               font=("Yu Gothic UI Semibold", 14)).place(x=50, y=450, width=70, height=30)
gui(project)
project.mainloop()

