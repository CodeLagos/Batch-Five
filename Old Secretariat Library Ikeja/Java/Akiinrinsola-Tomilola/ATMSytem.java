import java.text.NumberFormat; 
import java.util.Date;
import java.util.Scanner; 

public class ATMSystem {
    private static int Transaction2;

	public static void main(String[] args) 
        {
        int attempts = 0;
        Scanner i = new Scanner(System.in);
        System.out.println("===THIS IS LEADBANK===");
        Date date = new Date();
        System.out.println(date.toString());//used toString to print out current sate
        System.out.println("Please Insert Card");
        int CARD = 0;
        int VALID_CARD = 1;//used 1 in place of ATM card
            while(CARD != VALID_CARD && attempts < 3)
        {
            CARD  = i.nextInt();
            attempts++;
            if (CARD !=VALID_CARD && attempts < 3) { 
               System.out.println("Check Card And Try Again" );
            }
        }
        if (CARD == VALID_CARD && attempts <= 3){
            System.out.println("Please Wait.......");
            transaction();
        }
     }
    public static int transaction(){
        int PIN = 0;
        int attempts = 0;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter 4-digits Pin: ");
        PIN = s.nextInt();
        if (PIN <= 9999 && attempts <= 3) {  
            System.out.println("WELCOME!");
        } 
        else{
            System.out.println("Maximum Tries Exceeded");
            System.exit(0);
        }
    
		// Create Current and Savings Account 

		Account Savings = new Account();
		Savings.setType("Savings");
		Savings.setBalance(50000);
		

		Account Current = new Account();
		Current.setType("Current");
		Current.setBalance(50000);
		

		NumberFormat formatter = NumberFormat.getInstance();
		Scanner input = new Scanner(System.in);
        
        
		while (true) {
                        System.out.println("====LEADBANK====");
			System.out.println("Choose 1 For Deposit");
			System.out.println("Choose 2 For Withdrawal");
			System.out.println("Choose 3 For Transfer");
			System.out.println("Choose 4 To Check Account Balance");
			System.out.println("Choose 5 To Exit ");
			System.out.println("Choose the operation you want to perform: ");

			int selection = input.nextInt(); // assign the user's input to the selection variable

			// This switch block will handle one of five selections and deal with them appropriately

			switch (selection) {

				// case 1 handles the depositing of money

				case 1:
					System.out.print("Enter (1) for Savings or (2) for Current: ");
					int depAccount = input.nextInt(); // Keeps track of which account to deposit money to

					if (depAccount == 1) {

						System.out.println("Your Savings balance is:₦" + formatter.format(Savings.getBalance()));

						System.out.print("How much money would you like to deposit:₦");
						double deposit = input.nextDouble();

						Savings.deposit(deposit);

						System.out.println("Your Savings balance is now:₦ " + formatter.format(Savings.getBalance()));
                                                Transaction2();

					}

					else if (depAccount == 2) {

						System.out.println("Your Current balance is:₦ " + formatter.format(Current.getBalance()));

						System.out.println("How much money would you like to deposit:₦");
						double deposit = input.nextDouble();

                                                Current.deposit(deposit);

						System.out.println("Current balance is now:₦ " + formatter.format(Current.getBalance()));
                                                Transaction2();
					}

					break;



				// case 2 handles the withdrawal of money	

				case 2:
					System.out.print("Enter (1) for Savings or (2) for Current: ");
					int witAccount = input.nextInt(); // Keeps track of which account to withdraw from

					if (witAccount == 1) {

						System.out.println("Your Savings balance is:₦ " + formatter.format(Savings.getBalance()));

						System.out.println("How much money would you like to withdraw:₦ ");
						double withdraw = input.nextDouble();

						Savings.withdraw(withdraw);

						System.out.println("Your Savings balance is now:₦ " + formatter.format(Savings.getBalance()));
                                                Transaction2();

					}

					else if (witAccount == 2) {

						System.out.println("Your Current balance is:₦ " + formatter.format(Current.getBalance()));

						System.out.println("How much money would you like to withdraw:₦ ");
						double withdraw = input.nextDouble();

						Current.withdraw(withdraw);

						System.out.println("Your Current balance is now: " + formatter.format(Current.getBalance()));
                                                Transaction2();
					}

					break;

				// case 3 = the transfer of funds	

				case 3:
					System.out.print("From which account do you wish to transfer funds from?, (1) for Savings or (2) for Current: ");
					int tranAccount = input.nextInt();

					if (tranAccount == 1) {

						System.out.println("Your Savings balance is:₦" + formatter.format(Savings.getBalance()));

						System.out.println("How much money do you wish to transfer from Savings to Current:₦ ");
						double tranAmount = input.nextDouble();

						Savings.withdraw(tranAmount);
						Current.deposit(tranAmount);

						System.out.println("You successfully transferred " + formatter.format(tranAmount) + " from Savings to Current");

						System.out.println("Savings Balance:₦" + formatter.format(Savings.getBalance()));
						System.out.println("Current Balance:₦" + formatter.format(Current.getBalance()));
                                                Transaction2();
					}

					else if (tranAccount == 2) {

						System.out.println("Your Current balance is:₦ " + formatter.format(Current.getBalance()));

						System.out.println("How much money do you wish to transfer from Current to Savings:₦ ");
						double tranAmount = input.nextDouble();

						Current.withdraw(tranAmount);
						Savings.deposit(tranAmount);

						System.out.println("You successfully transferred " + formatter.format(tranAmount) + " from Current to Savings");

						System.out.println("Savings Balance:₦ " + formatter.format(Savings.getBalance()));
						System.out.println("Current Balance:₦ " + formatter.format(Current.getBalance()));
                                                Transaction2();
					}                       
					break;

				// case 4 simply outputs the balances of both Current and Savings accounts	

				case 4:
					System.out.println("Savings Balance:₦ " + formatter.format(Savings.getBalance()));
					System.out.println("Current Balance:₦ " + formatter.format(Current.getBalance()));
                                        Transaction2();
					break;

				// case 5 exits the system

				case 5:
					System.exit(0);

					break;

			}				 	

           System.out.println("Thank you for banking with us!");
		}

	}
private static void Transaction2(){
        Scanner input = new Scanner(System.in);
        System.out.println("Do you want to perform another transaction?\n\nPress 1 for another transaction\n2 To exit");
        Transaction2 = input.nextInt();
        if(Transaction2 == 1){
            transaction(); // call transaction method
        } else if(Transaction2 == 2){
            System.out.println("Thanks for banking with us. Good Bye!");
            System.exit(0);
        } else {
            System.out.println("Invalid choice\n\n");
           Transaction2();
        }
    }        

}


class Account {

	String type;
	double balance;

	void setType(String accType) {

		type = accType;
	}

	void setBalance(double accBal) {

		balance = accBal;
	}

	void deposit(double dep) {

		balance += dep; 
	}

	void withdraw(double wit) {

		balance -= wit; 
	}


	String getType() {

		return type;
	}

	double getBalance() {

		return balance;
	}

}
