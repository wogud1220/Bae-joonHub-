import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int answer=0;


        for (int i = 0; i < N; i++) {
            int[] arr = new int[26];
            String str = sc.next();//happy 입력받고
            str = str.toUpperCase();//대문자로 바꾸고
            char[] ch = str.toCharArray(); //['H' 'A', 'P']로 바꾸고
            boolean dap = true;


            for(int j = 0; j<ch.length; j++){
                //두번 나오는데 연속된 것이 아니라면
                if(j > 0 && arr[ch[j] - 65] > 0 && ch[j-1] != ch[j]){
                    dap = false;
                    break;
                }
                else
                    arr[ch[j] - 65]++;
            }
            answer = dap? answer+1:answer;

        }
        System.out.println(answer);
    }
}