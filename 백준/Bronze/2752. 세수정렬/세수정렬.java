import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[3];
        for(int i = 0; i<3; i++){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        for (int i = 0; i < 3; i++) {
            System.out.print(arr[i]+" ");
        }

    }

    }