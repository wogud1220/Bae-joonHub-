import java.io.IOException;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String[] lecture = new String[20];
        double[] gpa = new double[20];
        double[] grade = new double[20];
        String alpha;
        for (int i = 0; i < 20; i++) {
            lecture[i] = sc.next();
            gpa[i] = sc.nextDouble();
            alpha = sc.next();
            if(alpha.equals("A+")) grade[i] = 4.5;
            else if (alpha.equals("A0")) grade[i] = 4.0;
            else if (alpha.equals("B+")) grade[i] = 3.5;
            else if (alpha.equals("B0")) grade[i] = 3.0;
            else if (alpha.equals("C+")) grade[i] = 2.5;
            else if (alpha.equals("C0")) grade[i] = 2.0;
            else if (alpha.equals("D+")) grade[i] = 1.5;
            else if (alpha.equals("D0")) grade[i] = 1.0;
            else if (alpha.equals("F")) grade[i] = 0.0;
            else if (alpha.equals("P")){
                grade[i] = 100.0;
                gpa[i] = 0;
            }
        }
        double[] answer = new double[20];
        int pcnt = 0;
        for(int i = 0; i<20; i++){
            if(grade[i]==100)//P일 경우엔
                continue;
            else
                answer[i] = gpa[i] * grade[i];
        }
        System.out.println(Arrays.stream(answer).sum()/(Arrays.stream(gpa).sum())); //다 더하고
    }
}