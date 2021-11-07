import java.util.HashMap;
import java.util.Map;
// https://programmers.co.kr/learn/courses/30/lessons/43165?language=java


public class programmers_43165 {

    public static void main(String[] args) {
        programmers_43165 problem = new programmers_43165();
        int solution = problem.solution(new int[]{1, 1, 1, 1, 1}, 3);
        System.out.println("solution  = " + solution + " " + Integer.compare(solution, 5));
    }

    public int solution(int[] numbers, int target) {
        int[] accumulated = new int[numbers.length];
        Map<Integer, Integer> saver;
        Map<Integer, Integer> last = new HashMap<>();

        int temp = 0;
        for (int i = numbers.length - 1; i >= 0; i--) {
            accumulated[i] = temp;
            temp += numbers[i];
        }

        last.put(0, 1);
        for (int i = 0; i < numbers.length; i++) {
            int cur = numbers[i];
            saver = new HashMap<>();
            for (Integer integer : last.keySet()) {
                Integer count = last.get(integer);
                if (cur + integer <= accumulated[i] + target) {
                    saver.put(cur + integer, saver.getOrDefault(cur + integer, 0) + count);
                }
                if (integer - cur >= target - accumulated[i]) {
                    saver.put(integer - cur, saver.getOrDefault(integer - cur, 0) + count);
                }
            }
            last = saver;
        }

        return last.getOrDefault(target, 0);
    }

}
