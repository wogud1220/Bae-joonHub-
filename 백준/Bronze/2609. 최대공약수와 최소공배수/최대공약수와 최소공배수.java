import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int yaksu = GCD(a,b);
        int basu = a*b/yaksu;

        System.out.println(yaksu);
        System.out.println(basu);

    }
    static int GCD(int a, int b){
        if(b==0){
            return a;
        }
        return GCD(b,a%b);
    }






}
