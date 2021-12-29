import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class baekjoon_1028 {
    public static final char ONE = '1';
    public static final int LIMIT = 751;
    int[][] leftCount;
    int[][] rightCount;
    List<String> diamonds;
    int r, c;


    public baekjoon_1028(int[][] leftCount, int[][] rightCount, List<String> diamonds, int r, int c) {
        this.leftCount = leftCount;
        this.rightCount = rightCount;
        this.diamonds = diamonds;
        this.r = r;
        this.c = c;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] split = reader.readLine().split(" ");
        int r = Integer.parseInt(split[0]);
        int c = Integer.parseInt(split[1]);

        int[][] leftCount = new int[r][c];
        int[][] rightCount = new int[r][c];
        List<String> diamonds = new ArrayList<>();

        baekjoon_1028 main = new baekjoon_1028(leftCount, rightCount, diamonds, r, c);

        for (int i = 0; i < r; i++) {
            diamonds.add(reader.readLine());
        }
        reader.close();

        // 대각선 탐색
        int x, y;

        //left side
        x = 0;
        for (y = 0; y <= r - 2; y++) {
            main.makeLeftCountArray(x, y);
        }
        y = r - 1;
        for (x = 0; x < c; x++) {
            main.makeLeftCountArray(x, y);
        }

        //right side
        x = c - 1;
        for (y = 0; y <= r - 2; y++) {
            main.makeRightCountArray(x, y);
        }

        y = r - 1;
        for (x = 0; x < c; x++) {
            main.makeRightCountArray(x, y);
        }

        int height;
        for (int size = (LIMIT + 1) / 2; size >= 1; size--) {
            height = size * 2 - 1;
            for (x = size - 1; x <= c - size; x++) {
                for (y = 0; y <= r - height; y++) {
                    if (
                        // top point
                            leftCount[y][x] >= size &&
                                    rightCount[y][x] >= size &&
                                    // left point
                                    rightCount[y + (size - 1)][x - (size - 1)] >= size &&
                                    // right point
                                    leftCount[y + (size - 1)][x + (size - 1)] >= size
                    ) {
                        System.out.println(size);
                        return;
                    }
                }
            }
        }
        System.out.println(0);
    }

    void makeLeftCountArray(int curX, int curY) {
        int diamondCount = 0;
        while (isPosInMap(curX, curY)) {
            if (hasDiamond(curX, curY)) {
                diamondCount++;
                leftCount[curY][curX] = diamondCount;
            } else {
                leftCount[curY][curX] = 0;
                diamondCount = 0;
            }
            curY--;
            curX++;
        }
    }

    void makeRightCountArray(int curX, int curY) {
        int diamondCount = 0;
        while (isPosInMap(curX, curY)) {
            if (hasDiamond(curX, curY)) {
                diamondCount++;
                rightCount[curY][curX] = diamondCount;
            } else {
                rightCount[curY][curX] = 0;
                diamondCount = 0;
            }
            curY--;
            curX--;
        }
    }

    private boolean hasDiamond(int posX, int posY) {
        return diamonds.get(posY).charAt(posX) == ONE;
    }

    private boolean isPosInMap(int posX, int posY) {
        return (posX >= 0 && posX < c) && (posY >= 0 && posY <= r);
    }
}
