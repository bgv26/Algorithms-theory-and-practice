import java.util.ArrayList;
import java.util.Scanner;

public class CustomPriorityQueue {
    private final static String INSERT = "Insert";
    private final static String EXTRACT = "ExtractMax";
    private static ArrayList<Integer> heap = new ArrayList<>();
    private static int size = 0;

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
        if (size > 0) {
            siftUp(size, value);
        }
        size++;
    }

    private static String extract() {
        if (size == 0) {
            System.out.println("Queue is empty");
            return null;
        }

        String result = String.valueOf(heap.get(0));
        int value = heap.get(size - 1);
        heap.remove(size - 1);
        size--;
        if (size != 0) {
            siftDown(value);
        }
        return result;
    }

    private static void siftDown(int value) {
        int index = 0;
        while (index < size / 2) {
            int leftIndex = index * 2 + 1;
            int left = heap.get(leftIndex);
            int rightIndex = index * 2 + 2;
            int child = left;
            if (rightIndex <= size - 1 && (heap.get(rightIndex) > child)) {
                child = heap.get(rightIndex);
            }
            if (value >= child) {
                break;
            }
            heap.set(index, child);
            index = (child == left) ? leftIndex : rightIndex;
        }
        heap.set(index, value);
    }

    private static void siftUp(int index, int value) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            int parent = heap.get(parentIndex);
            if (value <= parent) {
                break;
            }
            heap.set(index, parent);
            index = parentIndex;

        }
        heap.set(index, value);
    }
}

