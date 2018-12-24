/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fproject;

/**
 *
 * @author Dre
 */
public class Arithmetic {
    private int value1;
    private int value2;
    public void setValue1(int value1){
      this.value1=value1;
    }
    public void setValue2(int value2){
      this.value2=value2;
    }
    public int getValue1(){
      return this.value1;
    }
    public int getValue2(){
      return this.value2;
    }

    
    Arithmetic(){}
    
    public int Addition(){
        return value1+value2;
    }
     public int Subtraction(){
        return value1-value2;
    }
      public int multiplication(){
         
        return value1*value2;
    }
     public int division(){
          if(value1==0||value2==0){
              System.out.println("Wrong Syntax");
              return 0;
          }
          else{
              return value1/value2;
          }
        
    }
    
}
