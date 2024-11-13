import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        StringBuilder sb_a = new StringBuilder(String.valueOf(a));
        StringBuilder sb_b = new StringBuilder(String.valueOf(b));
        sb_a.reverse();
        sb_b.reverse(); //뒤집고
        //정수로 변환
        a = Integer.parseInt(sb_a.toString());
        b = Integer.parseInt(sb_b.toString());

        int answer = a > b ? a : b;
        System.out.println(answer);


    }
}
