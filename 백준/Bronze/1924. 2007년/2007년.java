import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();


        int[] day = {31, 28, 31, 30, 31, 30, 31, 31 ,30, 31, 30, 31};
        String[] yo = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

        int totalDay = 0;
        for(int i = 0; i<x-1; i++){
            totalDay +=day[i];
        }
        totalDay+=y -1;

        System.out.println(yo[totalDay%7]);



    }
}