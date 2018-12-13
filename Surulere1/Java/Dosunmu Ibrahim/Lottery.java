import java.util.Scanner;

// This program can be used to calculate CGPA of a student
public class CGPA {
	private int totalUnit = 0;
	private int point;
	private int wp;
	private int totalWP = 0;
	private float cgpa; 
	
	public static void main (String args[]) {
		Scanner sc = new Scanner (System.in);
		CGPA myObject = new CGPA(); 
		System.out.printf("Course Name\t Unit\t Score\t Grade\n");
		for ( int i=1; i<=12; i++) {
			
			System.out.println("Enter your unit: ");
			int courseUnit = sc.nextInt();
			System.out.println("Enter your course score: ");
			int courseScore = sc.nextInt();
	
			myObject.calculateScore(courseScore, courseUnit); 
			System.out.println("");
		}
		myObject.displayCGPA();
		
	}
	public void calculateScore(int score, int unit ) { 

		if (score >=0 && score <=39) {
			point = 0;
			totalUnit += unit;
			wp = point * unit;
		System.out.println( "\t\t" + unit + "\t" + score + "\tF");
		}
		if (score >=40 && score <=44) {
			point = 1;
			totalUnit += unit;
			wp = point * unit;
			System.out.println( "\t\t" + unit + "\t" + score + "\tE");
		}
		if (score >=45 && score <=49) {
			point = 2;
			totalUnit += unit;
			wp = point * unit;
			System.out.println( "\t\t" + unit + "\t" + score + "\tD");
		}
		if (score >=50 && score <=59) {
			point = 3;
			totalUnit += unit;
			wp = point * unit;
			System.out.println( "\t\t" + unit + "\t" + score + "\tC");
		}
		if (score >=60 && score <=69) {
			point = 4;
			totalUnit += unit;
			wp = point * unit;
			System.out.println("\t\t" + unit + "\t" + score + "\tB");
		}
		if (score >=70 && score <=100) {
			point = 0;
			totalUnit += unit;
			wp = point * unit;
			System.out.println("\t\t" + unit + "\t" + score + "\tA");
		} 
	
	}
	public float calculateCGPA() {
		return cgpa = totalWP/totalUnit;
	}
	public void displayCGPA() {
		if (cgpa >= 0.00 && cgpa <= 0.99) {
			System.out.printf("Your CGPA is "+calculateCGPA()+". You are advised to withdraw");
		}
		if (cgpa >= 1.00 && cgpa <= 1.99) {
			System.out.printf("Your CGPA is "+calculateCGPA()+" and grade is PASS\n");
		}
		if (cgpa >= 2.00 && cgpa <= 2.49) {
			System.out.printf("Your CGPA is "+calculateCGPA()+" and grade is THIRD CLASS\n");
		}
		if (cgpa >= 2.50 && cgpa <= 3.49) {
			System.out.printf("Your CGPA is "+calculateCGPA()+" and grade is SECOND CLASS (Lower Division)\n");
		}
		if (cgpa >= 3.50 && cgpa <= 4.49) {
			System.out.printf("Your CGPA is "+calculateCGPA()+"and grade is SECOND CLASS (Upper Division)\n");
		}
		if (cgpa >= 4.50 && cgpa <= 5.00) {
			System.out.printf("Your CGPA is "+calculateCGPA()+"and grade is FIRST CLASS \n");
		}
	}
	 
}
