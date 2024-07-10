import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            int N = sc.nextInt();
            float maxHeight = 0;
            String studentStr = "";

            if (N == 0) break;
            for (int i = 0; i < N; i++) {
                String name = sc.next();
                float height = sc.nextFloat();
                if (height > maxHeight) {
                    maxHeight = height;
                    studentStr = name + " ";
                } else if (height == maxHeight) {
                    studentStr += name + " ";
                }
            }
            System.out.println(studentStr);
        }
        sc.close();
    }
}