import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    private static int[] degrees;
    private static int N;

    private void input() {
        Scanner scanner = new Scanner(System.in);
        String s;

        s = scanner.nextLine();
        N = Integer.parseInt(s);

        s = scanner.nextLine(); // 2 3 1 2 2
        String[] split = s.split(" ");
        degrees = Arrays.stream(split)
                .mapToInt(Integer::parseInt)
                .toArray();
    }

    private int solve(int n, int[] ints) {
        // X인 모험가가 한 그룹 X명 이상
        // 공포도가 2인 모험가는 반드시 2명이상이 있는 모험가 그룹에 참여
        // 공포도가 가장 높은 모험가가 5라고 하면, 5명을 무조건 포섭 -> 이걸 가장 공포도 높은 순으로 포섭

        int[] ints1 = Arrays.stream(ints)
                .sorted()
                .toArray();

        int i = ints1.length-1; // 마지막
        int maxi;
        int answer = 0;
        while (i >= 0){
            maxi = ints1[i]; //  1 2 2 2 3 -> maxi 4번째 index
            i = i - maxi; // 4-1 1번째 인덱스 -> 2
            answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.input();
        int result = solution.solve(N, degrees);

        System.out.println(result);

        // test
//        int result = solution.solve(5, new int[]{2, 3, 1, 2, 2});
//        int answer = 2;
//        System.out.println(result + " " + Integer.compare(result, answer));
//

    }

}
