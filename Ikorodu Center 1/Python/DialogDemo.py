#Aribido Lamzey, 08131089608, lamzey.m@gmail.com
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

window = Tk()
window.title("LAM Operating System")
label = Label(window, text = "LAM Operating System")

tkinter.messagebox.showinfo("LAM Operating System", "New User, Welcome To LAM Operating System")

name = tkinter.simpledialog.askstring("LAM Operating System", "Enter your name")
print(name)

password = tkinter.simpledialog.askstring("LAM Operating System", "Enter your password")
print(password)

question = tkinter.simpledialog.askstring("LAM Operating System", "Would You Love To Speak To Julia?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "How far are you enjoying Code Lagos?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "Are you cool enough for a Python BootCamp?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "Are you enjoying LAM OS?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "How will you rate this Operating System Alongside MAC OS, Linux and Windows?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "Well.... Do you know this Operating System was created by a Deutschlander?")
print(question)

question = tkinter.simpledialog.askstring("LAM Operating System", "Thanks for your adequate time, Below I would like to show you some of our relevant Dialog Box still under work progress")

tkinter.messagebox.showwarning("LAM Operating System", "This is a warning")

ifYes = tkinter.messagebox.askyesno("LAM Operating System", "Continue?")

tkinter.messagebox.showerror("LAM Operating System", "This is an error")

ifOK = tkinter.messagebox.askokcancel("LAM Operating System", "OK?")

ifYesNoCancel = tkinter.messagebox.askyesnocancel("LAM Operating System", "Yes, No, Cancel?")

tkinter.messagebox.showinfo("LAM Operating System", "Thanks For Your Time")

exit (tkinter)
