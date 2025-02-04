import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] array1 = new int[N][M];


        for(int i = 0; i<N; i++){
            for(int j = 0; j<M; j++){
                array1[i][j] = sc.nextInt();
            }
        }

        int[][] array2 = new int[N][M];

        for(int i = 0; i<N; i++){
            for(int j = 0; j<M; j++){
                array2[i][j] = sc.nextInt();
            }
        }

        for(int i = 0; i<N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(array1[i][j] + +array2[i][j]+" ");
            }
            System.out.println("");
        }





        }

    }