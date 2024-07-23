import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double p = sc.nextDouble();
        double q = sc.nextDouble();
        double r = sc.nextDouble();

        if (p != r) {
            System.out.println(0);
        } else {
            double area = (p + q) * p * 2;
            System.out.printf("%.4f", area);
        }
    }
}