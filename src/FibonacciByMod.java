import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FibonacciByMod {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        int m = scanner.nextInt();
        System.out.println(getModFibonacci(n, m));
    }

    private static int getModFibonacci(final long number, final int mod) {
        List<Integer> FibNumbers = new ArrayList<>(Arrays.asList(0, 1));
        int periodLength = 0;
        for (int i = 2; i < 6 * mod; i++) {
            FibNumbers.add((FibNumbers.get(i - 1) + FibNumbers.get(i - 2)) % mod);
            // Detect beginning of Pisano period
            if (FibNumbers.get(i - 1) == 0 && FibNumbers.get(i) == 1) {
                periodLength = i - 1;
                break;
            }
        }
        return FibNumbers.get((int) (number % periodLength));
    }

}
