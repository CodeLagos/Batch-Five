/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package temperature.conversion;
import java.util.Scanner;
/**
 *
 * @author hp
 */
public class TemperatureConversion {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner (System.in);
        int fahrenheit,celsius;
        
        System.out.println ("Please Enter your Temperature in Fahrenheit: ");
        fahrenheit = input.nextInt ();
        
            celsius = ((fahrenheit-32)*5)/9;
            System.out.println ("Temperature in Celsius is"+": "+celsius);
            
            
            
    }
    
}
