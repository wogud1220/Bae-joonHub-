import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M =sc.nextInt();
        int[] arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
            arr[i] = i;
        } //순서대로 저장

        int temp = 0;
        //역순으로 받을 번호 받기
        for(int i = 1; i<=M; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();


            //역순으로 변경
            for(int j = a; j<=b; j++){
                temp = arr[j];
                arr[j] = arr[b];
                arr[b] = temp;
                b--;
            }
        }
        for (int i = 1; i <=N ; i++) {
            System.out.print(arr[i]+" ");
        }

    }

}