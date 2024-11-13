import java.io.IOException;
import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String str = sc.next();
            String[] arr = str.split("");
            int left = 0;
            boolean flag = true;
            for(int j = 0; j<arr.length; j++){
                if(arr[j].equals("(")) left++;
                else {
                    left--;
                    if (left < 0) { // 닫는 괄호가 먼저 나오면 잘못된 괄호
                        flag = false;
                        break;
                    }
                }
            }
            if(flag && left == 0) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}