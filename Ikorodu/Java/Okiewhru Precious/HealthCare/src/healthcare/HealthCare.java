/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package healthcare;

/**
 *
 * @author Nero
 */
public class HealthCare {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        HealthProfile data = new HealthProfile("Juliet", "Okoro", "F", "27th", "July", 1998,60, 110.231);
        data.details();
        
        HealthProfile data2  = new HealthProfile("Precious", "Akpan", "M", "2nd", "March", 1982, 72,176);
        data2.details();
        
        HealthProfile data3 = new HealthProfile("Blessing", "Titus", "F", "3rd", "January", 1967, 62, 100);
        data3.details();
       // System.out.println("FIRST NAME: " + "\nLAST NAME: "+ data.details());
    }
    
}
