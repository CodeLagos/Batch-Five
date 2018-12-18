
print("OFFLINE EXAM WITH NEGATIVE MARKING FOR SCHOOL IN GUI FORM USING TKINTER")
print("BY SARUMOH SEUN HABIB")
    
Name=input("What is your name ? ")
print("Hi  "+Name)


from tkinter import *

root= Tk()

score=0
Answer=input(root)

def giveanswer1():
        if(Answer==cbutton1c):
            print("Correct!")
            score=score+1
        elif(Answer==cbutton1e):
            print("Next Question")
            score=score
        else:
            print("Wrong!")
            score=score-1


def giveanswer2():
        if(Answer==cbutton2d):
            print("Correct!")
            score=score+1
        elif(Answer==cbutton2e):
            print("Next Question")
            score=score
        else:
            print("Wrong!")
            score=score-1


def giveanswer3():
        if(Answer==cbutton3a):
            print("Correct!")
            score=score+1
        elif(Answer==cbutton3e):
            print("Next Question")
            score=score
        else:
            print("Wrong!")
            score=score-1


def finalanswer(event):
    print("Total Score "+str(score) +"/3")


#Labels

label_1 = Label(root, text="1. Who won the 2018 FIFA world cup")
label_2 = Label(root, text="2. Who is Nigeria's present President?")
label_3 = Label(root, text="3. When did Nigeria change from left  to right?")


label_1.grid(row=0, sticky=W)
label_2.grid(row=30, sticky=W)
label_3.grid(row=60, sticky=W)






#checkbuttons

#checkbuttons Q1
cbutton1a = Checkbutton(root, text="Brazil", command=giveanswer1)
cbutton1b = Checkbutton(root, text="England", command=giveanswer1)
cbutton1c = Checkbutton(root, text="France", command=giveanswer1)
cbutton1d = Checkbutton(root, text="Nigeria", command=giveanswer1)
cbutton1e = Checkbutton(root, text="Skip", command=giveanswer1)

cbutton1a.grid(row=0,column=2)
cbutton1b.grid(row=0,column=3)
cbutton1c.grid(row=0,column=4)
cbutton1d.grid(row=0,column=5)
cbutton1e.grid(row=0,column=6)


#checkbuttons Q2
cbutton2a = Checkbutton(root, text="Tony Aneneh", command=giveanswer2)
cbutton2b = Checkbutton(root, text="Adams Oshiomole", command=giveanswer2)
cbutton2c = Checkbutton(root, text="Tijani Babayaro", command=giveanswer2)
cbutton2d = Checkbutton(root, text="Mohamadu Buhari", command=giveanswer2)
cbutton2e = Checkbutton(root, text="Skip", command=giveanswer2)

cbutton2a.grid(row=30,column=2)
cbutton2b.grid(row=30,column=3)
cbutton2c.grid(row=30,column=4)
cbutton2d.grid(row=30,column=5)
cbutton2e.grid(row=30,column=6)

#checkbuttons Q3
cbutton3a = Checkbutton(root, text="1972", command=giveanswer3)
cbutton3b = Checkbutton(root, text="1954", command=giveanswer3)
cbutton3c = Checkbutton(root, text="1942", command=giveanswer3)
cbutton3d = Checkbutton(root, text="1988", command=giveanswer3)
cbutton3e = Checkbutton(root, text="Skip", command=giveanswer3)

cbutton3a.grid(row=60,column=2)
cbutton3b.grid(row=60,column=3)
cbutton3c.grid(row=60,column=4)
cbutton3d.grid(row=60,column=5)
cbutton3e.grid(row=60,column=6)


#Buttons

#buttons Q1
Answer_final = Button(root, text="Compute Result", command=finalanswer)

Answer_final.grid(row=90,column=2)



root.mainloop()
     
