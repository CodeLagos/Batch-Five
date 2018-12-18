/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package currentaffairsquiz;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

/**
 *
 * @author Sulyman Rasheed
 */
public class CurrentAffairsQuiz {
    private String firstname, lastname;
CurrentAffairsQuiz(String str, String str1) {
firstname = str;
lastname = str1;
}
public String getFirstname(){
return firstname;
}
public void setFirstname(String firstname) {
this.firstname = firstname;
}
public String getLastname(){
return lastname;
}
public void setLastname(String lastname) {
this.lastname = lastname;
}

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    Scanner input = new Scanner ( System.in);
    int day, month, year;
    int second, minute, hour;
    GregorianCalendar date = new GregorianCalendar();
    day = date.get(Calendar.DAY_OF_MONTH);
month = date.get(Calendar.MONTH);
year = date.get(Calendar.YEAR);

second = date.get(Calendar.SECOND);
minute = date.get(Calendar.MINUTE);
hour = date.get(Calendar.HOUR);

System.out.println("Date: " + day + " / " + (month + 1) + " / " + year);
System.out.println("Time : " + hour  + ":" + minute + ":" + second);
System.out.println();

System.out.println();
String Welcomequiz= "             Hello! Welcome to the quiz of Nigeria's Current Affairs";
System.out.println("" + Welcomequiz);
String firstname, lastname;
System.out.println("Input your first name");
firstname = input.next();
System.out.println("Input your last name");
lastname = input.next();
CurrentAffairsQuiz output = new CurrentAffairsQuiz(""+ firstname, "" + lastname);
System.out.println("Thank you " + output.getFirstname() +     output.getLastname());
System.out.println();
String introduction = "My  name is Mrs.Kehinde and I will be asking you, the user some multiple choice questions as regards Nigeria's history and/or current affairs";
System.out.println("" + introduction);
System.out.println();
String instructions = "There are four categories in this quiz and each category has four questions, the toal points obtainable is 80";
System.out.println("Instructions:input the best option from letter a-c " + instructions);
System.out.println();
System.out.println("press button 1 to proceed to the quiz or button 2 to exit");
int option;
option = input.nextInt();
if(option==1){
    String economicsanswer1, economicsanswer2, economicsanswer3, economicsanswer4 = null;
    System.out.println("                        Nigeria Economic history");
    System.out.println("1. In what year did Nigeria experienced recession? (a) 2015 (b) 2017 (c)10 ");
    String econsanswer1 = input.next();
    economicsanswer1 = "a";
    System.out.println("2. How many natural resources are there in Nigeria? (a) 20 (b) 21 (c)more than 21");
    String econsanswer2 = input.next();
    economicsanswer2 = "c";
    System.out.println("3. The Central Bank of Nigeria was established in _______ (a) 1975 (b) 2010 (c)none of the above");
    String econsanswer3 = input.next();
    economicsanswer3 = "c";
    System.out.println("4. Nigeria is ranked in what position as the most terrorised nation in the world (a) 2 (b) 1 (c)3 ");
    String econsanwer4 = input.next();
    economicsanswer4 = "c";
   
    System.out.println();
    System.out.println();
    String politicsanswer1, politicsanswer2, politicsanswer3, politicsanswer4 = null;
    System.out.println("                         Nigeria Political history");
    System.out.println("1. In what year was Nigeria algamated? (a) 1941 (b) 1871 (c)1914");
    String politanswer1 = input.next();
    politicsanswer1 = "c";
    System.out.println("2. Who was the first Prime Minister of Nigeria? (a) Yakubu Gowon (b) Tafawa Balewa (c)Goodluck Jonathan");
    String politanswer2 = input.next();
    politicsanswer2 = "b";
    System.out.println("3.What kind of party system do Nigeria practice (a) single/one (b) two (c)three/multi-party");
    String politanswer3 = input.next();
    politicsanswer3 = "c";
    System.out.println("4.In what year did Nigeria gained independence (a) 1980 (b) 1982 (c)1960 ");
    String politanswer4 = input.next();
    politicsanswer4 = "c";

    System.out.println();
    System.out.println();
    String religionanswer1, religionanswer2, religionanswer3, religionanswer4 = null;
    System.out.println("                        Nigeria Religion history");
    System.out.println("1. How many religions are there in Nigeria? (a) 2 (b) 1 (c)3 ");
    String relanswer1 = input.next();
    religionanswer1 = "c";
    System.out.println("2. Which of these is a religion in Nigeria (a) Islam (b) Atheist (c) none of the above");
    String relanswer2 = input.next();
    religionanswer2 = "a";
    System.out.println("3. Which of these is a religion in Nigeria (a) Christian (b) Babamama (c)none of the above");
    String relanswer3 = input.next();
    religionanswer3 = "a";
    System.out.println("4.An atheist is one who believes God? (a) true (b) false (c) maybe ");
    String relanswer4 = input.next();
    religionanswer4 = "b";
    System.out.println();
    System.out.println();
    
    String geographyanswer1, geographyanswer2, geographyanswer3, geographyanswer4 = null;
    System.out.println("                        Nigeria Geographical history");
    System.out.println("1. Is there sun in Nigeria (a) yes (b) no (c) why should I know ");
    String geoanswer1 = input.next();
    geographyanswer1 = "a";
    System.out.println("2. Is Nigeria a sub-saharan country? (a) false (b)true (c)not any more");
    String geoanswer2 = input.next();
    geographyanswer2 = "b";
    System.out.println("3. Nigeria is in which continent (a) Africa (b) Bi-afra (c)Nigeria-America");
    String geoanswer3 = input.next();
    geographyanswer3 = "a";
    System.out.println("4. Nigeria is ranked in what position as the most terrorised nation in the world (a) 2 (b) 1 (c)3 ");
    String geoanswer4 = input.next();
    geographyanswer4 = "c";
} else if (option ==2) {
    System.out.println("GoodBye " + output.getFirstname());
    }
        }
        
    }
    

  
        
        
        
        
    
    

