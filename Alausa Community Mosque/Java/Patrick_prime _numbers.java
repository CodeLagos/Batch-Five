/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package project_;                                                  
import java.util.Scanner;
/**             
             *
 * @author Phillip
 */
public class Project_ {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner d= new Scanner(System.in);
        System.out.println("this app allows you to get the prime numbers for a certain range");
         System.out.println("input first lower range ");
          int first=d.nextInt();
          System.out.println("input last  maximum range");
          int last=d.nextInt();
          int counter=first;
         
          while(counter < last){
              
             if(counter==2 || counter==3){
              System.out.print( counter + "  " );
            }
         
              if(counter%2==1  && counter%3==1 ){
                  System.out.print( counter + " " );
          }
      counter ++;
    }
}
}

