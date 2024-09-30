#Carlos Martinez Luna
#Exercise 1

import tkinter as tk
root=tk.Tk()
root.title("Grams Converter")
root.geometry("300x200")

#convertions
def convert_to_ounces():
    grams=float(entry.get())
    result=grams*0.0353
    result_label.config(text=str(result))
    result_label1.config(text="Ounces=")
    result_label1.place(x=10, y=170)
def convert_to_pounds():
    grams=float(entry.get())
    result=grams*0.00221
    result_label.config(text=str(result))
    result_label1.config(text="Pounds=")
def convert_to_kilograms():
    grams=float(entry.get())
    result=grams*0.001
    result_label.config(text=str(result))
    result_label1.config(text="Kilograms=")
#label
instructions_label=tk.Label(root, text="Enter grams: ")
instructions_label.place(x=10, y=10)

entry=tk.Entry(root)
entry.place(x=85, y=10)

mass_label=tk.Label(root, text="Choose:")
mass_label.place(x=10, y=60)
#buttons
ounces_button=tk.Button(root, text="Ounces", command=convert_to_ounces)
ounces_button.place(x=10, y=80)

pounds_button=tk.Button(root, text="Pounds", command=convert_to_pounds)
pounds_button.place(x=70, y=80)

kilograms_button=tk.Button(root, text="Kilograms", command=convert_to_kilograms)
kilograms_button.place(x=130, y=80)
#result
result_label1=tk.Label(root, text="result= ")
result_label1.place(x=10, y=170)
result_label=tk.Label(root, text="")
result_label.place(x=75, y=170)

root.mainloop()