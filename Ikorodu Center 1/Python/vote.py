#oke anu
#08106008841 okeanuoluwa35@gmail.com
import sys # this import the system modules
print("welcome to the poll unit")#prints a welcome message

candidate1=input("input the first candidates name\n") #ask user for the first candidate
candidate2=input("input the second candidate name\n")#ask user for the second candidate
vote1 =0 #initialise the votinig varaibles
vote2=0
print('How old are you')
while True:#initializing a loop for new
    print("how old are you: ") #ask user how old they are
    age=int(input())
    if age <= 18 :#allows user to continue if above or is 18
        continue
    print('welcome')
    while True:
        print('who do want to vote for.\n for' ,candidate1,'press 1','for',candidate2,'press2','to collate result press exit')
        voted =input()
        if voted == '1':
            vote1+=1
            break
        elif voted == '2':
            print(candidate2)
            vote2+=1
            break
        elif voted=='exit':
            print(candidate1,vote1,candidate2,vote2)
            sys.exit()
        
    
    
    
    

    
    
        

