#This GUI is simple calculator that computes basic arithmetic operations

import tkinter as tk

#Other ways of importing tkinter
#import tkinter
#from tkinter import

import math

#Code for the real code starts here

def Multiply():
	print("Code in action")
	r = float(formR.get())
	h = float(formH.get())
	product = r*h
	product = round(product,3)
	print(product)

	resultshow = "Answer: " + str(product)
	resultS.config(state = "normal")
	resultS.delete(1.0, tk.END)
	resultS.insert(tk.INSERT, resultshow)
	resultS.config(state = "disabled")

def Addition():
	print("Code in action")
	r = float(formR.get())
	h = float(formH.get())
	add = r+h
	add = round(add,3)
	print(add)

	resultshow = "Answer: " + str(add)
	resultS.config(state = "normal")
	resultS.delete(1.0, tk.END)
	resultS.insert(tk.INSERT, resultshow)
	resultS.config(state = "disabled")

def Division():
	print("Code in action")
	r = float(formR.get())
	h = float(formH.get())
	divide = r/h
	divide = round(divide,3)
	print(divide)

	resultshow = "Answer: " + str(divide)
	resultS.config(state = "normal")
	resultS.delete(1.0, tk.END)
	resultS.insert(tk.INSERT, resultshow)
	resultS.config(state = "disabled")



#Code for the GUI starts here
root = tk.Tk()
root.title("Simple Calculator")
nameR = tk.Label(root, text = "Number1", fg = "red")
nameR.pack()


formR = tk.Entry(root)
formR.pack()

nameH = tk.Label(root, text = "Number2", fg = "red")
nameH.pack()

formH = tk.Entry(root)
formH.pack()


multiply = tk.Button(root, text = "x", bg = "grey", width = 3, command = Multiply)
multiply.pack(pady = 3)

addition = tk.Button(root, text = "+", bg = "grey", width = 3, command = Addition)
addition.pack(pady = 3)

division = tk.Button(root, text = "/", bg = "grey", width = 3, command = Division)
division.pack(pady = 3)



resultS = tk.Text(root, width = 50, height =10, borderwidth = 5, bg = "brown" )
resultS.pack()
resultS.config(state="disabled")

root.mainloop()


#Three display managers in tkinter
#1. Pack
#2. Grid
#3. Place

#The GUI code ends here
