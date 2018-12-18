/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package randomint;

/**
 *
 * @author HP
 */
public class RandomInt {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int random = (int)
                (Math.random () * 10) + 5; 
        System.out.println(random);
    }
    
}
