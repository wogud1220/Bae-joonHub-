import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str;
        String[] arr;
        int N = sc.nextInt();
        str = String.valueOf(N);

        arr = str.split("");
        Arrays.sort(arr);
        for(int i = arr.length-1; i >= 0; i--){
            System.out.print(arr[i]);
        }
    }
}