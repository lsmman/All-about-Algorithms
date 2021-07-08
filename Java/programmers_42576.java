// 프로그래머스 해쉬 완수하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576?language=java

import java.util.*;


class Solution {
    public static String solution(String[] p, String[] c) {
        HashMap<String, Integer> hm = new HashMap<>();
        for (String s: p) {
            if (!hm.containsKey(s)) {
                hm.put(s, 1);
            }
            else {
                hm.replace(s, hm.get(s)+1);
            }
        }
        for (String s: c) {
            hm.replace(s, hm.get(s)-1);
        }
        String answer = "";
        for (Map.Entry<String, Integer> set : hm.entrySet()) {
            if (set.getValue() > 0){
                answer = set.getKey();
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] p = {"l", "k", "e"};
        String[] c = {"e", "k"};
        System.out.println(Solution.solution(p, c).equals("l"));

        String[] p2 = {"k", "k", "e"};
        String[] c2 = {"e", "k"};
        System.out.println(Solution.solution(p2, c2).equals("k"));
    }
/*
// 키가 중복되어 충돌이 일어나는 경우 Hashtable이나 HashMap은 감당이 안된다.
// 순서를 보장하는 LinkedHashMap을 사용해보자

    public static String solution(String[] participant, String[] completion) {
        Hashtable<String, Integer> ht = new Hashtable<String, Integer>();
        boolean[] check = new boolean[participant.length];
        for (int i = 0; i < participant.length; i++){
            ht.put(participant[i], i);
        }

        for (String tmp : completion) {
            check[ht.get(tmp)] = true;
        }

        String answer = "";
        for (int i = 0; i< check.length; i++){
            if (!check[i] ){
                answer = participant[i];
                break;
            }
        }

        return answer;
    }
*/
}
