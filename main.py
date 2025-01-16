#import libraries
from os.path import isfile,join
from os import *
from tkinter import *
from pso import Particle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#window configuration
root = Tk() 
root.geometry("700x600") #Width x Height
root.minsize(300,600)
root.configure(background='#ed0fcf')

#Labels
l1=Label(root,text="Minimum value for X")
l1.place(x=0,y=30)
l1.config(width=20,height=1,font=("Times New Roman",11))

l2=Label(root,text="Minimum value for Y")
l2.place(x=0,y=50)
l2.config(width=20,height=1,font=("Times New Roman",11))


l3=Label(root,text="Maximum value for X")
l3.place(x=300,y=30)
l3.config(width=20,height=1,font=("Times New Roman",11))

l4=Label(root,text="Maximum value for Y")
l4.place(x=300,y=50)
l4.config(width=20,height=1,font=("Times New Roman",11))

l5=Label(root,text="Population Size")
l5.place(x=0,y=80)
l5.config(width=20,height=1,font=("Times New Roman",11))

l6=Label(root,text="Maximum Iteration")
l6.place(x=0,y=100)
l6.config(width=20,height=1,font=("Times New Roman",11))

l7=Label(root,text="Specify Function to Evaluate")
l7.place(x=0,y=130)
l7.config(width=20,height=1,font=("Times New Roman",11))

#GUI Text 
text1 = Text(root)
text1.insert(INSERT,"0")
text1.config(width=10,height=1,font=("Times New Roman",11))
text1.place(x=170,y=30)

text2 = Text(root)
text2.insert(INSERT,"0")
text2.config(width=10,height=1,font=("Times New Roman",11))
text2.place(x=170,y=50)

text3 = Text(root)
text3.insert(INSERT,"1000")
text3.config(width=10,height=1,font=("Times New Roman",11))
text3.place(x=470,y=30)

text4 = Text(root)
text4.insert(INSERT,"1000")
text4.config(width=10,height=1,font=("Times New Roman",11))
text4.place(x=470,y=50)

text5 = Text(root)
text5.insert(INSERT,"20")
text5.config(width=10,height=1,font=("Times New Roman",11))
text5.place(x=170,y=80)

text6 = Text(root)
text6.insert(INSERT,"20")
text6.config(width=10,height=1,font=("Times New Roman",11))
text6.place(x=170,y=100)

#Dropdown
variable=StringVar(root)
variable.set("Ackley")

opt=OptionMenu(root, variable, "Ackley","Booth","Matyas","Himmelblau","Beale")
opt.config(width=20,height=1,font=("Times New Roman",10))
opt.place(x=170,y=130)

#Graph
root.figure=plt.Figure(figsize=(6,4) ,dpi=100)
root.fig1= FigureCanvasTkAgg(root.figure,root)
root.fig1.get_tk_widget().pack(side=BOTTOM)

#CallBack Function
def CallBack():
        XMIN=float(text1.get("1.0","end-1c"))
        YMIN=float(text2.get("1.0","end-1c"))
        XMAX=float(text3.get("1.0","end-1c"))
        YMAX=float(text4.get("1.0","end-1c"))
        POP=int(text5.get("1.0","end-1c"))
        maxiter=int(text6.get("1.0","end-1c"))
        
        option= (["Ackley","Booth","Matyas","Himmelblau","Beale"]).index(variable.get())
        particles=Particle(POP,option,XMIN,YMIN,XMAX,YMAX)
        particles.run_simulation(maxiter,POP,option,XMIN,YMIN,XMAX,YMAX,root)
        
        
#Simulation Button                
B = Button(root, text = "run simulation", command = CallBack)
B.place(x=50,y=170)
B.config(width=20,height=1)

root,mainloop()
