import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[][] milkCity = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                milkCity[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][][] milkDp = new int[N][N][3];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Arrays.fill(milkDp[i][j], 0);
            }
        }



        boolean firstDrink = false;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int curMilk = milkCity[i][j];
                int prevMilk = (curMilk+2)%3;
                if (!firstDrink) {
                    if (curMilk == 0) {
                        firstDrink = true;
                        milkDp[i][j][0] = 1;
                    }
                } else {
                    if (i == 0) {
                        milkDp[i][j][0] = milkDp[i][j-1][0];
                        milkDp[i][j][1] = milkDp[i][j-1][1] == 0 ? 0 : milkDp[i][j-1][1];
                        milkDp[i][j][2] = milkDp[i][j-1][2] == 0 ? 0 : milkDp[i][j-1][2];
                        if (curMilk != 0 && milkDp[i][j-1][prevMilk] == 0) continue;

                        milkDp[i][j][curMilk] = milkDp[i][j-1][prevMilk]+1;

                    } else if (j == 0) {
                        milkDp[i][j][0] = milkDp[i-1][j][0];
                        milkDp[i][j][1] = milkDp[i-1][j][1] == 0 ? 0 : milkDp[i-1][j][1];
                        milkDp[i][j][2] = milkDp[i-1][j][2] == 0 ? 0 : milkDp[i-1][j][2];
                        if (curMilk != 0 && milkDp[i-1][j][prevMilk] == 0) continue;
                        milkDp[i][j][curMilk] = milkDp[i-1][j][prevMilk]+1;
                    } else {
                        milkDp[i][j][0] = Math.max(milkDp[i-1][j][0], milkDp[i][j-1][0]);
                        milkDp[i][j][1] = Math.max(milkDp[i][j-1][1] == 0 ? 0 : milkDp[i][j-1][1], milkDp[i-1][j][1] == 0 ? 0 : milkDp[i-1][j][1]);
                        milkDp[i][j][2] = Math.max(milkDp[i][j-1][2] == 0 ? 0 : milkDp[i][j-1][2], milkDp[i-1][j][2] == 0 ? 0 : milkDp[i-1][j][2]);
                        if (curMilk == 0 || (milkDp[i][j-1][prevMilk] != 0)) {
                            milkDp[i][j][curMilk] = milkDp[i][j-1][prevMilk]+1;
                        }
                        if (curMilk == 0 || (milkDp[i-1][j][prevMilk] != 0)) {
                            milkDp[i][j][curMilk] = Math.max(milkDp[i][j][curMilk], milkDp[i-1][j][prevMilk]+1);
                        }
                    }

                }
            }
        }

        int answer = 0;
        for (int i = 0; i < 3; i++) {
            answer = Math.max(answer, milkDp[N-1][N-1][i]);
        }
        System.out.println(answer);
    }
}