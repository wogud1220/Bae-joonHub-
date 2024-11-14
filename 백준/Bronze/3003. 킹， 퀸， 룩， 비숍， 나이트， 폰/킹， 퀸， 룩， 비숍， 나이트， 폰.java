import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int pone = 8;
        int first = 1;
        int rest = 2;

        int[] arr = new int[6];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        for(int i =0; i<arr.length; i++){
            if(i == arr.length - 1) System.out.print(pone-arr[i]);
            else if(i>1) System.out.print(rest - arr[i]+" ");
            else System.out.print(first-arr[i]+" ");
        }
    }
}