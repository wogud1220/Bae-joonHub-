import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();
        if (M < 45 && H == 0){
            M = 60 + M - 45;
            H = 23;
        }
        else if(M <45){
            M = 60 + M - 45;
            H = H - 1;
        }
        else {
            M = M - 45;
        }

        System.out.println(H + " " + M);

        }
}