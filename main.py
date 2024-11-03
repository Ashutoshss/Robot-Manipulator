from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
from tkinter import filedialog as fd
import os

dir_path = os.getcwd()

Position = [10,30,45,20,0,60]
# Position = [0,0,0,0,0,0]

def mainfile():
    mainfile=fd.askopenfilename(initialdir=dir_path)    #menu part: you can add the the path a you costum directory

def devel():
    tmsg.showinfo("Devel","This GUI is developed by Ashutosh Singh.\nhttps://www.linkedin.com/in/ashutosh-singh-1bb931227/")

def savedfile():
    tmsg.showinfo("Saved Successfully",f"Saved the values in a txt file in the directory.\n{dir_path}")

def help():
    tmsg.showinfo("lol","sorry we can't help you ")

def about():
    tmsg.showinfo("About me","https://github.com/Ashutoshss/Robot-Manipulator")

def planButton():
    return

def executeButton():
    return

def stopButton():
    return

def update_label(value, label):
    label.config(text=round(float(value)))

root=Tk()
root.title("")
# root.attributes('-fullscreen',True)
root.geometry("355x300")
root.resizable(0,0)

#the title bar
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="open",command=mainfile)
m1.add_command(label="Save",command=savedfile)
m1.add_command(label="exit",command=quit)
mainmenu.add_cascade(label="file",menu=m1)
# -------------------------------------------
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="add")
m2.add_command(label="add")
m2.add_command(label="add")
mainmenu.add_cascade(label="option",menu=m2)
# -------------------------------------------
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="developer info",command=devel)
m3.add_command(label="help",command=help)
m3.add_command(label="about",command=about)
mainmenu.add_cascade(label="help",menu=m3,command=help)
root.config(menu=mainmenu)

# --------------------------FRAME 1--------------------------

frame1_color="white"
frame1=Frame(root,bg=frame1_color,borderwidth=20)
frame1.pack(side=LEFT,fill=Y)

f1_label = Label(frame1,text="Commands",bg=frame1_color,font=("Calibri",11))
f1_label.grid(row=0,column=0,padx=0,pady=0)
b2_1=ttk.Button(frame1,text="Plan",command=planButton)
b2_1.grid(row=1,column=0,padx=0,pady=5)
b2_2=ttk.Button(frame1,text="Execute",command=executeButton)
b2_2.grid(row=2,column=0,padx=0,pady=5)
b2_3=ttk.Button(frame1,text="Stop",command=stopButton)
b2_3.grid(row=3,column=0,padx=0,pady=5)

roughlabel2=Label(frame1,text="",bg=frame1_color)
roughlabel2.grid(row=4,column=0,padx=0,pady=10)

f1_label1 = Label(frame1,text="Start State:",bg=frame1_color,font=("Calibri",9))
f1_label1.grid(row=5,column=0,padx=0,pady=0)
options1 = ["<current>", "Option 2", "Option 3"]
current_value1 = tk.StringVar(root)
current_value1.set(options1[0])  # Set default value
dropdown1 = ttk.Combobox(frame1, textvariable=current_value1, values=options1,width=12)
dropdown1.grid(row=6,column=0,padx=0,pady=0)

f1_label2 = Label(frame1,text="Goal State:",bg=frame1_color,font=("Calibri",9))
f1_label2.grid(row=7,column=0,padx=0,pady=0)
options2 = ["<current>", "Option 2", "Option 3"]
current_value2 = tk.StringVar(root)
current_value2.set(options1[0])  # Set default value
dropdown2 = ttk.Combobox(frame1, textvariable=current_value2, values=options2,width=12)
dropdown2.grid(row=8,column=0,padx=0,pady=0)

# --------------------------FRAME 2--------------------------

frame2_color="white"
frame2=Frame(root,bg=frame2_color,borderwidth=28)
frame2.pack(side=RIGHT,fill=Y)

style = ttk.Style()
style.configure("TScale", background=frame2_color)

# Define labels before sliders
ScaleLabel1 = Label(frame2,text=Position[0],bg=frame2_color,font=("Calibri",8))
ScaleLabel1.grid(row=0,column=2)
ScaleLabel2 = Label(frame2,text=Position[1],bg=frame2_color,font=("Calibri",8))
ScaleLabel2.grid(row=1,column=2)
ScaleLabel3 = Label(frame2,text=Position[2],bg=frame2_color,font=("Calibri",8))
ScaleLabel3.grid(row=2,column=2)
ScaleLabel4 = Label(frame2,text=Position[3],bg=frame2_color,font=("Calibri",8))
ScaleLabel4.grid(row=3,column=2)
ScaleLabel5 = Label(frame2,text=Position[4],bg=frame2_color,font=("Calibri",8))
ScaleLabel5.grid(row=4,column=2)
ScaleLabel6 = Label(frame2,text=Position[5],bg=frame2_color,font=("Calibri",8))
ScaleLabel6.grid(row=5,column=2)

l1_1=Label(frame2,text="Joint1:  ",bg=frame2_color,font=("Calibri",8))
l1_1.grid(row=0,column=0)
v1_1=IntVar()
slider1=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_1, command=lambda v: update_label(v, ScaleLabel1))
slider1.set(Position[0])
slider1.grid(row=0,column=1,padx=1,pady=5)

l1_2=Label(frame2,text="Joint2:  ",bg=frame2_color,font=("Calibri",8))
l1_2.grid(row=1,column=0)
v1_2=IntVar()
slider2=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_2, command=lambda v: update_label(v, ScaleLabel2))
slider2.set(Position[1])
slider2.grid(row=1,column=1,padx=1,pady=5)

l1_3=Label(frame2,text="Joint3:  ",bg=frame2_color,font=("Calibri",8))
l1_3.grid(row=2,column=0)
v1_3=IntVar()
slider3=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_3, command=lambda v: update_label(v, ScaleLabel3))
slider3.set(Position[2])
slider3.grid(row=2,column=1,padx=1,pady=5)

l1_4=Label(frame2,text="Joint4:  ",bg=frame2_color,font=("Calibri",8))
l1_4.grid(row=3,column=0)
v1_4=IntVar()
slider4=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_4, command=lambda v: update_label(v, ScaleLabel4))
slider4.set(Position[3])
slider4.grid(row=3,column=1,padx=1,pady=5)

l1_5=Label(frame2,text="Joint5:  ",bg=frame2_color,font=("Calibri",8))
l1_5.grid(row=4,column=0)
v1_5=IntVar()
slider5=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_5, command=lambda v: update_label(v, ScaleLabel5))
slider5.set(Position[4])
slider5.grid(row=4,column=1,padx=1,pady=5)

l1_6=Label(frame2,text="Joint6:  ",bg=frame2_color,font=("Calibri",8))
l1_6.grid(row=5,column=0)
v1_6=IntVar()
slider6=ttk.Scale(frame2,from_=0,to=100,orient="horizontal",variable=v1_6, command=lambda v: update_label(v, ScaleLabel6))
slider6.set(Position[5])
slider6.grid(row=5,column=1,padx=1,pady=5)

root.mainloop()
#                                                                                        code written by Ashutosh Singh
#                                                                                        https://github.com/Ashutoshss/Robot-Manipulator
#                                                                                        last modified : Jun 8, 2024.
