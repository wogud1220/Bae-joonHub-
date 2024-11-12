import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {//약수라면
                count++; //약수 개수 증가
                if (count == K) {
                    System.out.println(i);
                    break;
                }
            }

        }//for문 끝
        if (count < K) {
            System.out.println(0);
        }
    }

    }