/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package grammtokilogram;
import java.util.Scanner;
/**
 *
 * @author Nero
 */
public class GrammToKilogram {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input= new Scanner(System.in);
        double kg;
        double gramm;
                
        System.out.print("value for gramm ");
        gramm = input.nextInt();
        kg = (gramm / 1000);
        
        System.out.println(gramm +"g = " + kg +"kg");
    }
    
}
