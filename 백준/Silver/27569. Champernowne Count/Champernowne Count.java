import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int answer = 0;
        long numberModK = 0;

        for (int i = 1; i <= n; i++) {
            int digitNumber = String.valueOf(i).length();
            numberModK = (numberModK * (long)Math.pow(10, digitNumber) % k + i % k) % k;
            if (numberModK == 0) {
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}