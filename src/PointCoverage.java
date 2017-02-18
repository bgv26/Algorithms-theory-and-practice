import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Segment implements Comparable<Segment> {
    private int left;
    private int right;

    int getRight() {
        return right;
    }

    void setLeft(int left) {
        this.left = left;
    }

    void setRight(int right) {
        this.right = right;
    }

    boolean contains(int num) {
        return num >= left && num <= right;
    }


    @Override
    public int compareTo(Segment s) {
        if (this.right == s.right) {
            return 0;
        }
        if (this.right > s.right) {
            return 1;
        }
        return -1;
    }
}

public class PointCoverage {
    public static void main(String[] args) {
        getPoints(getInput());
    }

    private static Segment[] getInput() {
        Scanner scanner = new Scanner(System.in);
        int numberOfSegments = scanner.nextInt();
        Segment[] segments = new Segment[numberOfSegments];
        for (int i = 0; i < numberOfSegments; i++) {
            segments[i] = new Segment();
            segments[i].setLeft(scanner.nextInt());
            segments[i].setRight(scanner.nextInt());
        }
        return segments;
    }

    private static void getPoints(Segment[] segments) {
        Arrays.sort(segments);
        ArrayList<Segment> segmentsList = new ArrayList<>(Arrays.asList(segments));
        ArrayList<String> result = new ArrayList<>();
        int count = 0;
        while (segmentsList.size() > 0) {
            int point = segmentsList.get(0).getRight();
            result.add(String.valueOf(point));
            count++;
//            segmentsList.remove(0);
            while (segmentsList.size() > 0 && segmentsList.get(0).contains(point)) {
                segmentsList.remove(0);
            }
        }
        System.out.println(count);
        System.out.println(String.join(" ", result));
    }
}
