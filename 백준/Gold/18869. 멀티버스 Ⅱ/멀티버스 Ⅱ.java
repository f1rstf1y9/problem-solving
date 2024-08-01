import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Integer>> spaceList = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            Set<Integer> set = new HashSet<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                 int num = Integer.parseInt(st.nextToken());
                 list.add(num);
                 set.add(num);
            }
            ArrayList<Integer> sortedList = new ArrayList<>(set);
            Collections.sort(sortedList);

            for (int j = 0; j < n; j++) {
                int idx = Collections.binarySearch(sortedList, list.get(j));
                list.set(j,idx);
            }
            spaceList.add(list);
        }

        // 똑같은 애들있는지 체크
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = i+1; j < m; j++) {
                if (Arrays.equals(spaceList.get(i).toArray(), spaceList.get(j).toArray())) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}