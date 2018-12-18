/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pytagorastheorem;
import java.util.Scanner;


/**
 *
 * @author MUYIWA
 */
public class PytagorasTheorem {
     static double a, b, res;
        static char choice ;
        static Scanner input = new Scanner(System.in);

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        menu();
        
            
        }
    public static void menu(){
    System.out.println("1. To find hypotenus\n");
            System.out.println("2. To find adjacent\n");
                    
            System.out.println("3. To find opposite\n");
            System.out.println("x. To Exit\n");
             choice = input.next().charAt(0);
             switch(choice)
             {
                  case'1': System.out.print("Enter value for adjacent a ");
                a = input.nextDouble();
                System.out.println("Enter value for opposite b");
                b = input.nextDouble();
                res =  (Math.sqrt((a*a)+(b*b)));
                System.out.println("hypotenus ="+res );
                break;
                
                case'2': System.out.print("Enter value for hypotenus a ");
                a = input.nextDouble();
                System.out.println("Enter value for opposite b");
                b = input.nextDouble();
                res =  (Math.sqrt((a*a)-(b*b)));
                System.out.println("adjacent ="+res );
                break;
                
                case'3': System.out.print("Enter value for hypotenus a ");
                a = input.nextDouble();
                System.out.println("Enter value for adjacent b");
                b = input.nextDouble();
                res =  (Math.sqrt((a*a)-(b*b)));
                System.out.println("opposite ="+res );
                break;
               
                
                case'x': System.exit(0);
                break;
                default: System.out.print("Wrong Choice!!!");
                break;
                }
            System.out.print("\n----------------------------------------\n");
        System.out.print("\n----------------------------------------\n");
        System.out.println("Another calculation");
        menu();
    }
        }

        
        
            
        
 
    

