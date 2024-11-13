import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            String str = sc.next();
            for (int j = 0; j < str.length(); j++) {
                for (int k = 0; k < num; k++) {
                    System.out.print(str.charAt(j));
                }

            }
            System.out.println("");
        }
    }
}
