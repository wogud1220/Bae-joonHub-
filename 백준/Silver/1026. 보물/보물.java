import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[N];
        int answer = 0;
        //a 입력
        for(int i = 0; i<N; i++){
            A[i] = sc.nextInt();
        }
        //b 입력
        for(int i = 0; i<N; i++){
            B[i] = sc.nextInt();
        }
        Arrays.sort(A);
        Arrays.sort(B);




        for(int i = 0; i<N; i++){
            answer += A[i] * B[N-i-1];
        }


        System.out.println(answer);








    }
}