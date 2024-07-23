import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static boolean isTidyNumber(StringBuilder number) {
        for (int i = 1; i < number.length(); i++) {
            if (number.charAt(i) < number.charAt(i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 1; i <= T; i++) {
           long N = Long.parseLong(br.readLine());
           StringBuilder numStr = new StringBuilder(String.valueOf(N));
           while (!isTidyNumber(numStr)){
                for (int n = 0; n < numStr.length()-1; n++) {
                    int currentNum = Integer.parseInt(numStr.substring(n,n+1));
                    int nextNum = Integer.parseInt(numStr.substring(n+1,n+2));
                    if (currentNum > nextNum) {
                        numStr.setCharAt(n, (char)('0' + currentNum - 1));
                        for (int j = n+1; j < numStr.length(); j++) {
                            numStr.setCharAt(j, '9');
                        }
                    }
                }
           }
           long tidyNum = Long.parseLong(String.valueOf(numStr));
           System.out.println("Case #" + i + ": " + tidyNum);
        }
    }
}