'''
#Aremu Abdullah
#Bmi_calculator and Calculator of multiples between a particular range
#08120668818
#Codelagosbatch 5

#define name1, height1, and weight1 
name1 = "john"
height1_m = 3
weight1_kg = 90

#define name2, height2, and weight2
name2 = "Micheal"
height2_m = 2
weight2_kg = 60

#define name3, height3, and weight3
name3 = "joseph"
height3_m = 3
weight3_kg = 40

#define the function bmi_calculator with the arguments name, height and weight 
def bmi_calculator(name, height_m, weight_kg):
    
#process bmi = weight in kg divided by height in meter squared
    bmi = weight_kg/ (height_m **2)
    
#print bmi
    print("bmi")
    print(bmi)
    
#if bmi is greater than 10, return name plus "is overweight"
    if (bmi > 10):
        return (name) + " is overweight"
    
#if bmi is equal to 10, return name plus "has normal weight"
    elif (bmi == 10):
        return (name) + " has normal weight"
    
#otherwise, return name plus"is underweight"
    else:
        return (name) + " is underweight"
    
#call the function with result1, result2 and result 3
result1 = bmi_calculator(name1, height1_m, weight1_kg)
result2 = bmi_calculator(name2, height2_m, weight2_kg)
result3 = bmi_calculator(name3, height3_m, weight3_kg)

#print results 1, 2 and 3
print(result1)
print(result2)
print(result3)


'''

#to add multiples of numbers within a particular range

#let e equal list of ranges between 1 and 5000
#print e

#for i in range (1,5000), print i


#assign total to zero
#for i in range (1, 5000), if i modulo 3,5,6,7,8,9 and 10 = 0,then
#write a new total to equal former total plus i
#print total

e = list (range(1, 5000))
print(e)

         

for i in range (1, 5000):
    print(i)


total = 0
         
for i in range (1, 5000):
         if i % 3 + i % 5 + i % 6 + i % 7 + i % 8 + i % 9 + i % 10 == 0:
         

             total = total + i
         

print(total)
         
    
         

            
        

