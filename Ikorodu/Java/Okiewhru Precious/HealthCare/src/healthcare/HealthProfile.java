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
public class HealthProfile {
    private String firstName;
    private String lastName;
    private String gender;
    private String day;
    private String month;
    private int year;
    private double height;
    private double weight;
   
    
    public HealthProfile(){
        
    }
   public HealthProfile(String firstName,String lastName, String gender, 
            String day, String month, int year, double height, double weight){
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
        this.day = day;
        this.month = month;
        this.year = year;
        this.height = height;
        this.weight = weight;
        
   }

    public String getFirstName(){
        return firstName;
    }
    
    public String getLastName(){
        return lastName;
    }
   
    public String getGender(){
        return gender;
    }
    
    public String getDay(){
        return day;
    }
    public String getMonth(){
        return month;
    }
    public int getYear(){
        return year;
    }
    public double getHeight(){
        return height;
    }

    public double getWeight(){
        return weight;
    }
    public int calculateAge(){
         return 2018 - year;
       
    }
    public int calculateMaxHR(){
        return 220 - (2018 - year);
    }
    public double calculateTargetHR(){
        return 0.5 * (220 - (2018-year));
    }
    
    public double calculateBMI(){
      return (weight *703)/(height * height);
    
   }   
    public void details(){
        System.out.println("********************************");
        System.out.println("FIRST NAME: "+this.getFirstName());
        System.out.println("LAST NAME: "+this.getLastName());
        System.out.println("FIRST NAME: "+this.getGender());
        System.out.println("DATE OF BIRTH: "+this.getDay()+" "+this.getMonth()+" "+ this.getYear());
        System.out.println("HEIGHT(inches): "+this.getHeight());
        System.out.println("WEIGHT(lbs): "+this.getWeight());
        System.out.println("AGE: "+this.calculateAge());
        System.out.println("MAX. HEARTRATE "+this.calculateMaxHR());
        System.out.println("TARGET HEARTRATE: "+this.calculateTargetHR());
        System.out.println("BODY MASS INDEX: "+this.calculateBMI());
        System.out.println();
    }
    
    
}
