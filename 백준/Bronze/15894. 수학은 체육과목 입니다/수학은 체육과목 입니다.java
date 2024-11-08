import java.util.*;
public class Main {
    public static void  main(String[] args) {

        long hap = 0;
        Scanner sc = new Scanner(System.in);
        long square = sc.nextInt();

        hap = square + 1 + (square*2) + (square-1);
                //밑 + 윗 + 옆 + 짧은 선
        System.out.println(hap);
    }
}