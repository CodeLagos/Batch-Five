/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package posmachine;
import java.util.Scanner;




/**
 *
 * @author presh
 */
public class PosMachine {
private static Scanner in;
private static float balance = 0 ; // initial balance to 0 for everyone
private static int anotherTransaction;


    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        in = new Scanner(System.in);
// call our transaction method here
transaction();
    }
private static void transaction(){
// here is where most of the work is
int choice;
System.out.println( "Please select an option" );
System.out.println( "1. Withdraw" );
System.out.println( "2. Transfer" );
System.out.println( "3. Depoit" );
System.out.println( "4. Balance" );
choice = in.nextInt();
switch (choice){
    
    
        
    case 1 :
float amount;
System.out.println( "Please enter amount to withdraw: " );
amount = in.nextFloat();
if(amount > balance || amount == 0 ){
System.out.println( "You have insufficient funds\n\n" );
anotherTransaction(); // ask if they want another transaction
} else {
// they have some cash
// update balance
balance = balance - amount;
System.out.println( "You have withdrawn " +amount+ " and your new balance is " +balance+ "\n" );
anotherTransaction();
}
break ;

    case 2:
   int transfer;
System.out.println( "please enter the amount you wish to transfer: " );
amount = in.nextFloat ();
if (amount < balance || amount ==0) {
System.out.println("You have successfully transfered funds to beneficiary\n\n");
balance = balance -amount;
System.out.println( "You have transfered " +amount+ " and your new balance is " +balance+ "\n" );
anotherTransaction();
}
break ;

    case 3 :
// option number 3 is for deposit
float deposit;
System.out.println( "Please enter amount you would wish to deposit: " );
deposit = in.nextFloat();
// update balance1
balance = deposit + balance;
System.out.println( "You have deposited " +deposit+ " new balance is " +balance+ "\n" );
anotherTransaction();
break ;

    case 4:
// this option is to check balance
System.out.println( "Your balance is " +balance+ "\n" );
anotherTransaction();
break ;
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
transaction(); // call transaction method
} else if (anotherTransaction == 2 ){
System.out.println( "Transcations completed! bye" );
} else {
System.out.println( "Invalid choice\n\n" );
anotherTransaction(); 
}
}
}


    


        
    
  


