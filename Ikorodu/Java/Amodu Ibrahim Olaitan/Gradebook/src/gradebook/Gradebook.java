/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package gradebook;

/**
 *
 * @author user
 */
public class Gradebook {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    }
    private String courseName;
    // constructor initializes courseName
  public Gradebook( String name )
 {
courseName = name; // initializes courseName
 } // end constructor

// method to set the course name
public void setCourseName( String name )
 {
 courseName = name; // store the course name
 } // end method setCourseName
 // method to retrieve the course name
 public String getCourseName()
{
 return courseName;
 // end method getCourseName
// display a welcome message to the GradeBook user
 public void displayMessage()
         {
 // getCourseName gets the name of the course
 System.out.printf( "Welcome to the grade book for\n%s!\n\n",
  getCourseName() );
         
         } // end method displayMessage

 // determine class average based on 10 grades entered by user

 {
 // create Scanner to obtain input from command window
 Scanner input = new Scanner( System.in );

 int total; // sum of grades entered by user

 int grade; // grade value entered by use int average; // average of grades

// initialization phase
total = 0; // initialize total


 // processing phase uses counter-controlled repetition
 while( ); // loop 10 times
{
 System.out.print( "Enter grade: " ); // prompt
grade = input.nextInt(); // input next grade
 total = total + grade; // add grade to total
 // termination phase

// display total and average of grades
 System.out.printf( "\nTotal of all 10 grades is %d\n", total );
System.out.printf( "Class average is %d\n", average );
 } // end method determineClassAverage
 } // end class GradeBook
 } // end while

  
