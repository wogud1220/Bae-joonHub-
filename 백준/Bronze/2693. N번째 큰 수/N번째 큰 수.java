import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        //test case 입력
        int T = sc.nextInt();
        for(int t = 0; t<T; t++) {
            // 배열의 원소 입력
            for (int i = 0; i < 10; i++) {
                arr[i] = sc.nextInt();
            }
            int n = 10;
            int least = 0;
            int temp = 0;
            //selection sort
            for (int i = 0; i < n - 1; i++) {
                least = i;
                for (int j = i + 1; j < n; j++) {
                    //j(우측)이 더 크다면
                    if (arr[least] > arr[j]) {
                        least = j; //최소값 인덱스 변경
                    }
                }
                temp = arr[least];
                arr[least] = arr[i];
                arr[i] = temp;
            }
            System.out.println(arr[7]);
        }




    }
}