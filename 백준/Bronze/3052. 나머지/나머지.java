import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }

        Set<Integer> answerSet = new HashSet<>();

        for (int i = 0; i < 10; i++) {
            answerSet.add(arr[i]%42);
        }
        System.out.println(answerSet.size());


    }

}