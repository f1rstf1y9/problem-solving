import java.util.Scanner;

public class Main {
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public static boolean isAkarakaPalindrome(String s) {
        if (s.length() == 1) {
            return true;
        }
        if (!isPalindrome(s)) {
            return false;
        }
        int end = s.length()/2;
        int start = s.length()/2;
        if (s.length()%2 == 1) {
            start += 1;
        }
        return isAkarakaPalindrome(s.substring(0, end)) && isAkarakaPalindrome(s.substring(start));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        if (isAkarakaPalindrome(s)) {
            System.out.println("AKARAKA");
        } else {
            System.out.println("IPSELENTI");
        }
    }
}