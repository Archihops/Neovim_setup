# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#Carlos Martinez Luna
#Exercise 1

import tkinter as tk
root=tk.Tk()
root.geometry("500x400")

#responses
def show_responses():
    responses=[]
    for entry in entries:
        response=entry.get()
        responses.append(response)
    response_labels=[]
    for i in range(len(questions)):
        response_label=tk.Label(root, text=f"{answers[i]}{responses[i]}")
        response_label.place(x=250, y=50 + i*30)
        response_labels.append(response_label)
#lists
questions=["Enter a parcel's width: ", "Enter a parcel's height: ", "Enter a parcel's length: ", "Enter a parcel's mass in kg: ",
"How many items are in the package?", "How much is the worth of the parcel? ", "What is the shipping Fee? "]


entries=[]

answers=["The width is ", "The height is ", "The length is ", "The mass is ", "The number of items in the parcel is ", "The worth in the parcel is $ ", "The shipping fee is $ "]
#questions
for i in range(len(questions)):
    question_label=tk.Label(root, text=questions[i])
    question_label.place(x=10, y=10 + i*40)
    entry=tk.Entry(root)
    entry.place(x=10, y=30 + i*40)
    entries.append(entry)
#results button
submit_button=tk.Button(root, text="CLick here to see the results", command=show_responses)
submit_button.place(x=250, y=-205 + len(questions)*30)

root.mainloop()
