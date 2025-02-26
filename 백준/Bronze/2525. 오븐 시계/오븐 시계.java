import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt(); // 시간
        int B = sc.nextInt(); // 분
        int C = sc.nextInt(); // 추가할 분

        A += C / 60; // C를 60으로 나눈 몫(추가할 시간)
        B += C % 60; // C를 60으로 나눈 나머지(추가할 분)

        if (B >= 60) {
            A += B / 60; // 초과한 분을 시간으로 올림
            B = B % 60; // 60으로 나눈 나머지(새로운 분)
        }

        A = A % 24; // 24시간을 넘어가면 0시부터 시작

        // 출력
        System.out.println(A + " " + B);
    }
}