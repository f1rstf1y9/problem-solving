import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] words = new String[2*N-2];
        String[] sortedWords = new String[2*N-2];
        sc.nextLine();
        for (int i = 0; i < 2*N-2; i++) {
            words[i] = sc.nextLine();
            sortedWords[i] = words[i];
        }

        Arrays.sort(sortedWords, (String o1, String o2) -> {return o1.length()-o2.length();});

        if (N==2) {
            System.out.println(words[0]+words[1]);
            System.out.println("PS");
        } else {
            String curStr = "";
            if (sortedWords[2*N-4].substring(1,N-2).equals(sortedWords[2*N-3].substring(0,N-3))) {
                curStr = sortedWords[2*N-4]+sortedWords[2*N-3].charAt(N-2);

                for (int i = 1; i < N-1; i++) {
                    if (!(curStr.substring(0,i).equals(sortedWords[2*(i-1)]) && curStr.substring(N-i, N).equals(sortedWords[2*(i-1)+1]))
                            && !(curStr.substring(0,i).equals(sortedWords[2*(i-1)+1]) && curStr.substring(N-i, N).equals(sortedWords[2*(i-1)]))){
                        curStr = "";
                        break;
                    }
                }
            }

            if (curStr.isEmpty()){
                curStr = sortedWords[2*N-3]+sortedWords[2*N-4].charAt(N-2);
            }

            System.out.println(curStr);

            boolean[] headUsed = new boolean[N-1];
            Arrays.fill(headUsed, false);

            for (int i = 0; i < 2* N-2; i++) {
                int len = words[i].length();

                if (words[i].equals(curStr.substring(0, len)) && !headUsed[len-1]) {
                    headUsed[len-1] = true;
                    System.out.print("P");
                } else {
                    System.out.print("S");
                }
            }

        }
    }
}