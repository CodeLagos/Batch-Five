/*Code Lagos Project by Oluwasola Awe
 *program on how to generate random password for those who have trouble
  remembering their passwords
 * using random() method of util class in java
 */
package passwordgeneration;

/**Oluwasola Awe
 * Code Lagos Java Project
 */
import java.util.*;
public class Passwordgeneration {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // The length of password  i chose is 8
        int length = 10;
        //the system prints out a password of length 8
        //i can vary the legth here between the lowest possible integer and the
        //highest which i benchmarked at 10
        System.out.println(password(8));
    }
    static char[] password(int len)
    {
        System.out.println("Generating random password for user");
        System.out.print("Your new password is : ");
    
        String Capital_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String Small_chars = "abcdefghijklmnopqrstuvwxyz";
        String numbers = "0123456789";
        String Symbols = "!@#$%^&*_=+-/.?<>)(~";
        
        String values = Capital_chars + Small_chars + numbers + Symbols;
       //Using random method
       Random rndm_method = new Random();
       char[] password = new char[len];
       for (int i = 0; i < len; i++)
       {
           //use of charAt() method: to get the character value
           //use of nextInt() because the scanned value is an integer
           password[i] = values.charAt(rndm_method.nextInt(values.length()));
           
       }
       return password;
    }
    //To change body of generated methods, choose Tools | Templates.
    }