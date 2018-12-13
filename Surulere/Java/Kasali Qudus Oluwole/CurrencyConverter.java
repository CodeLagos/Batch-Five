package CurrencyConverter;

import java.util.Scanner;

public class CurrencyConverter {

    static void heading(String line) {
        System.out.println(line);
        for (int i = 0; i < line.length(); i++) {
            System.out.print("*");
        }

    }

    public static void main (String[] args){
        heading("Welcome To The CodeLagos Currency Converter Project ");

        Scanner input = new Scanner(System.in);

        System.out.println(" ");
        System.out.println("Choose The Currency You Wanna Convert To: ");

        System.out.println("1. To Convert Dollar to Naira Press 1");
        System.out.println("2. To Convert Pounds to Naira Press 2");
        System.out.println("3. To Convert Yen to Naira Press 3");
        System.out.println("4. To Convert Rupees to Naira Press 4");
        int code = input.nextInt();

        //The exchange rate varies from time to time, that is why user is required to input the
        // exchange rate at that particalar moment to get accurate result.
        System.out.print("Input Exchange Rate: ");
        double exchangeRate = input.nextFloat();

        HelperClass converter = new HelperClass(code, exchangeRate);
        converter.currencyConverter();

    }
}

//Second java class
package CurrencyConverter;

import java.util.Scanner;

public class HelperClass {

    double code;
    double exchangeRate;

    public HelperClass (double code, double exchangeRate){
        this.code = code;
        this.exchangeRate = exchangeRate;
    }

    public void currencyConverter() {
        Scanner input = new Scanner(System.in);

        if (code == 1) {
            System.out.print("Enter amount in Dollars: ");
            int dollar = input.nextInt();

            double change = dollar * exchangeRate;
            System.out.println("The amount of "+ dollar + " in Dollars = " + change + " in Naira.");
        }
        else if (code == 2) {
            System.out.print("Enter amount in Pounds: ");
            int pounds = input.nextInt();

            double change = pounds * exchangeRate;
            System.out.println("The amount of "+ pounds + " in Pounds = " + change + " in Naira");
        }
        else if (code == 3) {
            System.out.print("Enter amount in Yen: ");
            int yen = input.nextInt();

            double change = yen * exchangeRate;
            System.out.print("The amount of "+ yen + " in Yen = " + change + " in Naira");
        }
        else if (code == 4) {
            System.out.print("Enter amount in Rupees: ");
            int rupees = input.nextInt();

            double change = rupees * exchangeRate;
            System.out.println("The amount of "+ rupees + " in Rupees = " + change + " in Naira" );
        }
        else {
            System.out.println("Invalid Number");
        }

    }
}
