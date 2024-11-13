import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N+1];
        int a,b,c = 0;
        for(int i = 1; i<=M; i++){
            a = sc.nextInt();
            b = sc.nextInt();
            c = sc.nextInt();

            for(int j = a; j<=b;j++){
                arr[j] = c;
            }

        }
        for(int i = 1; i<=N;i++){
            System.out.print(arr[i]+" ");
        }

    }
}
