import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        for(int i=0; i<5; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println((Arrays.stream(arr).sum())/5);
        Arrays.sort(arr);
        System.out.println(arr[2]);
    }
}