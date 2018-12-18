/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mathematicalproblems;
import java.util.Scanner;
/**
 *
 * @author USER
 */
public class MathematicalProblems {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    Scanner input = new Scanner( System.in);
    System.out.println("press either 1,2,3,4,5 to solve any mathematical problem identified below");

    System.out.println("press 1 for Simple regression calculation");
    System.out.println("press 2 for Simple interest calculation");
    System.out.println("press 3 for Quadratic Equation  calculation");
    System.out.println("press 4 for Simultaneous Equation calculation");
    System.out.println("press 5 for pathogoras calculation of the hypothenuse side, press 6 to find the ajacent value, press 7 to find the opposite value: ");
    int option = input.nextInt();
    
    if (option == 1) {
        double x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12,n, b1,d1,d2,d3,d4,d5,d6;
     System.out.println("Thank you, your selected problem to solve is Simple Regression");
     System.out.println("value of x1");
     x1 = input.nextDouble();
     System.out.println("value of y1");
     y1 = input.nextDouble();
     System.out.println("value of x2");
     x2 = input.nextDouble();
     System.out.println("value of y2");
     y2 = input.nextDouble();
     System.out.println("value of x3");
     x3 = input.nextDouble();
System.out.println("value of y3");
     y3 = input.nextDouble();
     System.out.println("value of x4");
     x4 = input.nextDouble();
     System.out.println("value of y4");
     y4 = input.nextDouble();
     System.out.println("value of x5");
     x5 = input.nextDouble();
     System.out.println("value of y5");
     y5 = input.nextDouble();
     System.out.println("value of x6");
     x6 = input.nextDouble();
     System.out.println("value of y6");
     y6 = input.nextDouble();
     System.out.println("value of x7");
     x7 = input.nextDouble();
     System.out.println("value of y7");
     y7 = input.nextDouble();
     System.out.println("value of x8");
     x8 = input.nextDouble();
     System.out.println("value of y8");
     y8 = input.nextDouble();
     System.out.println("value of x9");
     x9 = input.nextDouble();
     System.out.println("value of y9");
     y9 = input.nextDouble();
     System.out.println("value of x10");
     x10 = input.nextDouble();
     System.out.println("value of y10");
     y10 = input.nextDouble();
     System.out.println("value of x11");
     x11 = input.nextDouble();
     System.out.println("value of y11");
     y11 = input.nextDouble();
     System.out.println("value of x12");
     x12 = input.nextDouble();
     System.out.println("value of y12");
     y12 = input.nextDouble();
     System.out.println("enter number of observations");
     n = input.nextDouble();
     d1 =(n)* (x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5 + x6*y6 + x7*y7 + x8*y8 + x9*y9 + x10*y10 + x11*y11 + x12*y12);
     d2 =(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12) * (y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12);
     d3 = n * (Math.pow(x1,2) + Math.pow(x2,2)+ Math.pow(x3,2) + Math.pow(x4,2)+ Math.pow(x5,2) + Math.pow(x6,2)+ Math.pow(x7,2) + Math.pow(x8,2)+ Math.pow(x9,2) + Math.pow(x10,2)+ Math.pow(x11,2) + Math.pow(x12,2)); 
     d4  = Math.pow(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12,2);
     d5 = d1-d2;
     d6 = d3-d4;
     b1 = d5/d6;
     System.out.println("Sum of nxy: " + d1);
     System.out.println("Sum of xy: " + d2);
     System.out.println("multiplication of n and Sum of x square: " + d3);
     System.out.println("Sum of x square: " + d4);
     System.out.println("difference of nxy and xy: " + d5);
     System.out.println("difference of n*xsquare and sum of x square : " + d6);
     System.out.println("value of b1: " + b1);
    }
    else if (option == 2) {
    double i, p, y, s;
    System.out.println("Thank you, your selected problem to solve is Simple Interest");
    System.out.println("value of rate");
    i = input.nextDouble();
    System.out.println("value of principal");
    p = input.nextDouble();
    System.out.println("value of year");
    y = input.nextDouble();
    s =(i*p*y)/100;
    System.out.println("value of interest" + s);
    }
    else if (option == 3) {
    double a,b,c,s11,s12;
    System.out.println("Thank you, your selected problem to solve is Quadratic Equation");
    System.out.println("value of a");
    a = input.nextDouble();
    System.out.println("value of b");
    b = input.nextDouble();
    System.out.println("value of c");
    c = input.nextDouble();
    s11 = (-b + Math.sqrt(Math.pow(b,2)-(4*a*c))) / (2*a);
    s12 = (b + Math.sqrt(Math.pow(b,2)-(4*a*c))) / (2*a);
    System.out.println("value of x1: " + s11);
    System.out.println("value of x2: " + s12);
    }
    else if (option == 4) {
    System.out.println("Thank you, your selected problem to solve is Simultaneous Equation");
    double m1, n1, c1, m2, n2, c2, k1, k2;
    System.out.println("enter the first coefficient of x in eqn 1");
    m1 = input.nextDouble();
    System.out.println("enter the first coefficient of y in eqn 1");
    n1 = input.nextDouble();
    System.out.println("enter the first constant in eqn 1");
    c1 = input.nextDouble();
    System.out.println("enter the second coefficient of x in eqn 2");
    m2 = input.nextDouble();
    System.out.println("enter the second coefficient of x in eqn 2");
    n2 = input.nextDouble();
    System.out.println("enter the second constant in eqn 1");
    c2 = input.nextDouble();
    k2 = (c2-m2*c1)/(-m2*n1+m1*n2);
    k1 = n1*k2+c1/m1;
    System.out.println("value of x: " + k1);
    System.out.println("value of y: " + k2);
    }
    else if (option == 5) {
    System.out.println("Thank you, your selected problem to solve is Pathogoras solution");
    System.out.println("By pressing 5, you have opted to solve for the hypthenuse value b");
    double t,u,v;
    System.out.println("enter the value of a, which is d adjacent side or value");
    t = input.nextDouble();
    System.out.println("enter the value of c, which is d opposite or value");
    u = input.nextDouble();
    v = (Math.sqrt(Math.pow(t,2)+Math.pow(u,2)));
    System.out.println("The value of b: hypothenuse is: " + v);
    }
    else if ( option == 6) {
    System.out.println("By pressing 6, this will find value of adjacent a");
    double t1,u1,v1;
    System.out.println("enter the value of c, which is the opposite side or value");
    u1 = input.nextDouble();
    System.out.println("enter the value of b, which is the hypothenuse side or value");
    v1 = input.nextDouble();
    t1 = (Math.sqrt(Math.pow(v1,2)-Math.pow(u1,2)));  
    System.out.println("The value of a: adjacent is: " + t1);
   
    }
    // a = adj, b = hyp, c= opp
    //b2 = a2 + c2
    // c2 = b2-a2
    // a2 = b2 - c2
    else if ( option == 7) {
    System.out.println("By pressing 7, this will find value of opposite c");
    double t2,u2,v2;
    System.out.println("enter the value of b, which is the hypothenuse side or value");
    v2 = input.nextDouble();
    System.out.println("enter the value of a, which is the adjacent side or value");
    t2 = input.nextDouble();
    u2 = (Math.sqrt(Math.pow(v2,2)-Math.pow(t2,2)));
    System.out.println("The value of b: hypothenuse is: " + u2);
   
    }
    }
}
