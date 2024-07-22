import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] currentMatrix = new int[N][M];
        int[][] targetMatrix = new int[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                currentMatrix[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                targetMatrix[i][j] = line.charAt(j) - '0';
            }
        }

        int answer = 0;

        for (int i = 0; i < N-2; i++) {
            for (int j = 0; j < M-2; j++) {
                if (currentMatrix[i][j] != targetMatrix[i][j]) {
                    answer += 1;
                    for (int r = i; r < i+3; r++) {
                        for (int c = j; c < j+3; c++) {
                            if (currentMatrix[r][c] == 0) {
                                currentMatrix[r][c] = 1;
                            } else {
                                currentMatrix[r][c] = 0;
                            }
                        }
                    }
                 }
            }
        }

        boolean isCorrect = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (currentMatrix[i][j] != targetMatrix[i][j]) {
                    isCorrect = false;
                    break;
                }
            }
            if (!isCorrect) break;
        }

        System.out.println(isCorrect ? answer : -1);
    }
}