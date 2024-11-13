import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        str = str.trim(); // 앞뒤 공백 제거
        
        // 공백이 제거된 문자열이 빈 문자열인지 확인
        if (str.isEmpty()) {
            System.out.println(0);
        } else {
            // \\s+를 사용하여 여러 개의 공백을 하나의 공백으로 간주
            String[] arr = str.split("\\s+");
            int answer = arr.length;
            System.out.println(answer);
        }
    }
}