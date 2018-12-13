/*
 this is a command line interface simulation
 it creates a fighting simulation with an imaginary monster
 */
package fighting;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author SKEMPER
 */
public class Fighting {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Monster Statistics
        Scanner sc = new Scanner(System.in);
        System.out.println("Attack Points of Monster: ");
        int monsterAttack = sc.nextInt();
        System.out.println("Defense Points of Monster: ");
        int monsterDefense = sc.nextInt();
        System.out.println("Damage Points of Monster: ");
        int monsterDamage = sc.nextInt();
        System.out.println("Life Points of Monster: ");
        int monsterLife = sc.nextInt();
        
        
        //Player Statistics
        System.out.println("Your Attack Points: ");
        int yourAttack = sc.nextInt();
        System.out.println("Your Defense Points: ");
        int yourDefense = sc.nextInt();
        System.out.println("Your Damage Points: ");
        int yourDamage = sc.nextInt();
        System.out.println("Your Life Points: ");
        int yourLife = sc.nextInt();
        
        //The Attacker is decided by a coin toss
  do {
                Random generator = new Random();
                boolean attacker = generator.nextBoolean();
        
        //a dice is tossed for the attack value
        if (attacker)   {
            System.out.println("You Attack");
            int dice = generator.nextInt(6)+1 +generator.nextInt(6)+1;
            int attackValue = yourAttack + dice;
            System.out.println("Rolled Value: " + dice);
            System.out.println("Your Attack Value: " + attackValue);
            if (attackValue > monsterDefense) {
                System.out.println("Your Attack was Successful...");
                monsterLife = monsterLife - yourDamage;
                System.out.println("Monster's Remaining Life Points: " + monsterLife);
            } else {
                System.out.println("Your Attack was not Successful");
            }

        } else {
            System.out.println("Monster Attacks");
            int dice = generator.nextInt(6)+1 +generator.nextInt(6)+1;
            int attackValue = monsterAttack + dice;
            System.out.println("Rolled Value: " + dice);
            System.out.println("Monster Attack Value: " + attackValue);
            if (attackValue > monsterDefense) {
                System.out.println("Monster Attack was Successful...");
                monsterLife = monsterLife - yourDamage;
                System.out.println("Your Remaining Life Points: " + monsterLife);
            } else {
                System.out.println("Monster Attack was not Successful");
            }

        }

  }while (monsterLife > 0 && yourLife > 0);
   
    
    System.out.println("GAME OVER!!!");
        

    }
    
}
