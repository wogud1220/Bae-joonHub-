import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int a2, b2, c2;
        while(true){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            if (a == 0 && b == 0 && c == 0) {
                break;
            }
            a2 = a*a;
            b2 = b*b;
            c2 = c*c;
            if(a2 + b2 == c2) System.out.println("right");
            else if(a2 + c2 == b2) System.out.println("right");
            else if(b2 + c2 == a2) System.out.println("right");
            else System.out.println("wrong");
        }
    }
}