import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(getNumber(n));
    }

    private static int getNumber(final int number) {
        int result = 0;
        if (number >= 1) {
            result++;
        }

        int previous = result;
        for (int i = 2; i < number; i++) {
            int swap = result;
            result += previous;
            previous = swap;
        }

        return result;
    }

}
