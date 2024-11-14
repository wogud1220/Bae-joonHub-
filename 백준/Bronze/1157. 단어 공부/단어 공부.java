import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        str = str.toUpperCase();
        char[] arr = str.toCharArray();
        int[] answer = new int[26];
        for(int i = 0; i<arr.length; i++){
            answer[arr[i]- 65]++;
        }
        int max = Arrays.stream(answer).max().orElseThrow();
        int cnt = 0;
        int maxIndex =0;
        for(int i = 0; i<26; i++){
            if(max == answer[i]){
                cnt++;
                maxIndex = i;
            }
        }

        if(cnt>=2) System.out.println("?");
        else System.out.println((char)(65+maxIndex));


    }
}