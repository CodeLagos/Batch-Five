/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication36;
import java.util.Scanner;
/**
 *
 * @author Tundesky
 */
public class JavaApplication36 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    Scanner input=new Scanner(System.in);
    int x;
    int y;
    int z;
    
    System.out.println("enter first value");
    x=input.nextInt();
    System.out.println("enter second value");
    y=input.nextInt();
    System.out.println("enter third value");
    z=input.nextInt();
    int m;
    
    m=z;   
    if(y>m){
        m=y;
     }
    if(x>m){
        m=x;
    }
    System.out.println("the greatest number is "+m);
   }
    
}
