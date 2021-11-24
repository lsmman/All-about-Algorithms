//public class SolutionZoom {
//}
//
//
////줌 인터넷 코테
//
///**
// * 조각 맞추기 게임 구현
// */
//class Solution {
//    private int[][] grid;
//    private int rowMaxSize;
//    private int colMaxSize;
//    private int rowLength;
//    private int colLength;
//    private int[][] rowCorrespondCountArrays;
//    private int[][] colCorrespondCountArrays;
//
//    private static final int NOVALUE = 0;
//
//    public int[] solution(int[][] grid) {
//        this.grid = grid;
//        this.rowLength = grid.length;
//        this.colLength = grid[0].length;
//        this.rowMaxSize = Math.min((colLength + 1) / 2, rowLength);
//        this.colMaxSize = Math.min((rowLength + 1) / 2, colLength);
//        int maxSize = Math.max(rowMaxSize, colMaxSize);
//        int[] answer = {1, rowLength * colLength};
//        int count;
//
//        makeCorrespondCountArrays();
//
//        for (int curSize = maxSize; curSize > 1; curSize--) {
//            count = checkDiamondForm(curSize);
//            if (count > 0){
//                answer[0] = curSize;
//                answer[1] = count;
//                break;
//            }
//        }
//
//        return answer;
//    }
//
//    private void makeCorrespondCountArrays() {
//        makeRowCorrespondCountArrays();
//        makeColCorrespondCountArrays();
//    }
//
//    private void makeRowCorrespondCountArrays() {
//        rowCorrespondCountArrays = new int[rowLength][colLength];
//
//        for (int row = 0; row < rowLength; row++){
//            makeRowCorrespondCountArray(row);
//        }
//    }
//
//    private void makeRowCorrespondCountArray(int row) {
//        int[] target = grid[row];
//        int[] result = rowCorrespondCountArrays[row];
//        int last = NOVALUE;
//        int cnt = 0;
//
//        for (int col = colLength-1; col >= 0; col--) {
//            if (target[col] == last){
//                cnt++;
//                result[col] = cnt;
//                continue;
//            }
//            last = target[col];
//            cnt = 1;
//            result[col] = cnt;
//        }
//    }
//
//    private void makeColCorrespondCountArrays() {
//        colCorrespondCountArrays = new int[rowLength][colLength];
//
//        for (int col = 0; col < rowLength; col++){
//            makeColCorrespondCountArray(col);
//        }
//    }
//
//    private void makeColCorrespondCountArray(int col) {
//        int last = NOVALUE;
//        int cnt = 0;
//
//        for (int row = rowLength-1; row >= 0; row--) {
//            if (grid[row][col] == last){
//                cnt++;
//                colCorrespondCountArrays[row][col] = cnt;
//                continue;
//            }
//            last = grid[row][col];
//            cnt = 1;
//            colCorrespondCountArrays[row][col] = cnt;
//        }
//    }
//
//
//    private int checkDiamondForm(int size) {
//        int cnt = 0;
//        if (size <= rowMaxSize){
//            cnt += checkDiamondFormInRow(size);
//        }
//
//        if (size <= colMaxSize){
//            cnt += checkDiamondFormInCol(size);
//        }
//        return cnt;
//    }
//
//    private int checkDiamondFormInRow(int size){
//        int minSpace = Solution.getNeedSpaceBySize(size);
//        int count = 0;
//
//        // Case
//        //   ---
//        //    ---
//        //     ---
//        for (int srtRow = 0; srtRow <= rowLength-size; srtRow++) {
//            for (int srtCol = 0; srtCol <= colLength-minSpace; srtCol++) {
//                if (isDiamondForm(size, srtRow, srtCol, rowCorrespondCountArrays, 1)){
//                    count++;
//                }
//            }
//        }
//
//        // Case
//        //       ---
//        //      ---
//        //     ---
//        for (int srtRow = 0; srtRow <= rowLength-size; srtRow++) {
//            for (int srtCol = size-1; srtCol <= colLength-size; srtCol++) {
//                if (isDiamondForm(size, srtRow, srtCol, rowCorrespondCountArrays, -1)){
//                    count++;
//                }
//            }
//        }
//        return count;
//    }
//
//    private int checkDiamondFormInCol(int size){
//        int minSpace = Solution.getNeedSpaceBySize(size);
//        int count = 0;
//
//        // Case
//        //   |
//        //   ||
//        //    |
//        for (int srtRow = 0; srtRow <= rowLength-minSpace; srtRow++) {
//            for (int srtCol = 0; srtCol <= colLength-size; srtCol++) {
//                if (isDiamondForm(size, srtRow, srtCol, colCorrespondCountArrays, 1)){
//                    count++;
//                }
//            }
//        }
//
//        // Case
//        //    |
//        //   ||
//        //   |
//        for (int srtRow = 0; srtRow <= rowLength-minSpace; srtRow++) {
//            for (int srtCol = size-1; srtCol < colLength; srtCol++) {
//                if (isDiamondForm(size, srtRow, srtCol, colCorrespondCountArrays, -1)){
//                    count++;
//                }
//            }
//        }
//        return count;
//    }
//
//    private boolean isDiamondForm(int size, int srtRow, int srtCol, int[][] correspondCountArrays, int sign) {
//        int row;
//        int col;
//        for (int term = 0; term < size; term++){
//            row = srtRow + term;
//            col = srtCol + (term * sign);
//            if (correspondCountArrays[row][col] < size){
//                return false;
//            }
//        }
//        return true;
//    }
//
//    private static int getNeedSpaceBySize(int diamondSize){
//        return (diamondSize * 2) - 1;
//    }
//
//    public static void main(String[] args) {
//        {
//            int[] answer = {3, 2};
//            int[][] data = {{2, 1, 1, 3, 5, 1}, {1, 1, 3, 3, 5, 5}, {8, 3, 3, 3, 1, 5}, {3, 3, 3, 4, 4, 4}, {3, 3, 4, 4, 4, 4}, {1, 4, 4, 4, 4, 4}};
//            int[] result = new Solution().solution(data);
//            System.out.println(answer[0] + " " + result[0]);
//            System.out.println(answer[1] + " " + result[1]);
//        }
//        {
//            int[] answer = {1,9};
//            int[][] data = {{10,20,30},{40,50,60},{70,80,90}};
//            int[] result = new Solution().solution(data);
//            System.out.println(answer[0] + " " + result[0]);
//            System.out.println(answer[1] + " " + result[1]);
//        }
//        {
//            int[] answer =	{2,4};
//            int[][] data = {{1,1,1,1},{1,1,1,1}};
//            int[] result = new Solution().solution(data);
//            System.out.println(answer[0] + " " + result[0]);
//            System.out.println(answer[1] + " " + result[1]);
//        }
//    }
//}
//
//
///*
// 프린트 작업 큐 구현
// */
//import java.util.ArrayList;
//        import java.util.PriorityQueue;
//
//
//class printData implements Comparable {
//    public int ID;
//    public int requiredTime;
//    public int pageNum;
//
//    public printData(int[] inputData){
//        this.ID = inputData[0];
//        this.requiredTime = inputData[1];
//        this.pageNum = inputData[2];
//    }
//
//    @Override
//    public int compareTo(Object o) {
//        if (o == null){
//            throw new NullPointerException();
//        }
//        if (getClass() != o.getClass()){
//            throw new ClassCastException();
//        }
//        printData printData = (printData) o;
//        if (this.pageNum < printData.pageNum){
//            return -1;
//        }
//        if (this.pageNum > printData.pageNum){
//            return 1;
//        }
//        return this.requiredTime - printData.requiredTime;
//    }
//}
//
//class Solution {
//    public int[] solution(int[][] data) {
//        int[] answer = new int[data.length];
//        ArrayList<Integer> finishedOrder = new ArrayList<>();
//        PriorityQueue<printData> readyQ = new PriorityQueue<>();
//        ArrayList<printData> waitingQ = new ArrayList<>();
//        int curTime = 0;
//        int lengthOfWaitingQ = 0;
//        int indexOfWaitingQ = 0;
//
//        for (int[] datum : data) {
//            waitingQ.add(new printData(datum));
//        }
//        lengthOfWaitingQ = waitingQ.size();
//
//        while (!readyQ.isEmpty() || indexOfWaitingQ < lengthOfWaitingQ){
//            if (readyQ.isEmpty()){
//                curTime = Math.max(waitingQ.get(indexOfWaitingQ).requiredTime, curTime);
//            }
//            while (indexOfWaitingQ < lengthOfWaitingQ && curTime >= waitingQ.get(indexOfWaitingQ).requiredTime){
//                readyQ.add(waitingQ.get(indexOfWaitingQ));
//                indexOfWaitingQ++;
//            }
//
//            printData cur = readyQ.poll();
//            finishedOrder.add(cur.ID);
//            curTime += cur.pageNum;
//        }
//
//        for (int i = 0; i < answer.length; i++) {
//            answer[i] = finishedOrder.get(i);
//        }
//        System.out.println(finishedOrder);
//        return answer;
//    }
//
//    public static void main(String[] args) {
//        {
//            int[][] data = {{1, 0, 5}, {2, 2, 2}, {3, 3, 1}, {4, 4, 1}, {5, 10, 2}};
//            int[] answer = {1, 3, 4, 2, 5};
//
//            System.out.println(new Solution().solution(data).equals(answer));
//        }
//
//
//        {
//            int[][] data = {{1, 0, 3}, {2, 1, 3}, {3, 3, 2}, {4, 9, 1}, {5, 10, 2}};
//            int[] answer = {1,3,2,4,5};
//
//            System.out.println(new Solution().solution(data).equals(answer));
//        }
//
//        {
//            int[][] data = {{1, 2, 10}, {2, 5, 8}, {3, 6, 9}, {4, 20, 6}, {5, 25, 5}};
//            int[] answer = {1,2,4,5,3};
//
//            System.out.println(new Solution().solution(data).equals(answer));
//        }
//
//
//
//    }
//}
//
///*
//{{1, 0, 5},{2, 2, 2},{3, 3, 1},{4, 4, 1},{5, 10, 2}}	{1,3,4,2,5}
//{{1, 0, 3}, {2, 1, 3}, {3, 3, 2}, {4, 9, 1}, {5, 10, 2}}	{1,3,2,4,5}
//{{1, 2, 10}, {2, 5, 8}, {3, 6, 9}, {4, 20, 6}, {5, 25, 5}}	{1,2,4,5,3}
// */