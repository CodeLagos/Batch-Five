/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fproject;


public class sine extends SohCahToa {
    public static void main(String[] args){
        double x=45;
        double y=100;
        x=Math.toRadians(x);
        y=Math.toRadians(y);
        System.out.println("Math.sin(" + x + ")=" + Math.sin(x)); 
        System.out.println("Math.sin(" + y + ")=" + Math.sin(y)); 
    }
}
