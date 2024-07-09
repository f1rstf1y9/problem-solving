import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static int M;
    public static int[][] models;
    public static int[] answer;
    public static int maxEstimate = 0;
    public static boolean isEnsembleBest = false;

    public static int[] ensemble(int[] modelList) {
        int[] result = new int[M];
        int count = modelList.length;

        for (int i = 0; i < M; i++) {
            int countZero = 0;
            int countOne = 0;

            for (int j = 0; j < count; j++) {
                if (models[modelList[j]][i] == 1) countOne++;
                else countZero++;
            }
            result[i] = countOne > countZero ? 1 : 0;
        }
        return result;
    }

    public static void checkEnsemble(int currentNum, int countNum, int start, int[] modelEnsemble ) {
        if (isEnsembleBest) return;

        if (countNum == currentNum) {
            int[] model = ensemble(modelEnsemble);

            int accuracy = 0;
            for (int i = 0; i < M; i++) {
                if (model[i] == answer[i]) accuracy++;
            }

            if (accuracy > maxEstimate) {
                maxEstimate = accuracy;
                isEnsembleBest = true;
            }

            return;
        }

        for (int i = start; i < N; i++) {
            modelEnsemble[currentNum] = i;
            checkEnsemble(currentNum+1, countNum, i+1, modelEnsemble);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer(br.readLine());
        N = Integer.parseInt(tokens.nextToken());
        M = Integer.parseInt(tokens.nextToken());

        answer = new int[M];
        tokens = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            answer[i] = Integer.parseInt(tokens.nextToken());
        }

        models = new int[N][M];
        int accuracy;
        for (int i = 0; i < N; i++) {
            accuracy = 0;
            tokens = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                models[i][j] = Integer.parseInt(tokens.nextToken());
                if (models[i][j] == answer[j]) {
                    accuracy++;
                }
            }
            maxEstimate = Math.max(maxEstimate, accuracy);
        }

        for (int i = 3; i <= N; i += 2) {
            checkEnsemble(0, i, 0, new int[i]);
        }

        if (isEnsembleBest) {
            System.out.print(1);
        } else {
            System.out.print(0);
        }
    }
}