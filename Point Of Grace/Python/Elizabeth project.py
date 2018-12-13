                    #ADEWUNMI ELIZABETH
#A Bio data Project With BMI

print('Personal Profile')

surname = input('Enter surname: ')
first_name = input('Enter first name: ')
middle_name = input('Enter middle name: ')
date_of_birth = input('Enter date of birth: ')
sex = input('Enter sex: ')
complexion =input('Enter complexion:')
hobbies = ('Enter hobbies')
nationality = input('Enter nationality: ')
state_of_origin = input('Enter state of origin: ')
local_government_area = input('Enter local government area: ')
religion = input('Enter religiion: ')
address = input('Enter address: ')
phone_number = int(input('Enter phone number: '))
mobile_number = int(input('Enter mobile number: '))
email = input('Enter email: ')
education = ('Enter education: ')
profession = ('Enter profession: ')
marital_status = input('Enter marital status: ')
genotype = input('Enter genotype: ')
blood_group = input('Enter blood group: ')

#DISPLAY THE PURPOSE THE PROGRAM
print('THIS IS A BMI CALCULATOR')
print('********************************************')
print('Please enter Your Weight In kIlogram And Your Height In Metres')
weight = float(input('Please enter your weight: '))
height = float(input('Please enter your height: '))
bmi = weight / (height**2)
bmi_round = round(bmi, 1)
print('%s Is Your BMI' % bmi_round)
if (bmi_round < 18.5):
    print('Under Weight')
elif ((bmi_round >= 18.5) and (bmi < 25)):
    print('Normal')
elif ((bmi_round >= 25) and (bmi < 30)):
    print('Over Weight')

else:
    print('Obese')
