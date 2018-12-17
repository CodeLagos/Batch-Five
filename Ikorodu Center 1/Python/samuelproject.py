#Name: Oladele Samuel 
#Project name:Drug prescription app for minor sickness 
#Email address:oladelesameez1@gmail.com
#Mobile number:08105578283 


#welcome the user 
print("welcome to Drug prescription app for minor sickness by sameez")
#ask about how the user feels
q1 = raw_input("How are you feeling? \n (a)Good \n (b)Bad\n").lower()
#if he's good thank him for using the app and close it
if q1=="good":
    print("Thank you for using this app")
#if bad give him/her some list of major sicknesses 
elif q1=="bad":
    q2 = raw_input("what is the sickness?\n(a)head ache\n(b)malaria\n(c)stomach ache\n(d)fever\n(e)conjunctivitis \n")
 #after answering the question you then print the dosage
    if q2=="headache":
        print("Adult:-2 tablet of paracetamol,children:-1 tablet of paracetamol") 
    elif q2 =="stomach ache":
        print("Adult and children:-1 sachet of andrew liver salt")
    elif q2=="malaria":
        print("Coartem (artemether-lumefantrine)\n35 kg or greater: Administer 24 tablets over 3 days; use a 3-day treatment schedule with total of 6 doses\nDay 1: 4 tablets initially and 4 tablets again after 8 hours\nDays 2 & 3: 4 tablets BID (morning & evening)")
    elif q2=="fever":
        print("Adults and children over 12years: IBUPROFEN 200mg-400mg (10-20ml), up to three times a day as required.Leave at least four hours between doses and do not take more than 1200mg (60ml) in any 24 hour period\nchildren:For pain and fever - 20mg/kg/day in divided doses")
    elif q2=="conjunctivitis":
        print("Apply one to two drops of LOTEMAX into the conjunctival sac of the affected eye four times daily.")
print("if you can't find your sickness(disease) or symptoms persist,please visit the doctor")
print("Thank you for using this program")
        
        
        
    

 
