import java.util.*;
public class Main {
    public static void  main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int times = sc.nextInt();
        String[] str = new String[times];
        String s1 = "";
        for(int i = 0; i<times; i++){
            str[i] = sc.next();
        }
        for (int i= 0; i<times; i++){
            s1 = str[i];
            s1 = String.valueOf(s1.charAt(0)) + String.valueOf(s1.charAt(s1.length()-1));
            System.out.println(s1);
        }

    }
}