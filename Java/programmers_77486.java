
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
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
import java.util.Map;
import java.util.HashMap;

class Solution {
    private int calc_profit(int amount){
        return 100 * amount;
    }

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amounts) {
        Map<String, Integer> name2idx = new HashMap<>();
        int N = enroll.length;
        int refer, amount, tip, center;
        int[] referralInt = new int[N];
        int[] profits = new int[N];

        for (int i = 0; i < N; i++){
            profits[i] = 0;
        }

        center = N;
        name2idx.put("-", center);
        for (int idx = 0; idx < N; idx++){
            name2idx.put(enroll[idx], idx);
        }

        for (int i = 0; i < N; i++){
            referralInt[i] = name2idx.get(referral[i]);
        }

        for (int i = 0; i< seller.length; i++){
            amount = calc_profit(amounts[i]);
            refer = name2idx.get(seller[i]);
            while (refer != center && amount > 0){
                tip = (int)(amount / 10);
                profits[refer] += amount - tip;

                refer = referralInt[refer];
                amount = tip;
            }

        }

        return profits;
    }
}