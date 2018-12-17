print ('form a word from CPUDIE \n')
answer=['cup','pie','die','cupid','dupe','dip','epic','up','pic']
score=0
for i in range(7):
    question=input('supply a word:  \n')
    if question.lower() in answer:
        print('correct')
        score+=1
    else:
        print('this is a wrong word \n')
print ('you got',score,'points')
