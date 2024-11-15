import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        int N = sc.nextInt();
        Set<Integer> set = new HashSet<>();
        //O(M+N)으로 단축...
        for (int i = 0; i < N; i++) {
            set.add(sc.nextInt());
        }

        int M = sc.nextInt();
        int[] arr2 = new int[M];
        for(int i = 0; i< M ; i++){
            arr2[i] = sc.nextInt();
        }

        for(int i = 0; i<M; i++){
            boolean dap = false;
            if(set.contains(arr2[i])) dap = true;
            if(dap) System.out.println("1");
            else System.out.println("0");
        }

    }
}