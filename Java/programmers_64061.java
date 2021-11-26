import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

class programmers_64061 {
//class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int length = board.length;

        List<Deque<Integer>> deques = new ArrayList<>();
        Deque<Integer> queue = new LinkedList<>();

        for (int i = 0; i < length; i++) {
            deques.add(new LinkedList<>());
        }

        for (int col = 0; col < length; col++) {
            Deque<Integer> cur = deques.get(col);
            for (int row = 0; row < length; row++) {
                if (board[row][col] == 0){
                    continue;
                }
                cur.add(board[row][col]);
            }
        }

        for (int move : moves) {
            move--;
            if (deques.get(move).isEmpty()){
                continue;
            }
            int moved = deques.get(move).pollFirst();
            if (!queue.isEmpty() && moved == queue.peekLast()){
                queue.pollLast();
                answer += 2;
                continue;
            }
            queue.add(moved);
        }
        return answer;
    }

    public static void main(String[] args) {
        int result = new programmers_64061().solution(new int[][]{{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}}, new int[]{1, 5, 3, 5, 1, 2, 1, 4});
        System.out.println(result + " " + (result-4));
    }
}