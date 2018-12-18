package numberbases;
import java.util.Scanner;
public class HexaDecimal {

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter The Decimal Number : ");
        
        int inputNumber = sc.nextInt();
       
        int copyOfInputNumber = inputNumber;
        
        String hexa = "";
        
       char hexaDecimals[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
      
        int rem = 0;
        
        
        while(inputNumber > 0)
        {
            rem = inputNumber%16;
            
            hexa =  hexaDecimals[rem] + hexa;
            
            inputNumber = inputNumber/16;
        }
        
        System.out.println("HexaDecimal Equivalent of "+copyOfInputNumber+" is "+hexa);
    }
}
   
  



