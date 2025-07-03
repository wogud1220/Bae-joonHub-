import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        int X = sc.nextInt();
        int N = sc.nextInt();

        int[] stuff = new int[N];
        int[] num = new int[N];

        for(int i = 0; i<N; i++){
            stuff[i] = sc.nextInt();
            num[i] = sc.nextInt();
        }
        int answer = 0;
        for(int i = 0; i<N; i++){
            answer +=stuff[i] * num[i];
        }

        System.out.println(answer == X ? "Yes" :"No");





    }
}