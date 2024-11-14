import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        String str = sc.next();
        int num = sc.nextInt();
        System.out.println(str.charAt(num-1));

    }
}