import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N+1];
        int temp = 0;
        for(int i = 1; i<=N;i++){
            arr[i] = i;
        }
        for(int i = 1; i<=M; i++){

            int a = sc.nextInt();
            int b = sc.nextInt();
            temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }
        for(int i = 1; i<=N; i++){
            System.out.println(arr[i]);
        }
    }
}
