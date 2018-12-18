print("Elizabeth Dooter Ohaka")
print("lizzemonline@yahoo.com")

print("The purpose of the programme is to detect the learning stlye of each pupil. There by ascertaining the total percentage of each style present in the classroom so that (1) specific learning experiences are provided to suite the interests of the learners (2). Differentiated learning based more on empirical evidence can take place.(3). Appropriate choice of after-school and co-curricular activities can be made.")


print("\n Welcome To Learning Style Detector")
name = input("Name: ")
print('\n Hi ' + name )
print('\n------------\n')
score = 0
score = int(score)
print("Section A")
print("Q1. Does the pupil make an effort to keep his/her environment orderly?")
print("A. Yes")
print("B. No")
Q1Response = input('Your answer: ')

if (Q1Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q2. Does the pupil enjoy making use of worksheets?")
print("A. Yes")
print("B. No")
Q2Response = input('Your answer: ')

if (Q2Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q3. Does he/she enjoy looking at or creating pictures?")
print("A. Yes")
print("B. No")
Q3Response = input('Your answer: ')

if (Q3Response == "A"): 
    score = score + 1
else:
    score = score - 1
print("Q4. Is the pupil attentive to visual cues and details?")
print("A. Yes")
print("B. No")
Q4Response = input('Your answer: ')

if (Q4Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q5. Do his/her eyes follow the teacher around during lessons?")
print("A. Yes")
print("B. No")
Q5Response = input('Your answer: ')

if (Q5Response == "A"):
    score = score + 1
else:
    score = score - 1
a_score = score



print('\n------------\n')
score = 0
score = int(score)
print("Section B")
print("Q1. Does the pupil readily participate in singing exercises?")
print("A. Yes")
print("B. No")
Q1Response = input('Your answer: ')

if (Q1Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q2. Does the pupil repeat the words of the teacher to himself/herself?")
print("A. Yes")
print("B. No")
Q2Response = input('Your answer: ')

if (Q2Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q3. Does the pupil nod to show understanding and agreement during lessons?")
print("A. Yes")
print("B. No")
Q3Response = input('Your answer: ')

if (Q3Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q4. Does he/she read aloud?")
print("A. Yes")
print("B. No")
Q4Response = input('Your answer: ')

if (Q4Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q5. Does the pupil like to talk to himself/herself?")
print("A. Yes")
print("B. No")
Q5Response = input('Your answer: ')

if (Q5Response == "A"):
    score = score + 1
else:
    score = score - 1
b_score = score

print('\n------------\n')
score = 0
score = int(score)
print("Section C")
print("Q1. Does he/she fiddle with objects during lessons?")
print("A. Yes")
print("B. No")
Q1Response = input('Your answer: ')

if (Q1Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q2. Is the pupil good at sports/dancing?")
print("A. Yes")
print("B. No")
Q2Response = input('Your answer: ')

if (Q2Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q3. Does the pupil use his/her hands to demonstrate while speaking?")
print("A. Yes")
print("B. No")
Q3Response = input('Your answer: ')

if (Q3Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q4. Does the pupil like to take things apart?")
print("A. Yes")
print("B. No")
Q4Response = input('Your answer: ')

if (Q4Response == "A"):
    score = score + 1
else:
    score = score - 1
print("Q5. Does he/she find it difficult to sit still?")
print("A. Yes")
print("B. No")
Q5Response = input('Your answer: ')

if (Q5Response == "A"):
    score = score + 1
else:
    score = score - 1
c_score = score
print('\n------------\n')
if (a_score >= b_score >= c_score):
    print(name + " you are a visual learner")
elif (b_score >= a_score >= c_score):
    print(name + "you are an auditory learner")
elif (c_score >= a_score >= b_score):
    print(name + "you are a kinesthetic learner")
else:
    print("Please retake the test")


    


