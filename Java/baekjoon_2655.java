// 2655

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Block{

    int square;
    int height;
    int weight;
    int index;
    static int INDEX = 1;

    public Block(int square, int height, int weight) {
        this.square = square;
        this.height = height;
        this.weight = weight;
        this.index = INDEX;
        INDEX++;
    }

    public int sort_key(int limit){
        return this.square * limit + this.weight;
    }
    @Override
    public String toString() {
        return "Block{" +
                "square=" + square +
                ", height=" + height +
                ", weight=" + weight +
                ", index=" + index +
                '}';
    }
}

public class Main {
    private static final int LIMIT = 10001;
    List<Block> blockList = new ArrayList<>();

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int[] ints = Arrays.stream(s)
                    .mapToInt(Integer::parseInt)
                    .toArray();
            blockList.add(new Block(ints[0], ints[1], ints[2]));
        }
    }

    public void solve() throws IOException {
        input();
        _solve();
    }

    private void _solve(){
        int size = blockList.size();
        blockList.sort(Comparator.comparingInt(o -> o.sort_key(LIMIT)));
        int[][] cur = new int[size][2];
        int cur_weight, j_weight;
        int cur_height, last_height;

        for (int i = 0; i < size; i++) {
            cur[i][0] = blockList.get(i).height;
            cur[i][1] = -1;
        }

        for (int i = 0; i < size; i++) {
            cur_weight = blockList.get(i).weight;
            cur_height = blockList.get(i).height;
            for (int j = 0; j < i; j++) {
                j_weight = blockList.get(j).weight;
                last_height = cur[j][0];
                if (j_weight <= cur_weight && cur[i][0] < cur_height + last_height) {
                    cur[i][0] = cur_height + last_height;
                    cur[i][1] = j;
                }
            }
        }

        int max_val = 0;
        int idx = -1;

        for (int i = 0; i < size; i++) {
            if (max_val < cur[i][0]){
                max_val = cur[i][0];
                idx = i;
            }
        }

        List<Integer> answer = new ArrayList<>();
        while (idx != -1){
            answer.add(blockList.get(idx).index);
            idx = cur[idx][1];
        }
        System.out.println(answer.size());
        for (int i = answer.size()-1; i >= 0; i--) {
            System.out.println(answer.get(i));
        }
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
//        main.test();
        main.solve();
    }

    public void test(){
        blockList.add(new Block(25, 3, 4));
        blockList.add(new Block(4, 4, 6));
        blockList.add(new Block(9, 2, 3));
        blockList.add(new Block(16, 2, 5));
        blockList.add(new Block(1, 5, 2));

        _solve();
    }
}

/*
3
1 1 1
2 2 2
3 3 3
답: 1 2 3

3
2 1 3
1 1 2
3 3 1
답: 1 3
*/