from tkinter import*
import math
master=Tk()
def self():
  self.printme()
def printme(self):
  print("Code in action")  

    
def getandreplace(self):

  self.expression = self.e.get()
  self.newtext=self.experession.replace(self.newdiv,"/")
  self.newtext=self.newtext.replace("x","*")
def equals(self):
  self.getandreplace()
  try:
   self.value= eval(self.newtext)
  except SyntaxError or NameError:
   self.e.delete(0,END)
   self.e.insert(0,"Invalid input!")
  else:
   self.e.delete(0,END)
   self.e.insert(0,self.value)

def squareroot(self):
   self.getandreplace()
   try:
    self.value= eval(self.newtext)
   except SyntaxError or NameError:
    self.e.delete(0,END)
    self.e.insert(0,"Invalid input!")
   else:
    self.sqrtval=math.sqrt(self.value)
    self.e.delete(0,END)
    self.e.insert(0,self.sqrtval)
def square(self):
   self.getandreplace()
   try:
    self.value= eval(self.newtext)
   except SyntaxError or NameError:
    self.e.delete(0,END)
    self.e.insert(0,"Invalid input!")
   else:
    self.sqval=math.pow(self.value,2)
    self.e.delete(0,END)
    self.e.insert(0,self.sqval)
def clearall(self):
   self.e.delete(0,END)
def clear(self):
   self.txt=self.e.get()[:-1]
   self.e.delete(0,END)
   self.e.insert(0,self.txt)
def action(self,args):
   self.e.insert(END,args)
def _init_(self,master):   
   master.title("Calculator")
   master.geometry()
   self.e = Entry(master)
   self.e.grid(row=0,column=0,columnspan=6,pady=3)
   self.e.focus_set()

   self.div="÷"
   self.newdiv=self.div.decode("utf-8")

screen = Entry(master,bd=30,justify=RIGHT,font=("Ariel",20,"bold"),width=20,bg="powder blue")
screen.insert(0,"0")
screen.grid(pady=5,columnspan=7)


  




btn1 = Button(master,text="1",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(1))
btn1.grid (row=1,column=0)             

btn2 = Button(master,text="2",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(2))
btn2.grid (row=1,column=1)             

btn3 = Button(master,text="3",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(3))
btn3.grid (row=1,column=2)             

btn4 = Button(master,text="4",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(4))
btn4.grid (row=2,column=0)             

btn5 = Button(master,text="5",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(5))
btn5.grid (row=2,column=1)             

btn6 = Button(master,text="6",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(6))
btn6.grid (row=2,column=2)             

btn7 = Button(master,text="7",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(7))
btn7.grid (row=3,column=0)             

btn8 = Button(master,text="8",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(8))
btn8.grid (row=3,column=1)             

btn9 = Button(master,text="9",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(9))
btn9.grid (row=3,column=2)             

btn0 = Button(master,text="0",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(0))
btn0.grid (row=4,column=1)

btnadd = Button(master,text="+",font=("Ariel",20,"bold"),width=5,height=3,bg="pink",command=lambda:self.action("+"))
btnadd.grid (row=5,column=2,rowspan=2)

btnsubtract = Button(master,text="-",font=("Ariel",20,"bold"),width=5,height=1,bg="grey",command=lambda:self.action("-"))
btnsubtract.grid (row=5,column=0)

btndivide = Button(master,text="/",font=("Ariel",20,"bold"),width=5,height=1,bg="grey",command=lambda:self.action(self.newdiv))
btndivide.grid (row=5,column=1)             

btnmultiply = Button(master,text="*",font=("Ariel",20,"bold"),width=5,height=1,bg="grey",command=lambda:self.action("x"))
btnmultiply.grid (row=6,column=0)

btndecimal = Button(master,text=".",font=("Ariel",20,"bold"),width=5,height=1,bg="grey",command=lambda:self.action("."))
btndecimal.grid (row=6,column=1)

btnsqrt = Button(master,text="√",font=("Ariel",20,"bold"),width=5,height=1,bg="yellow",command=lambda:self.squareroot())
btnsqrt.grid (row=1,column=3)

btnsq = Button(master,text="X^2",font=("Ariel",20,"bold"),width=5,height=1,bg="yellow",command=lambda:self.square())
btnsq.grid (row=2,column=3)

ClearAll = Button(master,text="CE",font=("Ariel",20,"bold"),width=5,height=1,bg="powder blue",command=lambda:self.clearall())
ClearAll.grid (row=4,column=0)             

Clear = Button(master,text="C",font=("Ariel",20,"bold"),width=5,height=1,bg="powder blue",command=lambda:self.clear())
Clear.grid (row=4,column=2)

btnequalto = Button(master,text="=",font=("Ariel",20,"bold"),width=5,height=1,bg="yellow",command=lambda:self.equals())
btnequalto.grid (row=3,column=3)


btnbrao =  Button(master,text="(",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action("("))
btnbrao.grid (row=5,column=3)


btnbrac = Button(master,text=")",font=("Ariel",20,"bold"),width=5,height=1,bg="purple",fg="yellow",command=lambda:self.action(")"))
btnbrac.grid (row=6,column=3)

master.mainloop()
