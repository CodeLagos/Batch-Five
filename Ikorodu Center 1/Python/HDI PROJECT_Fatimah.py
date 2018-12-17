#Display the purpose of the program
import math
print("HDI CHECK/CALCULATOR ANALYSIS")
#HDI CALCULATOR AND ANALYSIS  DONE BY TAIWO, FATIMOH OLAJUMOKE. CODELAGOS BATCH 5.0 PYTHON PROGRAMING CLASS, IKORODU MAIN CENTRE,
#contact 08168110033
#fatimohtaiwo999@gmail.com
#Human Development Index (HDI)is a summary measure of average achievement in key aspect of human development which are also known to be tha basic indicator,namely; life expectancy,education index and income index  
#REFERRENCE The data useD in this project are gotten directly from the UNDP website
def callagain():
    if (HDI<0.50):
       print("this indicate that the above named country/state/city has a low percentile,therefore has a poor economy and high poverty level")
    elif(HDI>=0.50)and (HDI<=0.69):
        print("this indicate that the above named country/state/city has a medium percentile,therefore has a deveoping economy and less poverty levelmedium")
    elif(HDI>=0.70)and (HDI<=0.79):
        print("this indicate that the above named country/state/city has a high percentile,therefore has a developed economy and with lesser poverty level")
    else:
        print("this indicate that the above named country/state/city has a very high percentile,therefore has a developed economy, high mass consumption and least poverty level")
    Restart = (input('would you like to check another country HDI? input yes or no\n'))
    if Restart in('y','YES','yes','Y'):
        print("proceed")
    else:
        print("cancel")
        exit()
while True:
          OPTION = (input("which continent would like to choose from? \na)North America.\nb)South America.\nc)Europe.\nd)Asia.\ne)Africa.\nf)Australia.\ng)input a preferred country/state/city\n"))
          if(OPTION == "a"):
              North_America = (input(" available North America countries are : \na)The United States.\nb)Canada.\nc)Puerto Rico.\nd)Trinidad and Tobago.\ne)Haiti\n"))
              if(North_America == "a"):
                 print("united state")
                  
                 life_exp = float("0.92")
                 edu_index = float("0.90")
                 living_standard = float("0.95")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("USA HDI is:",HDI)
                 callagain() 
              elif(North_America == "b"):
                 print("canada")
                  
                 life_exp = float("0.96")
                 edu_index = float("0.90")
                 living_standard = float("0.92")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("canada HDI is:",HDI)
                 callagain()
              elif(North_America == "c"):
                 print("Puerto Rico")
                  
                 life_exp = float("0.92")
                 edu_index = float("0.83")
                 living_standard = float("0.79")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Puerto Rico HDI is:",HDI)
                 callagain()
              elif(North_America == "d"):
                 print("Trinidad and Tobago")
                  
                 life_exp = float("0.78")
                 edu_index = float("0.72")
                 living_standard = float("0.85")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Trinidad and Tobago HDI is:",HDI)
                 callagain()
              else:
                 (North_America == "e")
                 print("Haiti")
                  
                 life_exp = float("0.67")
                 edu_index = float("0.43")
                 living_standard = float("0.42")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("HAITI HDI is:",HDI)
                 callagain()
          elif(OPTION == "b"):
              South_America = (input(" available South American countries are : \na)Brazil\.\nb)Argentina.\nc)Bolivia.\nd)Columbia.\ne)Guyana\n"))
              if(South_America == "a"):
                 print("Brazil")
                  
                 life_exp = float("0.86")
                 edu_index = float("0.69")
                 living_standard = float("0.74")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Brazil HDI is:",HDI)
                 callagain()
              elif(South_America == "b"):
                 print("Argentina")
                  
                 life_exp = float("0.87")
                 edu_index = float("0.81")
                 living_standard = float("0.79")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Argentina HDI is:",HDI)
                 callagain()
              elif(South_America == "c"):
                 print("Bolivia")
                  
                 life_exp = float("0.76")
                 edu_index = float("0.69")
                 living_standard = float("0.64")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Bolivia HDI is:",HDI)
                 callagain()
              elif(South_America == "d"):
                 print("Columbia")
                  
                 life_exp = float("0.84")
                 edu_index = float("0.68")
                 living_standard = float("0.73")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Columbia HDI is:",HDI)
                 callagain()
              else:
                 (South_America == "e")
                 print("Guyana")
                  
                 life_exp = float("0.72")
                 edu_index = float("0.59")
                 living_standard = float("0.65")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Guyana HDI is:",HDI)
                 callagain()
          elif(OPTION == "c"):
              Europe = (input(" available European countries are : \na)France\.\nb)Ukraine.\nc)Malta.\nd)Turkey.\ne)Moldova\n"))
              if(Europe == "a"):
                 print("France")
                  
                 life_exp = float("0.97")
                 edu_index = float("0.84")
                 living_standard = float("0.90")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("France HDI is:",HDI)
                 callagain()
              elif(Europe == "b"):
                 print("Ukraine")
                  
                 life_exp = float("0.80")
                 edu_index = float("0.79")
                 living_standard = float("0.66")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Ukraine HDI is:",HDI)
                 callagain()
              elif(Europe == "c"):
                 print("Malta")
                  
                 life_exp = float("0.94")
                 edu_index = float("0.82")
                 living_standard = float("0.88")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Malta is:",HDI)
                 callagain()
              elif(Europe == "d"):
                 print("Turkey")
                  
                 life_exp = float("0.84")
                 edu_index = float("0.68")
                 living_standard = float("0.73")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Turkey HDI is:",HDI)
                 callagain()
              else:
                 (Europe == "e")
                 print("Moldova")
                  
                 life_exp = float("0.80")
                 edu_index = float("0.71")
                 living_standard = float("0.61")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Moldova HDI is:",HDI)
                 callagain()   
          elif(OPTION == "d"):
              Asia = (input(" available Asian countries are : \na)Phillippines.\nb)Saudi Arabia.\nc)Singapore.\nd)Afghanistan.\ne)Nepal\n"))
              if(Asia == "a"):
                 print("Phillippines")
                  
                 life_exp = float("0.76")
                 edu_index = float("0.66")
                 living_standard = float("0.68")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Phillippines HDI is:",HDI)
                 callagain()
              elif(Asia == "b"):
                 print("Saudi Arabia")
                  
                 life_exp = float("0.84")
                 edu_index = float("0.79")
                 living_standard = float("0.94")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Saudi Arabia HDI is:",HDI)
                 callagain()
              elif(Asia == "c"):
                 print("Singapore")
                  
                 life_exp = float("0.97")
                 edu_index = float("0.83")
                 living_standard = float("1.00")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Singapore is:",HDI)
                 callagain()
              elif(Asia == "d"):
                 print("Afghanistan")
                  
                 life_exp = float("0.68")
                 edu_index = float("0.42")
                 living_standard = float("0.44")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Afghanistan HDI is:",HDI)
                 callagain()
              else:
                 (Asia == "e")
                 print("Nepal")
                  
                 life_exp = float("0.78")
                 edu_index = float("0.50")
                 living_standard = float("0.48")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Nepal HDI is:",HDI)
                 callagain() 
          elif(OPTION == "e"):
              Africa = (input(" available African countries are : \na)Seychelles.\nb)Liberia.\nc)Ethopia.\nd)Gabon.\ne)Nigeria\n"))
              if(Africa == "a"):
                 print("Seychelles")
                  
                 life_exp = float("0.83")
                 edu_index = float("0.73")
                 living_standard = float("0.84")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Seychelles HDI is:",HDI)
                 callagain()
              elif(Africa == "b"):
                 print("Liberia")
                  
                 life_exp = float("0.66")
                 edu_index = float("0.43")
                 living_standard = float("0.29")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Liberia HDI is:",HDI)
                 callagain()
              elif(Africa == "c"):
                 print("Ethopia")
                  
                 life_exp = float("0.71")
                 edu_index = float("0.33")
                 living_standard = float("0.43")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Ethopia is:",HDI)
                 callagain()
              elif(Africa == "d"):
                 print("Gabon")
                  
                 life_exp = float("0.72")
                 edu_index = float("0.63")
                 living_standard = float("0.77")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Gabon HDI is:",HDI)
                 callagain()
              else:
                 (Africa == "e")
                 print("Nigeria")
                  
                 life_exp = float("0.52")
                 edu_index = float("0.48")
                 living_standard = float("0.59")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Nigeria HDI is:",HDI)
                 callagain()
          elif(OPTION == "f"):
              Australia = (input(" available  Australia countries are : \na) Australia.\nb)Kiribati.\nc)Fiji.\nd)Papau New Guinea.\ne)Vanuata\n"))
              if(Australia == "a"):
                 print(" Australia")
                  
                 life_exp = float("0.97")
                 edu_index = float("0.93")
                 living_standard = float("0.92")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print(" Australia HDI is:",HDI)
                 callagain()
              elif(Australia == "b"):
                 print("Kiribati")
                  
                 life_exp = float("0.72")
                 edu_index = float("0.62")
                 living_standard = float("0.52")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Kiribati HDI is:",HDI)
                 callagain()
              elif(Australia == "c"):
                 print("Fiji")
                  
                 life_exp = float("0.78")
                 edu_index = float("0.79")
                 living_standard = float("0.67")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Fiji is:",HDI)
                 callagain()
              elif(Australia == "d"):
                 print("Papau New Guinea")
                  
                 life_exp = float("0.70")
                 edu_index = float("0.43")
                 living_standard = float("0.53")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Papau New Guinea HDI is:",HDI)
                 callagain()
              else:
                 (Australia == "e")
                 print("Vanuata")
                  
                 life_exp = float("0.81")
                 edu_index = float("0.53")
                 living_standard = float("0.51")
                 hdi = life_exp * edu_index * living_standard
                 HDI = pow(hdi,0.33)
                 HDI = round(HDI,2)
                 print("Vanuata HDI is:",HDI)
                 if (HDI<0.50):
                   print("this indicate that the above named country/state/city has a low percentile,therefore has a poor economy and high poverty level")
                 elif(HDI>=0.50)and (HDI<=0.69):
                     print("this indicate that the above named country/state/city has a medium percentile,therefore has a deveoping economy and less poverty levelmedium")
                 elif(HDI>=0.70)and (HDI<=0.79):
                     print("this indicate that the above named country/state/city has a high percentile,therefore has a developed economy and with lesser poverty level")
                 else:
                     print("this indicate that the above named country/state/city has a very high percentile,therefore has a developed economy, high mass consumption and least poverty level")
                 Restart = (input('would you like to check another country HDI? input yes or no\n'))
                 if Restart in('y','YES','yes','Y'):
                   print("proceed")
                 else:
                     print("cancel")
                     exit()
          elif(OPTION == "g"):
                country_state_community = (input("enter the preferred country,state or community which HDI is to be calculated: ")) 
                #life expectancy as the health indicator
                #actual value of life expectancy is the estmated value gotten from the research carried out in the health sector to get the life expectancy at birth 
                print("life expectancy at birth")
                actual_value = int(input("enter the actual value: "))
                minimum_value =int("20")
                maximum_value =int("85")
                 
                life_exp =(actual_value - minimum_value)/(maximum_value - minimum_value)
                life_exp = round(life_exp,2)
                print("life_exp:",life_exp)
                #knowledge as an eductation indicator for expected year of schooling
                print("expected year of schooling")
                exp_value = int(input("enter the actual value: "))
                minimum_value =int("0")
                maximum_value =int("18")
                edu_exp =(exp_value - minimum_value)/(maximum_value - minimum_value)
                edu_exp = round(edu_exp,2)
                print("edu_exp:",edu_exp)
                #knowledge as an eductation indicator for mean year of schooling
                print("mean year of schooling")
                mean_value = int(input("enter the actual value: "))
                minimum_value =int("0")
                maximum_value =int("15")
                edu_mean =(mean_value - minimum_value)/(maximum_value - minimum_value)
                edu_mean = round(edu_mean,2)
                print("edu_mean:",edu_mean)
                edu_index = (edu_exp + edu_mean)/2
                edu_index = round(edu_index,2)
                print("edu_exp:",edu_index)
                #Gross National income per capital as an indicator for standard of living
                print("per capital income IN US DOLLARS to determine standard of living ")
                mean_income = int(input("enter the per capital come: "))
                minimum_value =int("100")
                maximum_value =int("75000")
                living_standard = (math.log10(mean_income) - math.log10(minimum_value)) / (math.log10(maximum_value) - math.log10(minimum_value))
                living_standard = round(living_standard,2)
                print("living_standard:",living_standard)
                #TO CALCULATE HUMAN DEVELOPMET INDEX OF THE GIVEN DATA
                hdi = life_exp * edu_index * living_standard
                hdi = round(hdi,2)
                print("hdi is",hdi)
                HDI = pow(hdi,0.33)
                HDI = round(HDI,2)
                print("HDI is:",HDI)
                callagain()
          else:
              print("input a valid alphabet")
              Restart = (input('would you like to check another country HDI? input yes or no\n'))
              if Restart in('y','YES','yes','Y'):
                print("proceed")
              else:
                   print("cancel")
                   exit()
                
