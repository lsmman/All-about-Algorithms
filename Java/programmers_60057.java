// https://programmers.co.kr/learn/courses/30/lessons/60057?language=java#

import java.lang.Math;

class Solution {
    public int solution(String s) {
        String cur = "";
        String pre = "";
        int cnt, length, unit;
        int term, idx;
        int n = s.length();
        int answer = n;

        unit = (int) (n / 2);
        s = s + " " + s;

        for (term = 1; term <= unit; term++) {
            pre = s.substring(0, term);
            cnt = 1;
            length = 0;
            for (idx = term; idx <= n; idx += term) {
                cur = s.substring(idx, idx + term);
                if (cur.equals(pre)) {
                    cnt += 1;
                    continue;
                }

                if (cnt > 1) {
                    length += Integer.toString(cnt).length();
                }

                length += term;
                cnt = 1;
                pre = cur;
            }
            length += n % term;
            answer = Math.min(answer, length);
        }
        return answer;
    }
}