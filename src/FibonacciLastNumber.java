import java.util.Scanner;

public class FibonacciLastNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(getLastNumber(n));
    }

    private static int getLastNumber(final int number) {
        int result = 0;
        if (number >= 1) {
            result++;
        }

        int previous = result;
        for (int i = 2; i < number; i++) {
            int swap = result % 10;
            result = (result + previous) % 10;
            previous = swap;
        }

        return result;
    }
}
