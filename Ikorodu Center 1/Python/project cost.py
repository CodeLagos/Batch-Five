while True:
    print("This is Damilola Talabi project")
    print("This is a production cost calculator")
    menu=input('Choose the production cost approach you want.\n1.UNIT COST\n2.FIXED COST\n3.VARIABLE COST\n4.TOTAL COST\n5.AVERAGE TOTAL COST\n6.MARGINAL COST\n7.AVERAGE FIXED COST\n8.AVERAGE VARIABLE COST\n9.TOTAL FIXED COST\n10.TOTAL AVERAGE COST\n11.MARGINAL REVENUE\n12.TOTAL REVENUE\n13.AVERAGE REVENUE\n14.MARGINAL PRODUCT\n15.AVERAGE PRODUCT\n16.TOTAL PRODUCT\n17.ECONOMIC PROFIT\n18.BREAK EVEN POINT\n19.PROFIT MAXIMIZING CONDITION\n')

    if menu =='1':
        V_C=int(input('Enter the Variable Cost:'))
        F_C=int(input('Enter the Fixed Cost:'))
        T_U=int(input('Enter the Total Unit:'))
        UNIT_COST=(V_C)+(F_C)/(T_U)
        print ("UNIT COST is:", UNIT_COST)
    elif menu =='2':
        Fixed_cost=int(input('Enter the Fixed Cost:'))
        print("FIXED COST is:",Fixed_cost)
    elif menu =='3':
        Variable_cost=int(input('Enter the Variable Cost:'))
        print("VARIABLE COST is:",Variable_cost)
    elif menu =='4':
        TFC=int(input('Enter the Total Fixed Cost:'))
        TVC=int(input('Enter the Total Variable Cost:'))
        TOTAL_COST=(TFC)+(TVC)
        print ("TOTAL COST is:",TOTAL_COST)
    elif menu == '5':
        TC=int(input('Enter the Total Cost:'))
        Q=int(input('Enter the Output produced:'))
        AVERAGE_TOTAL_COST=TC/Q
        print(AVERAGE_TOTAL_COST)
    elif menu =='6':
        C1=int(input('Enter First Cost Value:'))
        C2=int(input('Enter Second Cost Value:'))
        Q1=int(input('Enter First Output Value:'))
        Q2=int(input('Enter Second Output Value:'))
        MARGINAL_COST=(C2-C1)/(Q2-Q1)
        print("MARGINAL COST is:",MARGINAL_COST)
    elif menu == '7':
        ATC=int(input('Enter the Average Total Cost:'))
        AVC=int(input('Enter the Average Variable Cost:'))
        AVERAGE_FIXED_COST=(ATC)-(AVC)
        print("AVERAGE FIXED COST is:",AVERAGE_FIXED_COST)
    elif menu =='8':
        TVC=int(input('Enter the Total Variable Cost:'))
        AFC=int(input('Enter the Average Fixed Cost:'))
        AVERAGE_VARIABLE_COST=(TVC)/(AFC)
        print("AVERAGE VARIABLE COST is:",AVERAGE_VARIABLE_COST)
    elif menu =='9':
        TC=int(input('Enter the Total Cost:'))
        TVC=int(input('Enter the Total Variable Cost:'))
        TOTAL_FIXED_COST=(TC)-(TVC)
        print("TOTAL FIXED COST is:",TOTAL_FIXED_COST)
    elif menu =='10':
        AVC=int(input('Enter the Average Variable Cost:'))
        AFC=int(input('Enter the Average Fixed Cost:'))
        Q=int(input('Enter the Output:'))
        TOTAL_AVERAGE_COST=(AVC+AFC)/Q
        print ("TOTAL AVERAGE COST is:",TOTAL_AVERAGE_COST)
    elif menu =='11':
        TR1=int(input('Enter the First Total Revenue:'))
        TR2=int(input('Enter the Second Total Revenue:'))
        Q1=int(input('Enter the First Output'))
        Q2=int(input('Enter the Second Output'))
        MARGINAL_REVENUE=(TR2-TR1)/(Q2-Q1)
        print("MARGINAL REVENUE is:",MARGINAL_REVENUE)
    elif menu =='12':
        P=int(input('Enter the Price of Product:'))
        Q=int(input('Enter the Quantity Produced:'))
        TOTAL_REVENUE=(P)*(Q)
        print("TOTAL REVENUE is:",TOTAL_REVENUE)
    elif menu =='13':
        TR=int(input('Enter the Total Revenue:'))
        Q=int(input('Enter the Number Of Output produced:'))
        AVERAGE_REVENUE=(TR)/(Q)
        print("AVERAGE REVENUE is:",AVERAGE_REVENUE)
    elif menu =='14':
        TP1=int(input('Enter the first Total Product:'))
        TP2=int(input('Enter the Second Total Product:'))
        VF1=int(input('Enter the First Variable Function:'))
        VF2=int(input('Enter the Second Variable Function:'))
        MARGINAL_PRODUCT=(TP2-TP1)/(VF2-VF1)
        print("MARGINAL PRODUCT is:",MARGINAL_PRODUCT)
    elif menu == '15':
        TP=int(input('Enter the Total Product:'))
        VF=int(input('Enter the Variable Function:'))
        AVERAGE_PRODUCT=(TP)/(VF)
        print ("AVERAGE PRODUCT is:",AVERAGE_PRODUCT)
    elif menu =='16':
        AP=int(input('Enter the Average Product:'))
        VF=int(input('Enter the Variable Function:'))
        TOTAL_PRODUCT=(AP)*(VF)
        print ("TOTAL PRODUCT is:",TOTAL_PRODUCT)
    elif menu == '17':
        TR=int(input('Enter the Total Revenue:'))
        TC=int(input('Enter the Total Cost:'))
        ECONOMIC_PROFIT=(TR)-(TC)
        print("ECONOMIC PROFIT is:",ECONOMIC_PROFIT)
    elif menu == '18':
        AR=int(input('Enter the Average Revenue:'))
        ATC=int(input('Enter the Average Total Cost:'))
        BREAK_EVEN_POINT=(AR)==(ATC)
        print("BREAK EVEN POINT is:",BREAK_EVEN_POINT)
    elif menu =='19':
        MR=int(input('Enter the Marginal Revenue:'))
        MC=int(input('Enter the Marginal Cost:'))
        PROFIT_MAXIMISING_CONDITION=(MR)==(MC)
        print("PROFIT MAXIMISING CONDITION is:",PROFIT_MAXIMISING_CONDITION)


    

    
    
    


    
    
