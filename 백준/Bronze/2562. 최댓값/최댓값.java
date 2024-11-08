import java.util.*;
public class Main {
    public static void  main(String[] args) {

    int max = 0;
    int n = 0;
    int index = 0;
     Scanner scanner = new Scanner(System.in);
     for(int i = 0; i<9;i++){
         n = scanner.nextInt();
         if(n>max){
             max = n;
             index = i;
         }
     }
        System.out.println(max);
        System.out.println(index+1);
    }
}