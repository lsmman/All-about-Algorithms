import java.util.Scanner;

public class baekjoon_1439 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().strip() + " ";
        char c = input.charAt(0);
        int ones = 0;
        int zeros = 0;

        for (int i = 1; i < input.length(); i++){
            if (input.charAt(i) != c){
                if (c == '1') ones++;
                if (c == '0') zeros++;

                c = input.charAt(i);
            }
        }
       
        System.out.println(Math.min(ones, zeros));
    }
}