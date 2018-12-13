import java.util.Scanner;

public class SimpleCalculator {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		float num1, num2, result;
		System.out.println("Enter the first number: ");
		num1 = input.nextFloat();
		System.out.println("Enter the second number: ");
		num2 = input.nextFloat();
		System.out.println("Enter the operator +-*/");
		char operator = input.next().charAt(0);
		switch(operator) {
		case '+':
			result = num1 + num2;
			System.out.println("The sum of the numbers is "+result);
			break;
		case '-':
			result = num1 - num2;
			System.out.println("The difference of the numbers is "+result);
			break;
		case '*':
			result = num1 * num2;
			System.out.println("The product of the numbers is "+result);
			break;
		case '/':
			result = num1 / num2;
			System.out.printf("%f divided by %f gives %f ", num1, num2, result);
			break;	
		default:
		System.out.println("Enter valid numbers!!!");

	}

} 
}
