import tkinter 

root=tkinter.Tk()
root.geometry("500x500")
root.title("My first GUI")
root.background("black")
label=tkinter.Label(root, text="hello world", font=("arial",18))
label.pack(padx=20, pady=60)

mycanvas=tkinter.Canvas(root, width=300, height=300, bg="black")
mycanvas.pack(padx=20, pady=10)


root.mainloop()
