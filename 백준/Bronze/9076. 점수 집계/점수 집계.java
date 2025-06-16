import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();// test case
        int[] arr = new int[5];
        //N번 반복
        for(int n = 0; n<N; n++) {
            int sum = 0;
            //배열에 값 넣기
            for (int i = 0; i < 5; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);

            //최저, 최고를 뺀 합.
            for(int i = 1; i<4; i++){
                sum+=arr[i];
            }
            //24 - 19
            if(arr[3] - arr[1] >= 4){
                System.out.println("KIN");
            }
            else {
                System.out.println(sum);
            }



        }

    }
}