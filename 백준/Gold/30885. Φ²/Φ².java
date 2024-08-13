import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextInt();
        Deque<long[]> a = new LinkedList<>();
        Deque<long[]> temp = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            a.add(new long[]{i+1, sc.nextLong()});
        }

        while (a.size() != 1) {
            while (!a.isEmpty()) {
                long curIdx, curSize, tempSize;
                long[] curCell = a.pollFirst();
                curIdx = curCell[0];
                curSize = curCell[1];
                tempSize = curSize;

                if (!temp.isEmpty() && temp.peekLast()[1] <= curSize) {
                    tempSize += temp.pollLast()[1];
                }

                if (!a.isEmpty() && a.peekFirst()[1] <= curSize) {
                    tempSize += a.pollFirst()[1];
                }

                temp.addLast(new long[]{curIdx, tempSize});
            }
            a = temp;
            temp = new LinkedList<>();
        }
        System.out.println(a.getFirst()[1]);
        System.out.println(a.getFirst()[0]);
    }
}
