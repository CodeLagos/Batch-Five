"""
AFOLABI SHERIFF OPEYEMI

TECHQUEST CENTRE

PYTHON CLASS: 8:30AM - 10:30AM

07089810339

PROJECT: STANDARD AND SCIENTIFIC CALCULATOR

"""


from tkinter import*
import math
import parser
import tkinter.messagebox 


###################################GIU CODES#################################################################
root = Tk()
root.title("Calculator")
root.config(background="light green")
root.resizable(width=False, height=False)
root.geometry("450x440+0+0")

calculator = Frame(root)
calculator.grid()

class Calculator:
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=textDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self,current=firstnum+secondnum
            self.display(self.current)

    def sum_of_total():
         self.result=True
         self.current= float(self.current)
           
         if self.check_sum==True:
            self.valid_function()
                
         else:
            self.total= float(textDisplay.get())
                

    def display(self, value):
        textDisplay.delete(0, END)
        textDisplay.insert(0, value)


    def valid_function():
        if self.op=="Add":
            self.total+=self.current
        if self.op=="Sub":
            self.total-=self.current
        if self.op=="Mult":
            self.total*=self.current
        if self.op=="Div":
            self.total/=self.current
        if self.op=="Mod":
            self.total%=self.current
        self.input_value= True
        self.check_sum= False
        self.display(self.total)

    def operation(self, op):
        self.current=float(self.current)
        if check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value = True
        self.check_sum= True
        self.op=op
        self.result= False

    def Clear_Entry(self):
        self.result= False
        self.current="0"
        self.display(0)
        self.input_value = True

    
    def allClear_Entry(self):
        self.result= False
        self.current="0"
        self.display(0)
        self.input_value = True
        
    def squared(self):
        self.result= False
        self.current=math.sqrt(float(textDisplay.get()))
        self.display=(self.current)

    def mathPM(self):
        self.result= False
        self.current=~(float(textDisplay.get()))
        self.display=(self.current)
        

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def cos(self):
        self.result= False
        self.current=math.cos(math.radian(float(textDisplay.get())))
        self.display=(self.current)

    def cosh(self):
        self.result= False
        self.current=math.cosh(math.radian(float(textDisplay.get())))
        self.display=(self.current)

    def tan(self):
        self.result= False
        self.current=math.tan(math.radian(float(textDisplay.get())))
        self.display=(self.current)

    def tanh(self):
        self.result= False
        self.current=math.tanh(math.radian(float(textDisplay.get())))
        self.display=(self.current)

    def sin(self):
        self.result= False
        self.current=math.sin(math.radian(float(textDisplay.get())))
        self.display=(self.current)

    def sinh(self):
        self.result= False
        self.current=math.sinh(math.radian(float(textDisplay.get())))
        self.display=(self.current)
            
            
            
            
        

added_value=Calculator()            

textDisplay = Entry(calculator, font= ("arial", 16, "bold"), bd = 20, bg = "light green", width =26, justify = RIGHT)
textDisplay.grid(row=0, column=0, columnspan =3, pady =1)
textDisplay.insert(0, "0")

numpad = "789456123"
i = 0
buttn = []
for j in range(2, 5):
    for k in range(3):
        buttn.append(Button(calculator, width=6, height=2, font= ("arial", 16, "bold"), bd=4, text=numpad[i]))
        buttn[i].grid(row=j, column=k, pady=1)
        buttn[i]["command"]= lambda x = numpad[i]: added_value.numberEnter(x)

        i+=1

buttnClear=Button(calculator, text=chr(67), width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnClear.grid(row=1, column=0, pady=1)


buttnClearAll=Button(calculator, text=chr(67)+ chr(69), width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnClearAll.grid(row=1, column=1, pady=1)

buttnSqrt=Button(calculator, text="√", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnSqrt.grid(row=1, column=2, pady=1)


buttnAdd=Button(calculator, text="+", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green", command= lambda: added_value.opearation("Add"))
buttnAdd.grid(row=1, column=3, pady=1)

buttnSub=Button(calculator, text="-", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green", command= lambda: added_value.opearation("Sub"))
buttnSub.grid(row=2, column=3, pady=1)

buttnMult=Button(calculator, text="*", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green", command= lambda: added_value.opearation("Mult"))
buttnMult.grid(row=3, column=3, pady=1)

buttnDiv=Button(calculator, text=chr(247), width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green", command= lambda: added_value.opearation("Divide"))
buttnDiv.grid(row=4, column=3, pady=1)

buttnZero=Button(calculator, text="0", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green",command= lambda: added_value.numberEnter(0))
buttnZero.grid(row=5, column=0, pady=1)

buttnDot=Button(calculator, text=".", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnDot.grid(row=5, column=1, pady=1)

buttnPM=Button(calculator, text=chr(177), width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green") 
buttnPM.grid(row=5, column=2, pady=1)

buttnEqual=Button(calculator, text="=", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnEqual.grid(row=5, column=3, pady=1)

#################################Scientific Calculator###########################################################

buttnPi=Button(calculator, text="n", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnPi.grid(row=1, column=4, pady=1)

buttnCos=Button(calculator, text="cos", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnCos.grid(row=1, column=5, pady=1)

buttnTan=Button(calculator, text="tan", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnTan.grid(row=1, column=6, pady=1)

buttnSin=Button(calculator, text="sin", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnSin.grid(row=1, column=7, pady=1)

buttn2Pi=Button(calculator, text="2n", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttn2Pi.grid(row=2, column=4, pady=1)

buttnCosh=Button(calculator, text="cosh", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnCosh.grid(row=2, column=5, pady=1)

buttnTanh=Button(calculator, text="tanh", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnTanh.grid(row=2, column=6, pady=1)

buttnSinh=Button(calculator, text="sinh", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnSinh.grid(row=2, column=7, pady=1)

buttnlog=Button(calculator, text="log", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnlog.grid(row=3, column=4, pady=1)

buttnExp=Button(calculator, text="Exp", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnExp.grid(row=3, column=5, pady=1)

buttnMod=Button(calculator, text="Mod", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnMod.grid(row=3, column=6, pady=1)

buttnE=Button(calculator, text="e", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnE.grid(row=3, column=7, pady=1)

buttnlog2=Button(calculator, text="log2", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnlog2.grid(row=4, column=4, pady=1)

buttnDeg=Button(calculator, text="deg", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnDeg.grid(row=4, column=5, pady=1)

buttnacosh=Button(calculator, text="acosh", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnacosh.grid(row=4, column=6, pady=1)

buttnasinh=Button(calculator, text="asinh", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnasinh.grid(row=4, column=7, pady=1)

buttnlog10=Button(calculator, text="log10", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnlog10.grid(row=5, column=4, pady=1)

buttnCos=Button(calculator, text="log1p", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnCos.grid(row=5, column=5, pady=1)

buttnexpm1=Button(calculator, text="expm1", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttnexpm1.grid(row=5, column=6, pady=1)

buttn1gamma=Button(calculator, text="1gamma", width=6, height=2, font= ("arial", 16, "bold"), bd=4, bg = "light green")
buttn1gamma.grid(row=5, column=7, pady=1)


############################################CONNECTING FUNCTIONS##################################################

def Exit():
    Exit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    root.destroy()
    return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("815x428+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x570+0+0")

    
################################Menu#############################################################################
menu = Menu(root)
root.config(menu=menu)

subMenu= Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Standard...", command=Standard)
subMenu.add_command(label="Scientific...", command=Scientific)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=Exit)


editMenu= Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Delete")

helpMenu= Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="ask for help...")
helpMenu.add_command(label="Search")


root.mainloop()
