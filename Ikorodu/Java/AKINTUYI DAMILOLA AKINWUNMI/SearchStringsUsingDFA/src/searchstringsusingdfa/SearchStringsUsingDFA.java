/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package searchstringsusingdfa;
import java.util.Scanner;
/**
 *
 * @author Sulyman Rasheed
 */
public class SearchStringsUsingDFA {

    /**
     * @param args the command line arguments
     */
    
    
    public static final int NO_OF_CHARS = 256;
 
    public static int getNextState(char[] pat, int M, int state, int x)
    {
    //NAME : AKINTUYI DAMILOLA AKINWUNMI
        if (state < M && x == pat[state])
            return state + 1;
        int ns, i;
        
        for (ns = state; ns > 0; ns--)
        {
            if (pat[ns - 1] == x)
            {
                for (i = 0; i < ns - 1; i++)
                {
                    if (pat[i] != pat[state - ns + 1 + i])
                        break;
                }
                if (i == ns - 1)
                    return ns;
            }
        }
        return 0;
    }
    public static void computeTF(char[] pat, int M, int[][] TF)
    {
        int state, x;
        for (state = 0; state <= M; ++state)
            for (x = 0; x < NO_OF_CHARS; ++x)
                TF[state][x] = getNextState(pat, M, state, x);
    }
    public static void search(char[] pat, char[] txt)
    {
        int M = pat.length;
        int N = txt.length;
        int[][] TF = new int[M + 1][NO_OF_CHARS];
        computeTF(pat, M, TF);
        int i, state = 0;
        for (i = 0; i < N; i++)
        {
            state = TF[state][txt[i]];
            if (state == M)
            {
                System.out.print(pat);
                System.out.print(" found at " + (i - M + 1));
            }
        }
    }
  
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the main string: ");
        String main = sc.nextLine();
        System.out.println("Enter the pattern string: ");
        String pattern = sc.nextLine();
        search(pattern.toCharArray(), main.toCharArray());
        sc.close();
  }
}

    
    

