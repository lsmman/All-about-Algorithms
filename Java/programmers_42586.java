// 프로그래머스 스택/큐 기능개발
// https://programmers.co.kr/learn/courses/30/lessons/42586?language=java


import java.util.*;

class programmers_42586 {
    public static int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        int remain, turn_needed;
        int cur, pre, last, i;
        int[] answer_arr;
        ArrayList<Integer> answer = new ArrayList<>();

        for (i =0 ; i < speeds.length; i++){

            remain = 100 - progresses[i];
            turn_needed = (int)(remain / speeds[i]);
            if (remain % speeds[i] > 0){
                turn_needed += 1;
            }
            q.offer(turn_needed);
        }

        pre = -1;
        last = -1;
        while (!q.isEmpty()) {
            cur = q.remove();
            if (pre >= cur) {
                answer.set(last, answer.get(last)+1);
            }
            else {
                answer.add(1);
                last++;
                pre = cur;
            }
        }
        answer_arr = new int[answer.size()];
        for (i = 0; i < answer.size(); i++) {
            answer_arr[i] = answer.get(i);
        }
        return answer_arr;
    }

    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        int[] answer = {2, 1};

        int[] s = programmers_42586.solution(progresses, speeds);
        for (int i : s) {
            System.out.println(i);
        }
        System.out.println(s.equals(answer));
    }

}
