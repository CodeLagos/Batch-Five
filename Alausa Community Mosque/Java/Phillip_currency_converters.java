/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projectcurrency;
import java.util.Scanner;
/**
 *
 * @author HP
 */
public class Projectcurrency {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner a=new Scanner(System.in);
        int val;
        int val2;
        int result;
        int result2;
        int result3;
        System.out.println("enter 1=dollars to naira,2=naira to dollars");
        int choice=a.nextInt();
        if(choice==1){
             System.out.println("enter value in dollars");
             val=a.nextInt();
             result=val*360;
             System.out.printf("The value in naira is %d",result);
        }
        else if(choice==2){
             System.out.println("enter value in naira");
             val2=a.nextInt();
             result2=val2/360;
             result3=val2%360;
             System.out.printf("The value in dollars is %d and %d in cent\n",result2,result3);
        }
        else{
           System.out.println("wrong choice");
        }
        
        
    }
    
}
