import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
//        int N = sc.nextInt();
//        int M = sc.nextInt();

        String[][] array1 = new String[5][15];
        String answer = "";
        String a;
        for (int i = 0; i < 5; i++) {
            a = sc.next();
            for (int j = 0; j < a.length(); j++) {
                array1[i][j] = String.valueOf(a.charAt(j));
            }
        }
        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (array1[j][i] != null) {  // null 체크
                    answer = answer.concat(array1[j][i]);
                }
            }
        }
        System.out.println(answer);
    }
}