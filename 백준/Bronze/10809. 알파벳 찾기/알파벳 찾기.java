import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        char[] arr = str.toCharArray();
        int[] index = new int[arr.length];
        for(int i = 0; i<26;i++){
            System.out.print(str.indexOf((char)97+i)+" ");
        }

    }
}
