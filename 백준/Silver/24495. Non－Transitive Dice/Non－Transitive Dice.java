import java.util.Scanner;

public class Main {
    public static int[] A = new int[4];
    public static int[] B = new int[4];

    public static boolean isFirstWinner(int[] A, int[] B) {
        int a_score = 0;
        int b_score = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (A[i] > B[j]) {
                    a_score += 1;
                } else if (A[i] < B[j]) {
                    b_score += 1;
                }
            }
        }
        return (a_score > b_score) ? true : false;
    }

    public static boolean check(int[] die1, int[] die2) {
        for (int a = 1; a <= 10; a++) {
            for (int b= 1; b <= 10; b++) {
                for (int c = 1; c <= 10; c++) {
                    for (int d = 1; d <= 10; d++) {
                        int[] C = {a, b, c, d};
                        if (isFirstWinner(C, die1) && isFirstWinner(die2, C)) return true;
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            for (int j = 0; j < 4; j++) {
                A[j] = sc.nextInt();
            }
            for (int j = 0; j < 4; j++) {
                B[j] = sc.nextInt();
            }
            if (isFirstWinner(A, B)) {
                if (check(A, B)) {
                    System.out.println("yes");
                } else {
                    System.out.println("no");
                }
            } else if (isFirstWinner(B, A)) {
                if (check(B, A)) {
                    System.out.println("yes");
                } else {
                    System.out.println("no");
                }
            } else {
                System.out.println("no");
            }
        }
    }
}