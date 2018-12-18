/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package patients.biodata;
import java.util.Scanner;

/**
 *
 * @author Abiola
 */
public class PatientsBiodata {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
   Scanner input = new Scanner(System.in);
      String PatientName, Religion, NextofKin, Occupation, State, LasrraifApplicable;
  
      System.out.println("Enter patient name;");
      PatientName = input.nextLine();
  
   System.out.println("Hospital number");
   int Hospitalnumber = input.nextInt();
   
   System.out.println("Religion");
   Religion = input.next(); 
   
   System.out.println("Age of patient");
   int Ageofpatient = input.nextInt();
   
   System.out.println("NextofKin");
   NextofKin = input.next(); 
  
   System.out.println("Occupation");
   Occupation = input.next(); 
   
   System.out.println("State");
   State = input.next(); 
   
   System.out.println("Lasrra if Applicable?");
   LasrraifApplicable = input.next();    
   
    }
    
}
