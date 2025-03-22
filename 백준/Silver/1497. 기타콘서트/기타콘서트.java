import java.io.*;
import java.util.*;

public class Main {
    public static long maxValue = 0;
    public static int maxCount = 0;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        long[] guitars = new long[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            st.nextToken();
            
            String valiable_songs = st.nextToken().replace('Y', '1').replace('N', '0');
            guitars[i] = Long.parseLong(valiable_songs, 2);
        }
        
        backtracking(guitars, 0, 0, 0, N);
            
        if (maxValue == 0) {
            System.out.println(-1);
        } else {
            System.out.println(maxCount);
        }
    }
    
    public static void backtracking(long[] guitars, long currentValue, int currentIdx, int currentCount, int N) {
        if (currentValue == maxValue) {
            maxCount = Math.min(currentCount, maxCount);
        }
        if (currentValue > maxValue) {
            maxCount = currentCount;
            maxValue = currentValue;
        }
        if (currentIdx == N) return;
        
        backtracking(guitars, currentValue | guitars[currentIdx], currentIdx+1, currentCount+1, N);
        backtracking(guitars, currentValue, currentIdx+1, currentCount, N);
    }
}