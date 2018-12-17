/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package timiproject;
import java.util.Scanner;

/**
 *
 * @author HP
 */
public class TIMIproject {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
          Scanner in = new Scanner(System.in);
        double val;
        double result;
        double choice;
        double val2;
        System.out.println("enter 1=celsius to fahreheit,2=celsius to fahreheit");
        choice=in.nextInt();
        if (choice==1){
        System.out.println("enter value in celsius");
        val=in.nextDouble();
        result=val*1.8+32;
        System.out.printf("the temperature in celsius is %f",result);   
        }
        else if (choice==2){
        System.out.println("enter value in fahreheit");
        val=in.nextDouble();
        result=(val-32)/1.8;
        System.out.printf("the temperature in fahreheit is %f",result);
        }
        if(choice!=1|| choice!=2){
            System.out.println("wrong choice");
        }
      
    }
    
}
