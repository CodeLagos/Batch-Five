/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rechargecard;

import java.util.Scanner;

/**
 *
 * @author Sulyman Rasheed
 */
public class RechargeCard {

    private static Scanner in;
private static float balance = 0 ; // initial balance to 0 for everyone
private static int anotherTransaction;
public static void main(String args[]){
in = new Scanner(System.in);
// call our transaction method here
recharge();
}
private static void recharge(){
// here is where most of the work is
int choice;
System.out.println( "Please select an option" );
System.out.println( "1. MTN" );
System.out.println( "2. GLO" );
System.out.println( "3. AITEL" );
System.out.println( "4. Etisalat" );

choice = in.nextInt();
switch (choice){
case 1 :
float recharge1;
System.out.println( "Please enter amount you would wish to recharge(MTN): " );
recharge1 = in.nextFloat();
// update balance
//balance = recharge + balance;
System.out.println( "You have recharged " +recharge1);
anotherTransaction();//}
break ;
case 2 :
// option number 2 is depositing
float recharge;
System.out.println( "Please enter amount you would wish to recharge(GLO): " );
recharge = in.nextFloat();
// update balance
//balance = recharge + balance;
System.out.println( "You have recharged " +recharge);
anotherTransaction();
break ;
case 3 :
float recharge3;
System.out.println( "Please enter amount you would wish to recharge(AIRTEL): " );
recharge3 = in.nextFloat();
// update balance
//balance = recharge + balance;
System.out.println( "You have recharged " +recharge3);
anotherTransaction();
break ;
case 4:
    float recharge4;
System.out.println( "Please enter amount you would wish to recharge(ETISALAT): " );
recharge4 = in.nextFloat();
// update balance
//balance = recharge + balance;
System.out.println( "You have recharged " +recharge4);
anotherTransaction();
    break;
default :
        
System.out.println( "Invalid option:\n\n" );
anotherTransaction();
break ;
}
}
private static void anotherTransaction(){
System.out.println( "Do you want another transaction?\n\nPress 1 for another transaction\n2 To exit" );
anotherTransaction = in.nextInt();
if (anotherTransaction == 1 ){
recharge(); // call transaction method
} else if (anotherTransaction == 2 ){
System.out.println( "Thanks for patronage!" );
} else {
System.out.println( "Invalid choice\n\n" );
recharge();

    }
    
} 
 }
