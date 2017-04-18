import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BinarySearch {
    private static long[] arrayOfLong;

    public static void main(String[] args) throws FileNotFoundException {
        run();
    }

    private static void run() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("C:\\Devel\\Algorithms-theory-and-practice\\src\\input.txt"));
        int n = scanner.nextInt();
        arrayOfLong = new long[n];
        for (int i = 0; i < n; i++) {
            arrayOfLong[i] = scanner.nextLong();
        }
        int k = scanner.nextInt();
        for (int i = 0; i < k; i++) {
            int index = binarySearch(scanner.nextLong());
            System.out.print(String.valueOf(index) + " ");
        }
    }

    private static int binarySearch(long seek) {
        int left = 0;
        int right = arrayOfLong.length - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (arrayOfLong[middle] == seek) {
                return middle + 1;
            } else if (arrayOfLong[middle] > seek) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return -1;
    }
}
