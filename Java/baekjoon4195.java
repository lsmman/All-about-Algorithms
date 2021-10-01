import java.util.*;

public class baekjoon4195 {

    Map<String, String> parent;
    Map<String, Integer> networkCount;

    public static void solve() {
        Scanner scanner = new Scanner(System.in);
        List<Integer> answers = new ArrayList<>();
        baekjoon4195 network;

        int loop, result;
        List<String> inputs_arr;
        String input_line;
        input_line = scanner.nextLine();
        int cases = Integer.parseInt(input_line);

        for (int i = 0; i < cases; i++) {
            inputs_arr = new ArrayList<>();
            network = new baekjoon4195();
            input_line = scanner.nextLine();
            loop = Integer.parseInt(input_line);

            for (int j = 0; j < loop; j++) {
                input_line = scanner.nextLine();
                inputs_arr.add(input_line);
            }
            for (String input : inputs_arr) {
                result = network.count_friend_network(input);
                answers.add(result);
            }
        }
        scanner.close();

        for (int answer : answers) {
            System.out.println(answer);
        }
    }

    public baekjoon4195() {
        parent = new HashMap<>();
        networkCount = new HashMap<>();
    }

    private String find(String name) {
        String parent_name = parent.get(name);
        if (name.equals(parent_name)) {
            return name;
        }
        String network_name = find(parent_name);
        parent.put(name, network_name);
        return network_name; // 제일 상위 네트워크 이름 리턴
    }

    private void union(String parent_a, String parent_b) {
        if (parent_a.equals(parent_b)){
            return;
        }
        parent.put(parent_b, parent_a);
        int merged_cnt = networkCount.get(parent_b) + networkCount.get(parent_a);
        networkCount.put(parent_a, merged_cnt);
        return;
    }

    public int count_friend_network(String input) {
        String[] s = input.split(" ");
        if (s.length != 2) {
            return 0;
        }
        String name_a = s[0];
        String name_b = s[1];

        if (!parent.containsKey(name_a)) {
            parent.put(name_a, name_a);
            networkCount.put(name_a, 1);
        }
        if (!parent.containsKey(name_b)) {
            parent.put(name_b, name_b);
            networkCount.put(name_b, 1);
        }

        String parent_a = this.find(name_a);
        String parent_b = this.find(name_b);

        union(parent_a, parent_b);

        return networkCount.get(find(name_a));
    }

    public static void main(String[] args) {
        baekjoon4195.solve();
//        baekjoon4195.test();
    }

//}

    public static void test() {
        test1();
        test2();
    }

    private static void test1() {
        ArrayList<String> testcase = new ArrayList<>();
        ArrayList<Integer> answers = new ArrayList<>();

        testcase.add("a b");
        testcase.add("a c");
        testcase.add("d e");
        testcase.add("a d");
        testcase.add("f g");
        testcase.add("g i");
        testcase.add("c i");

        baekjoon4195 solver = new baekjoon4195();
        int result;

        for (String eachCase : testcase) {
            result = solver.count_friend_network(eachCase);
            answers.add(result);
        }

        int[] excepted = new int[]{2, 3, 2, 5, 2, 3, 8};
        for (int i = 0; i < excepted.length; i++) {
            if (!(answers.get(i).equals(excepted[i]))) {
                System.out.println("this is test1 error " + i);
                return;
            }
        }
    }

    private static void test2(){
        ArrayList<String> testcase = new ArrayList<>();
        ArrayList<Integer> answers = new ArrayList<>();

        testcase.add("a b");
        testcase.add("b c");
        testcase.add("d e");
        testcase.add("e f");
        testcase.add("g h");
        testcase.add("h i");
        testcase.add("a f");
        testcase.add("c i");


        baekjoon4195 solver = new baekjoon4195();
        int result;

        for (String eachCase : testcase) {
            result = solver.count_friend_network(eachCase);
            answers.add(result);
        }

        int[] excepted = new int[] {
                2,
                3,
                2,
                3,
                2,
                3,
                6,
                9,
        };
        for (int i = 0; i < excepted.length ; i++) {
            if (!(answers.get(i).equals(excepted[i]))){
                System.out.println("this is test2 error " + i);
                return;
            }
        }
    }
}


