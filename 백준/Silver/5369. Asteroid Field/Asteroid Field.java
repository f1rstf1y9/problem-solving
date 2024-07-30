import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int m = sc.nextInt();
            String[] grid = new String[m];
            for (int j = 0; j < m; j++) {
                grid[j] = sc.next();
            }


            int[] start = new int[2];
            int[] end = new int[2];

            for (int r = 0; r < m; r++) {
                for (int c = 0; c < m; c++) {
                    if (grid[r].charAt(c) == 's') {
                        start[0] = r;
                        start[1] = c;
                    }
                    if (grid[r].charAt(c) == 'd') {
                        end[0] = r;
                        end[1] = c;
                    }
                }
            }

            boolean[][] visited = new boolean[m][m];
            for (int j = 0; j < m; j++) {
                Arrays.fill(visited[j], false);
            }

            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[] {start[0], start[1], 0});
            visited[start[0]][start[1]] = true;

            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, -1, 0, 1};

            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                if (cur[0] == end[0] && cur[1] == end[1]) {
                    System.out.println(cur[2]);
                    break;
                }
                for (int j = 0; j < 4; j++) {
                    int nx = cur[0] + dx[j];
                    int ny = cur[1] + dy[j];
                    if (0 <= nx && nx < m && 0 <= ny && ny < m
                            && !visited[nx][ny] && grid[nx].charAt(ny) != '*') {
                        visited[nx][ny] = true;
                        queue.add(new int[] {nx, ny, cur[2]+1});
                    }
                }
            }

            if (!visited[end[0]][end[1]]) {
                System.out.println(-1);
            }
        }
    }
}