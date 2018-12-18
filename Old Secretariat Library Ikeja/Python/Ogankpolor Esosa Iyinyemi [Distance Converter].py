print("Ogankpolor Esosa Iyinyemi")
print("esosaogankpolor@gmail.com")
print("Old secreteriat library Ikeja")
print("Distance Converter")
conv_fac = 0.62137
selection=input("what would you like to convert?\n 1)kilometer-miles\n 2)miles-kilometer\n")
if selection=="1":
   print("kilometer-miles")
   kilometer=float(input("Enter your kilometer value:"))
   miles=kilometer*conv_fac
   print(miles)
if selection=="2":
   print("miles-kilometer")
   miles=float(input("Enter your miles value:"))
   kilometer=miles/conv_fac
   print(kilometer)







