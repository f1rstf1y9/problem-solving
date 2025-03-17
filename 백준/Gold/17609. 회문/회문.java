import java.io.*;

public class Main {
    public static int is_palindrome(String str, int p1, int p2, boolean is_pseudo) {
        while (p1 < p2) {
            if (str.charAt(p1) == str.charAt(p2)) {
                p1++;
                p2--;
            } else {
                if (is_pseudo) return 2;
                if (is_palindrome(str, p1, p2-1, true) == 0 || is_palindrome(str, p1+1, p2, true) == 0) return 1;
                return 2;
            }
        }
        return 0;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            String str = br.readLine();
            System.out.println(is_palindrome(str, 0, str.length()-1, false));
        }
    }
}
