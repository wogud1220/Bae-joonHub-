import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char[] chArr = str.toCharArray();
        int count=0;
        for(int i = 0; i<chArr.length; i++){
            if(i+1< chArr.length) {
                if (chArr[i] == 'c' && chArr[i + 1] == '=' || chArr[i + 1] == '-') {
                    count++;
                    i++;
                    continue;
                } else if (chArr[i] == 'd' && chArr[i + 1] == '-') {
                    count++;
                    i++;
                    continue;
                } else if (chArr[i] == 'l' && chArr[i + 1] == 'j') {
                    count++;
                    i++;
                    continue;
                } else if (chArr[i] == 'n' && chArr[i + 1] == 'j') {
                    count++;
                    i++;
                    continue;
                } else if (chArr[i] == 's' && chArr[i + 1] == '=') {
                    count++;
                    i++;
                    continue;
                } else if (chArr[i] == 'z' && chArr[i + 1] == '=') {
                    count++;
                    i++;
                    continue;
                }

            }
                if(i+2<chArr.length) {
                    if (chArr[i] == 'd' && chArr[i + 1] == 'z' && chArr[i + 2] == '=') {
                        count++;
                        i += 2;
                        continue;
                    }
                }
            //나머지 한 글자들
            count++;
        }

        System.out.println(count);


    }
}