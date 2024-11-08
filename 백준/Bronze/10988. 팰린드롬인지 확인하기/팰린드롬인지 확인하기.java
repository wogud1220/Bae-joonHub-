import java.util.*;
public class Main {
    public static void  main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 1;
        String sc1 = sc.nextLine();
        for (int i = 0; i < sc1.length()/2; i++) {
            if (sc1.charAt(i) != sc1.charAt(sc1.length() - 1 - i)) {
                answer  =0;
            }
        }
        System.out.println(answer);

    }
}