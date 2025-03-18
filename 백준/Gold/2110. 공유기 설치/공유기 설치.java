import java.io.*;
import java.util.*;

public class Main {
    public static boolean isValiable(int distance, int[] house, int C) {
        int count = 1;
        int prev_idx = 0;
        int cur_idx = 0;
        
        while (count < C) {
            cur_idx++;
            if (cur_idx >= house.length) return false;
            if (house[cur_idx] - house[prev_idx] >= distance) {
                prev_idx = cur_idx;
                count++;
            }
        }
        return true;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        
        int[] house = new int[N];
        for (int i = 0; i < N; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(house);
        
        int answer = 0;
        int low = 0;
        int high = house[house.length-1] - house[0];
        while (low <= high) {
            int mid = (low + high) / 2;
            if (isValiable(mid, house, C)) {
                answer = mid;
                low = mid+1;
            } else high = mid-1;
        }
        System.out.print(answer);
    }
}
