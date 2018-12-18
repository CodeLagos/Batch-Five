/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package resultsheet;
import java.util.Scanner;
/**Gabriel 
 *
 * @author  Eke Gabriel *CEGZEAL
 */
public class ResultSheet {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("STUDENT RESULT SHEET ");
        System.out.print("Enter Student Name: ");
        String name = input.nextLine();
        System.out.print("Enter Surname: ");
        String surName = input.nextLine();
        System.out.print("Other names: ");
        String otherNames = input.nextLine();
        System.out.print("Class/level: ");
        String classlevel = input.nextLine();
        
        
        
        // Data of the student
        System.out.println("\nInput Subject Score");
        System.out.print("Mathematics:  ");
        double mathematics = input.nextDouble();
        System.out.print("English: ");
        double english = input.nextDouble();
        System.out.print("Biology: ");
        double biology = input.nextDouble();
        System.out.print("Geography: ");
        double geography = input.nextDouble();
        System.out.print("Physics: ");
        double physics = input.nextDouble();
        System.out.print("Chemistry: ");
        double chemistry = input.nextDouble();
        System.out.print("Lictrature: ");
        double lictrature = input.nextDouble();
        System.out.print("Government: ");
        double government = input.nextDouble();
        System.out.print("Yoruba: ");
        double yoruba = input.nextDouble();
        
        
        System.out.println("\nDATA IMFORMATION");
        System.out.println("Name: "+ name);
        System.out.println("surname: "+ surName);
        System.out.println("Other names: " + otherNames);
        System.out.println("Class/level: " + classlevel);
        
        
        
        
        System.out.println("\nSubject/course Imformation");
        System.out.print("Mathematics: " + mathematics);
        double score = mathematics;
       if (score <=49){ System.out.println("-----faild  (F)"); }
       else if (score <=59){ System.out.println("-----pass  (P)"); }
       else if (score <=69){ System.out.println("-----credit  (C)"); }
       else if (score >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("English: " + english);
         double score1 = english;
       if (score <=49){ System.out.println("-----faild  (F)"); }
       else if (score1 <=59){ System.out.println("-----pass  (P)"); }
       else if (score1 <=69){ System.out.println("-----credit  (C)"); }
       else if (score1 >=70){ System.out.println("-----excellent  (A)"); }
       
       
        System.out.print("Biology: " + biology);
         double score2 = biology;
       if (score2 <=49){ System.out.println("-----faild  (F)"); }
       else if (score2 <=59){ System.out.println("-----pass  (P)"); }
       else if (score2 <=69){ System.out.println("-----credit  (C)"); }
       else if (score2 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Geography: " + geography);
         double score3 = geography;
       if (score3 <=49){ System.out.println("-----faild  (F)"); }
       else if (score3 <=59){ System.out.println("-----pass  (P)"); }
       else if (score3 <=69){ System.out.println("-----credit   (C)"); }
       else if (score3 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Physics: " + physics);
         double score4 = physics;
       if (score4 <=49){ System.out.println("-----faild  (F)"); }
       else if (score4 <=59){ System.out.println("-----pass  (P)"); }
       else if (score4 <=69){ System.out.println("-----credit  (C)"); }
       else if (score4 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Chemistry: " + chemistry);
         double score5 = chemistry;
       if (score5 <=49){ System.out.println("-----faild  (F)"); }
       else if (score5 <=59){ System.out.println("-----pass  (P)"); }
       else if (score5 <=69){ System.out.println("-----credit  (C)"); }
       else if (score5 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Lictrature: " + lictrature);
         double score6 = lictrature;
       if (score6 <=49){ System.out.println("-----faild  (F)"); }
       else if (score6 <=59){ System.out.println("-----pass  (P)"); }
       else if (score6 <=69){ System.out.println("-----credit  (C)"); }
       else if (score6 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Government: " + government);
         double score7 = government;
       if (score7 <=49){ System.out.println("-----faild  (F)"); }
       else if (score7 <=59){ System.out.println("-----pass  (P)"); }
       else if (score7 <=69){ System.out.println("-----credit  (C)"); }
       else if (score7 >=70){ System.out.println("-----excellent  (A)"); }
       
        System.out.print("Yoruba: " + yoruba);
         double score8 = yoruba;
       if (score8 <=49){ System.out.println("-----faild  (F)"); }
       else if (score8 <=59){ System.out.println("-----pass  (P)"); }
       else if (score8 <=69){ System.out.println("-----credit  (C)"); }
       else if (score8 >=70){ System.out.println("-----excellent  (A)"); }
       
        
               double a = mathematics;
               double b = english;
               double c = biology;
               double d = geography;
               double e = physics;
               double f = chemistry;
               double g = lictrature;
               double h = government;
               double i =  yoruba;
        double sum = (a+b+c+d+e+f+g+h+i);
       double  percentage = sum*10/100;
       System.out.println("Total=" + sum);
       System.out.println("Precentage: " + percentage);
       
       double average = percentage;
       if (average <=49){ System.out.println("Failed to repeat class"); }
       else if (average <=59){ System.out.println("Promoted on trial"); }
       else if (average <=69){ System.out.println("Passed Promoted"); }
       else if (average >=70){ System.out.println("Excellent you need to be Rewarded");}
       
    }
 }