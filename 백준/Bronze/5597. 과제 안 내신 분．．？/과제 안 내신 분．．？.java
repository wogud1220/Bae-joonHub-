import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[28];

        for (int i = 0; i < 28; i++) {
            arr[i] = sc.nextInt();
        }//배열 정렬하고
        Arrays.sort(arr);
        int index = 0;
        for (int i = 1; i <= 30; i++) {
            if (index < 28 && arr[index] == i) {
                // 배열에 숫자가 존재하면 다음 인덱스로 이동
                index++;
            } else {
                System.out.println(i);
            }
        }
    }
}
