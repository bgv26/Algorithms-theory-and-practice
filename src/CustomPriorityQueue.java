import java.util.ArrayList;
import java.util.Scanner;

public class CustomPriorityQueue {
    private final static String INSERT = "Insert";
    private final static String EXTRACT = "ExtractMax";
    private static ArrayList<Integer> heap = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfOperation = scanner.nextInt();
        for (int i = 0; i < numberOfOperation; i++) {
            String operation = scanner.nextLine();
            if (operation.contains(INSERT)) {
                int value = Integer.valueOf(operation.split(" ")[1]);
                insert(value);
            }
            if (operation.contains(EXTRACT)) {
                System.out.println(extract());
            }
        }
    }

    private static void insert(int value) {
        siftUp(value);
    }

    private static String extract() {
        String result = "";
        return result;
    }

    private static void siftDown(int value) {
    }

    private static void siftUp(int value) {
        heap.add(value);
        int valueIndex = heap.size() - 1;
        int parent = heap.get(valueIndex / 2);
        while (value > parent) {
            heap.add(valueIndex, parent);
            heap.add(valueIndex / 2, value);
            valueIndex /= 2;
        }
    }
}
