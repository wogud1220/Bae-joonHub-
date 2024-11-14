import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char[] charArr = str.toCharArray();
        int count = 0;
        //char[] = {"W", "A"}
        for(int i = 0; i<charArr.length; i++){
            if(charArr[i] <= 'C') //C보다 작으면
                count+=3;
            else if (charArr[i]<='F') {
                count+=4;
            } else if (charArr[i]<='I') {
                count+=5;
            } else if (charArr[i]<='L') {
                count+=6;
            } else if (charArr[i]<='O') {
                count+=7;
            } else if (charArr[i]<='S') {
                count+=8;
            } else if (charArr[i]<='V') {
                count+=9;
            } else if (charArr[i]<='Z') {
                count+=10;
            }
        }

        System.out.println(count);





    }
}