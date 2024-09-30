#Carlos Martinez Luna
#Exercise 1
import tkinter

root=tkinter.Tk()
root.geometry("240x120")
root.configure(bg="grey")
root.title("Lab 9 Program 1")
#Labels 
label1=tkinter.Label(root, text="My first name is Stu.", font=("arial",18),foreground=("blue4"),background=("light blue"))
label1.pack(padx=0, pady=0)

label2=tkinter.Label(root, text="My Last name is Dent.", font=("arial",18),foreground=("blue4"),background=("light blue"))
label2.pack(padx=0, pady=0)

label3=tkinter.Label(root, text="My faculty is Arts.", font=("arial",18),foreground=("blue4"),background=("light blue"))
label3.pack(padx=0, pady=0)

label4=tkinter.Label(root, text="My year is One.", font=("arial",1),foreground=("blue4"),background=("light blue"))
label4.pack(padx=0, pady=0)



#Exercise 2
root=tkinter.Tk()
root.geometry("400x600")
root.title("Lab 9 Program 2")
#shapes(coords=left, top, right, bottom)
canvas1=tkinter.Canvas(root, width=1920 ,height=1080,background="grey")
canvas1.create_rectangle(50,50,345,540,fill="lime green",width=3,outline="blue")
canvas1.create_oval(160,260,230,330,fill="slate blue", width=3, outline="blue")
#(coords=x1,y1,x2,y2,x3,y3)
canvas1.create_polygon(180,70,180,250,70,250,fill="light blue",width=3,outline="blue")
canvas1.create_polygon(210,70,210,250,325,250,fill="light blue",width=3,outline="blue")
canvas1.create_polygon(180,520,180,340,70,340,fill="light blue",width=3,outline="blue")
canvas1.create_polygon(210,520,210,340,325,340,fill="light blue",width=3,outline="blue")
canvas1.pack()
root.mainloop()