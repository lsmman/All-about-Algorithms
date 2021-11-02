/**
 * Permutations
 *
 * nPr = n! / (n-r)!
 */
class Permutations{
    public long permuations(int n, int r){
        if (n < 0 || r < 0){
            return 0L;
        }
        long result = 1;
        for(int i = 0; i < r; i++){
            result *= (n - i);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Permutations().permuations(4, 2)); // 12
        System.out.println(new Permutations().permuations(5, 3)); // 60
        System.out.println(new Permutations().permuations(1, 0)); // 1
        System.out.println(new Permutations().permuations(1, 1)); // 1
    }
}