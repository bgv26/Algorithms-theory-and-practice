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
            String operation = scanner.next();
            if (operation.contains(INSERT)) {
                int value = scanner.nextInt();
                insert(value);
            }
            if (operation.contains(EXTRACT)) {
                System.out.println(extract());
            }
        }
    }

    private static void insert(int value) {
        heap.add(value);
        int lastIndex = heap.size() - 1;
        siftUp(lastIndex);
    }

    private static String extract() {
        String result = String.valueOf(heap.get(0));
        int lastIndex = heap.size() - 1;
        heap.set(0, heap.get(lastIndex));
        heap.remove(lastIndex);
        siftDown(0);
        return result;
    }

    private static void siftDown(int index) {
        int lastIndex = heap.size() - 1;
        int leftIndex = index * 2 <= lastIndex ? index * 2 : lastIndex;
        int rightIndex = index * 2 + 1 <= lastIndex ? index * 2 + 1 : lastIndex;

        int current = heap.get(index);
        int left = heap.get(leftIndex);
        int right = heap.get(rightIndex);

        int next = Math.min(left, right);
        int nextIndex = next == left ? leftIndex : rightIndex;

        if (current < next) {
            heap.set(index, next);
            heap.set(nextIndex, current);
            siftDown(nextIndex);
        }
    }

    private static void siftUp(int index) {
        int current = heap.get(index);
        int parent = heap.get(index / 2);
        if (current > parent && index > 0) {
            if (current > parent) {
                heap.set(index, parent);
                heap.set(index / 2, current);
                index /= 2;
            }
            siftUp(index);
        }
    }
}
