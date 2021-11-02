import java.util.Arrays;

public class programmers_43238 {
    public static void main(String[] args) {
        programmers_43238 solutionObj = new programmers_43238();
        long solution = solutionObj.solution(6, new int[]{7, 10});
        System.out.println(solution + " " + Long.compare(28L, solution));

    }

    public long solution(int nInt, int[] timesInt) {
        long answer, left, right, cur_n;
        long n = (long)nInt;
        left = 0;
        right = n * (long) Arrays.stream(timesInt)
                .min()
                .orElse(1);
        answer = right;
//        이분탐색..

        while (left <= right){
            long mid = (left + right) / 2;
            cur_n = findCountJudgeablePerson(timesInt, mid);
            if (cur_n < n){
                left = mid + 1;
            }
            else { // cur_n >= n
                answer = Math.min(mid, answer);
                right = mid - 1;
            }
        }
        return answer;
    }

    private long findCountJudgeablePerson(int[] timesInt, long mid) {
        long count = 0;
        for (int t : timesInt) {
            count += (long) (mid / t);
        }
        return count;
    }

}
