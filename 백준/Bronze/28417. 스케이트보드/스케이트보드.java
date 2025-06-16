import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //인원수 받고
        int N =  sc.nextInt();

        int dap = 0;


        int[] arr = new int[7];


        for(int n = 0; n<N; n++) {
            for (int i = 0; i < 7; i++) {
                arr[i] = sc.nextInt();
            }
            //런 최고점수
            int runMax = Math.max(arr[0], arr[1]);
            //트릭 최고 점수
            int[] trickArr = new int[5];
            int j = 2;
            for (int i = 0; i < 5; i++) {
                trickArr[i] = arr[j];
                j++;
            }

            Arrays.sort(trickArr);
            int total = trickArr[4] + trickArr[3] + runMax;
            dap = Math.max(total, dap);
        }


        System.out.println(dap);


    }
}