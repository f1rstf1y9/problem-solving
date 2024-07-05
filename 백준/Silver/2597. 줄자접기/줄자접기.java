import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float length = sc.nextFloat();

        float[][] points = new float[3][2];

        for (int i = 0; i < 3; i++) {
            float x = sc.nextFloat();
            float y = sc.nextFloat();
            points[i][0] = Math.min(x, y);
            points[i][1] = Math.max(x, y);
        }

        for (int i = 0; i < 3; i++) {
            float x = points[i][0];
            float y = points[i][1];

            if (x == y) continue;

            float mid = (x+y)/2;
            if (length - mid <= mid) {
                length = mid;
                for (int j = i; j < 3; j++) {
                    float left = points[j][0];
                    float right = points[j][1];

                    if (mid < left) {
                        left = mid - (left - mid);
                    }
                    if (mid < right) {
                        right = mid - (right - mid);
                    }
                    points[j][0] = Math.min(left, right);
                    points[j][1] = Math.max(left, right);
                }
            } else {
                length -= mid;
                for (int j = i; j < 3; j++) {
                    float left = points[j][0];
                    float right = points[j][1];
                    left = (left < mid) ? mid - left : left - mid;
                    right = (right < mid) ? mid - right : right - mid;
                    points[j][0] = Math.min(left, right);
                    points[j][1] = Math.max(left, right);
                }
            }
        }
        System.out.print(length);
    }
}