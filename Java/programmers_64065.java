import java.util.*;

class programmers_64065 {
    //class Solution {
    public int[] solution(String s) {
        int length = s.length();
        char open = '{';
        char close = '}';

        Set<Integer> result = new LinkedHashSet<>();
        PriorityQueue<String> tuples = new PriorityQueue<>((o1, o2) -> o1.length() - o2.length());
        int srt = 0;

        for (int i = 1; i < length-1; i++) {
            if (s.charAt(i) == open){
                srt = i+1;
                continue;
            }
            if (s.charAt(i) == close){
                String substring = s.substring(srt, i);
                tuples.add(substring);
            }
        }

        while (!tuples.isEmpty()){
            String cur = tuples.poll();
            int[] elements = Arrays.stream(cur.split(","))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            for (int element : elements) {
                if (result.contains(element)){
                    continue;
                }
                result.add(element);
            }

        }
        return result.stream().mapToInt(v -> v).toArray();
    }

    public static void main(String[] args) {

    }
}