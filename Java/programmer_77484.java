
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] ranks = new int[] {6, 6, 5, 4, 3, 2, 1};
        int low_cnt, high_cnt;

        low_cnt = 0;
        high_cnt = 0;
        for (int i = 0; i < lottos.length; i++){
            if (lottos[i] == 0){
                high_cnt++;
                continue;
            }
            for (int j = 0; j< win_nums.length; j++){
                if (win_nums[j] == lottos[i]){
                    low_cnt++;
                    high_cnt++;    
                    break;
                }
            }
        }

        return new int[] {ranks[high_cnt], ranks[low_cnt]};
    }
}
