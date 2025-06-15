import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int[] arr1 = {A,B,C};
        Arrays.sort(arr1);
        System.out.println(arr1[1]);

    }
}