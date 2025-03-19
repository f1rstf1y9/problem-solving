import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String pwd = br.readLine();
        
        if (pwd.charAt(0) == '0') {
            System.out.println(0);
            return;
        }
        
        int N = pwd.length();
        
        int[] dp = new int[N];
        dp[0] = 1;
        
        for (int i = 1; i < N; i++) {
            int num1 = Character.getNumericValue(pwd.charAt(i));
            int num2 = Integer.parseInt(""+pwd.charAt(i-1)+pwd.charAt(i));
            
            int p1 = (num1 >= 1 && num1 <= 9) ? 1 : 0;
            int p2 = (num2 >= 10 && num2 <= 26) ? 1 : 0;
            
            if (i == 1) {
                dp[i] = p1 + p2;
            } else {
                dp[i] = (dp[i-1]*p1 + dp[i-2]*p2) % 1000000;
            }
        }
        
        System.out.println(dp[N-1]);
    }
}