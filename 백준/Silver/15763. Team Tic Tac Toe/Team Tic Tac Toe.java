import java.util.Scanner;

public class Main {
    public static char[][] tictactoe;

    public static int countVictory(char[][] tictactoe, char team) {
        int count = 0;

        for (int i = 0; i < 3; i++) {
            int j;
            for (j = 0; j < 3; j++) {
                if (tictactoe[i][j] != team) {
                    break;
                }
            }
            if (j == 3) {
                count++;
            }
        }
        for (int i = 0; i < 3; i++) {
            int j;
            for (j = 0; j < 3; j++) {
                if (tictactoe[j][i] != team) {
                    break;
                }
            }
            if (j == 3) {
                count++;
            }
        }
        if (team == tictactoe[0][0] && tictactoe[0][0] == tictactoe[1][1] && tictactoe[1][1] == tictactoe[2][2]) count++;
        if (team == tictactoe[0][2] && tictactoe[0][2] == tictactoe[1][1] && tictactoe[1][1] == tictactoe[2][0]) count++;

        return count;
    }

    public static char[][] makeNewTictactoe(char a, char b) {
        char[][] newTictactoe = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tictactoe[i][j] == b) {
                    newTictactoe[i][j] = a;
                } else {
                    newTictactoe[i][j] = tictactoe[i][j];
                }
            }
        }
        return newTictactoe;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        tictactoe = new char[3][3];
        String alphabets = "";

        int singleVictory = 0;
        int teamVictory = 0;

        for (int i = 0; i < 3; i++) {
            String s = sc.next();
            for (int j = 0; j < 3; j++) {
                char c = s.charAt(j);
                tictactoe[i][j] = c;
                if (!alphabets.contains(String.valueOf(c))) {
                    alphabets += c;
                }
            }
        }

        int[] singleVictoryArr = new int[alphabets.length()];
        for (int i = 0; i < alphabets.length(); i++) {
            singleVictoryArr[i] = countVictory(tictactoe, alphabets.charAt(i));
            if (singleVictoryArr[i] > 0) {
                singleVictory++;
            }
        }

        for (int i = 0; i < alphabets.length()-1; i++) {
            for (int j = i+1; j < alphabets.length(); j++ ) {
                char a = alphabets.charAt(i);
                char b = alphabets.charAt(j);
                char[][] newTictactoe = makeNewTictactoe(a, b);
                int victoryCount = countVictory(newTictactoe, a);
                if (victoryCount - singleVictoryArr[i] - singleVictoryArr[j] > 0) {
                    teamVictory++;
                }
            }
        }
        System.out.println(singleVictory);
        System.out.println(teamVictory);
    }
}