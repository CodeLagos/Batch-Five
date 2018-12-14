print("")
print("       °THIS IS A CURRENCY CONVERTER°")
print( "")
print(" Please choose your converter.")
kripp = input("\n(A) Nigerian Naira \n(B) US Dollar \n(C) Japan Yen \n(D) China Yuan \n(E) Russian Ruble \n(F) South African Rand \n(G) British Pound \n")
if(kripp.lower() == "a"):
     sweet = float(input("Please enter your amount in Naira: "))
     drop = input( "\n(A) To Us Dollar \n(B) To Ghana Cedes \n(C) To South African Rand \n(D) To British Pound \n")
     
     if(drop.lower() == "a"):
         dollar = sweet * 0.00273
         print(sweet,"naira is equal to", dollar, "US dollars")
    
     elif(drop.lower() == "b"):
         cedes = sweet * 0.01344
         print(sweet,"naira is equal to", cedes, "Ghana Cedis")
     
     elif(drop.lower() == "c"):
         Rand = sweet * 0.03880
         print(sweet,"naira is equal to", Rand, "South African Rand")
     
     else:
           Pound = sweet * 0.00217
           print(sweet,"naira is equal to", Pound, "British Pound")
     

elif(kripp.lower() == "b"):
      taste = float(input("Please enter your amount in Dollar: "))
      prop = input( "\n(A) To Australian Dollar \n(B) To Ghana Cedes \n(C) To South African Rand \n(D) To Nigeria Naira \n")

      if(prop.lower() == "a"):
         Australian = taste * 1.38540
         print(taste,"US Dollar is ", Australian , "Australian dollars")
    
      elif(prop.lower() == "b"):
	        Cedes = taste * 4.9231
	        print(taste,"US Dollar is ", Cedes , "Ghanaian New Cedis")
	       
      elif(prop.lower() == "c"):
	        Rand = taste * 14.2119
	        print(taste,"US Dollar is ", Rand, " South African Rand")
	         
	             
      else:
	          Naira = taste * 363.217
	          print(taste,"US Dollar is ", Naira, " Nigerian Naira")
	    
	     
   
elif(kripp.lower() == "c"):
      enjoy = float(input("Please enter your amount in Yen: "))
      pick = input( "\n(A) To Nigerian Naira \n(B) To Canadian Dollar \n(C) To South African Rand \n(D) To British Pound \n(E) To US Dollar \n")

      if(pick.lower() == "a"):
          naira = enjoy * 3.20378
          print(enjoy, "Japan Yen is ", naira, "Nigerian Naira")
          
      elif(pick.lower() == "b"):
          canadian = enjoy * 0.01179
          print(enjoy, "Japan Yen is ",canadian, "Canadian Dollar")

      elif(pick.lower() == "c"):
          wand = enjoy * 0.12536
          print(enjoy, "Japan Yen is ", wand, "South African Rand")
          
      elif(pick.lower() == "d"):
          paund = enjoy * 0.00702
          print(enjoy, "Japan Yen is ", paund, " British Pound")
          
      
      else:
           dolly = enjoy * 0.00882
           print(enjoy, "Japan Yen is ", dolly, "US Dollars")
           
     
elif(kripp.lower() == "d"):
      math = float(input("Please enter your amount in Yuan: "))      
      Good = input( "\n(A) To Australian Dollar \n(B) To Ghana Cedes \n(C) To South African Rand \n(D) To Nigeria Naira \n")
      
      if(Good.lower() == "a"):
          ausd = math * 0.20114
          print(math, " China Yuan is ", ausd, " Australian Dollar")
      
      elif(Good.lower() == "b"):
          ghacede = math * 0.71477
          print(math, " China Yuan is ", ghacede, "Ghanaian New Cedi")
          
      elif(Good.lower() == "c"):
           sorand = math * 2.06337
           print(math, " China Yuan is ", sorand, "South African Rand")
           
      else:
           niagra = math * 52.7341
           print(math, " China Yuan is ", niagra, "Nigerian Naira")
      

elif(kripp.lower() == "e"):
      forever = float(input("Please enter your amount in Ruble: "))
      forest = input ("\n(A) To Nigerian Naira \n(B) To Canadian Dollar \n(C) To South African Rand \n(D) To British Pound \n")

      if(forest.lower() == "a"):
          nini = forever * 5.6885
          print(forever, "Russian Ruble is ", nini, "Nigerian Naira")
          
      elif(forest.lower() == "b"):
            canadol  = forever * 0.02012
            print(forever, "Russian Ruble is ", canadol, "Canadian Dollar")
            
      elif(forest.lower() == "c"):
            sowo = forever * 0.21398
            print(forever, "Russian Ruble is ", sowo, "South African Rand")
            
      else:
           pondo = forever * 0.01198
           print(forever, "Russian Ruble is ", pondo, " British Pound")
           
elif(kripp.lower() =="f"):
      mate = float(input("Please enter your amount in Rand: "))
      drip = input( "\n(A) To Us Dollar \n(B) To Ghana Cedes \n(C) To China Yuan \n(D) To British Pound \n")
     
      if(drip.lower() == "a"):
          usd = mate * 0.07029
          print(mate, "South African Rand is",usd, "US Dollar")
          
      elif(drip.lower() == "b"):
            ghac = mate * 0.34603
            print(mate, "South African Rand is",ghac, "Ghanaian Cedis")
            
      elif(drip.lower() == "c"):
            chiyuan = mate * 0.48377
            print(mate, "South African Rand is", chiyuan, "China Yuan")
            
      else:
            bripound = mate * 0.05591
            print(mate, "South African Rand is", bripound, "British Pound ")
            
      
else:
     crop = float(input("Please enter your amount in Pound: "))
     deal = input( "\n(A) To Us Dollar \n(B) To Ghana Cedes \n(C) To China Yuan \n(D) To Nigerian Naira \n")

     if(deal.lower() == "a"):
          pousd = crop * 1.25698
          print(crop, "British Pound is ", pousd, "US Dollar")
          
     elif(deal.lower() == "b"):
          gha = crop * 6.18824
          print(crop, "British Pound is ",gha, "Ghanaian Cedis")
          
     elif(deal.lower() == "c"):
          chichi = crop * 8.65159
          print(crop, "British Pound is ",chichi, "China Yuan ")
          
     elif(deal.lower()== "d"):
           nana = crop * 456.556
           print(crop, "British Pound is ",nana, "Nigerian Naira") 
     
     else:
           print("incorrect")