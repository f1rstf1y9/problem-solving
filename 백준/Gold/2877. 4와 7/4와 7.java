import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = Integer.parseInt(sc.nextLine());
        
        StringBuffer answer = new StringBuffer();
        
        while (K > 0) {
            answer.append((K%2 == 0) ? "7" : "4");
            K = (K-1)/2;
        }
        
        System.out.println(answer.reverse().toString());
    }
}
