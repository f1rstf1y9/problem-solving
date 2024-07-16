import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static ArrayList<Integer> primes = new ArrayList<>();
    public static int number = 2000000;
    public static int[] numbers = new int[number+1];

    public static void getAnswer(int target) {
        for (int prime : primes) {
            if (target - prime < 2) {
                break;
            }
            if (numbers[target-prime] == 1) {
                System.out.println(prime + " " + (target-prime));
                return;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        Arrays.fill(numbers, 1);

        for (int i = 2; i*i <= number; i++) {
            if (numbers[i] == 0) continue;
            for (int j = i*i; j <= number; j+=i) {
                numbers[j] = 0;
            }
        }

        for (int i = 2; i <= number; i++) {
            if (numbers[i] != 0) {
                primes.add(i);
            }
        }

        for (int i = 0; i < T; i++) {
            int N = sc.nextInt() * 2;
            getAnswer(N);
        }
    }
}