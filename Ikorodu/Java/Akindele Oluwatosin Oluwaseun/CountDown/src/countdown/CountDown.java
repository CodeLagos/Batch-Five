/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package countdown;
import java.util.Scanner;
/**
 *
 * @author Nero
 */
public class CountDown {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        
        int counter = 10;
        while (counter > 0){
           counter--;
        
            System.out.println( counter);
        }  
    }
    
}
