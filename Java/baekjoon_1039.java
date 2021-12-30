// 참고 : https://ukyonge.tistory.com/119
import java.util.*;

public class baekjoon_1039 {
    static int num;
    static int length;
    static int k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] split = sc.nextLine().split(" ");
        sc.close();

        num = Integer.parseInt(split[0]);
        length = split[0].trim().length();
        k = Integer.parseInt(split[1]);

        bfs();
    }

    static void bfs() {
        Unit cur;
        int i, j;
        int swapResult;
        Queue<Unit> queue = new LinkedList<>();
        boolean[][] visit = new boolean[1000001][11];

        queue.add(new Unit(num, 0));
        visit[num][0] = true;
        while (!queue.isEmpty()){
            if (queue.peek().count == k) break;
            cur = queue.poll();

            for (i = 0; i < length; i++) {
                for (j = i+1; j < length; j++) {
                    swapResult = swapIfNotStartWithZero(cur.num, i, j);
                    if (swapResult == -1 || visit[swapResult][cur.count+1]) continue;
                    visit[swapResult][cur.count+1] = true;
                    queue.add(new Unit(swapResult, cur.count+1));
                }
            }
        }
        int answer = -1;
        while (!queue.isEmpty()){
            answer = Math.max(answer, queue.poll().num);
        }
        System.out.println(answer);
    }

    static int swapIfNotStartWithZero(int curNum, int a, int b) {
        int[] nums = new int[length];
        int result = 0;
        for (int i = length-1; i >= 0; i--) {
            nums[i] = curNum % 10;
            curNum = curNum / 10;
        }
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;

        if (nums[0] == 0){
            return -1;
        }

        for (int i = 0; i < length; i++) {
            result = result * 10 + nums[i];
        }
        return result;
    }

    private static class Unit {
        public int num;
        public int count;

        public Unit(int num, int count) {
            this.num = num;
            this.count = count;
        }
    }
}
