package numberbases;
import java.util.Scanner;
public class NumberBases {

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        

        
        System.out.println("Enter The Decimal Number : ");
        
        int inputNumber = sc.nextInt();
       
        
        int copyOfInputNumber = inputNumber;
        
   
        String binary = "";
        
  
        int rem = 0;
        
        
        while (inputNumber > 0)
        {
            rem = inputNumber % 2;
            
            binary =  rem + binary;
            
            inputNumber = inputNumber/2;
        }
        
        System.out.println("Binary Equivalent of "+copyOfInputNumber+" is "+binary);
    }
}


