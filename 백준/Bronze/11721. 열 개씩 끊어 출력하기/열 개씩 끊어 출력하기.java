import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String N = sc.next();

        for(int i = 0; i<N.length(); i=i+10){
            if(i+10 < N.length()){
                System.out.println(N.substring(i,i+10));
            }
            else{
                System.out.println(N.substring(i));
            }
        }


    }
}