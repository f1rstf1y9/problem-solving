import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(nums);
        
        int start_idx = 0;
        int end_idx = N-1;
        int cnt = 0;
        
        while (start_idx < end_idx) {
            if (nums[start_idx]+nums[end_idx] == M) {
                cnt++; start_idx++;
            } else if (nums[start_idx]+nums[end_idx] < M) {
                start_idx++;
            } else {
                end_idx--;
            }
        }
        
        System.out.print(cnt);
    }
}