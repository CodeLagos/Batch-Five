/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication33;
import java.util.Scanner;
/**
 *
 * @author Tundesky
 */
public class JavaApplication33 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input=new Scanner(System.in);
         int z;
         int x;
         int y;
        
         System.out.println("enter first value");
         x=input.nextInt();
         System.out.println("enter second value");
         y=input.nextInt();
         z=x-y;
         System.out.println("the difference is "+z); 
    }
    
}
