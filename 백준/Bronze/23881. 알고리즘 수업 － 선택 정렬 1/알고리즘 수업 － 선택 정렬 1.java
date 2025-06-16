import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 배열 크기
        int K = sc.nextInt(); // K번째 교환 추적
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int cnt = 0;
        for (int last = N - 1; last >= 1; last--) {
            int maxIdx = 0;
            for (int i = 1; i <= last; i++) {
                if (A[i] > A[maxIdx]) {
                    maxIdx = i;
                }
            }

            if (maxIdx != last) {
                // 실제 교환 발생
                int temp = A[last];
                A[last] = A[maxIdx];
                A[maxIdx] = temp;
                cnt++;

                if (cnt == K) {
                    int x = Math.min(A[last], A[maxIdx]);
                    int y = Math.max(A[last], A[maxIdx]);
                    System.out.println(x + " " + y);
                    return;
                }
            }
        }
        //-1
        System.out.println(-1);
    }
}