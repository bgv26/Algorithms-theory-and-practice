import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class TurnpikeProblem {
    public static void main(String[] args) {
        // DEFINE "L"!!!
        int[] L = getIntArrayFromFile("D:\\Devel\\Algorithms-theory-and-practice\\src\\test.txt");
        int[] rightOut = getIntArrayFromFile("D:\\Devel\\Algorithms-theory-and-practice\\src\\out.txt");
        int[] out = turnpike(L);
        assert Arrays.equals(out, rightOut) : "Беда";
        for (int anOut : out != null ? out : new int[0]) {
            System.out.print(anOut + " ");
        }
    }

    private static int[] getIntArrayFromFile(String fileName) {
        ArrayList<Integer> intTokens = new ArrayList<>();
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)));
            String str;
            while ((str = bufferedReader.readLine()) != null) {
                String[] tokens = str.split(" ");
                for (String token : tokens) {
                    intTokens.add(Integer.valueOf(token));
                }
            }
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
        int[] L = new int[intTokens.size()];
        for (int i = 0; i < intTokens.size(); i++) {
            L[i] = intTokens.get(i);
        }
        return L;
    }

    private static int[] turnpike(int[] Lin) {
        PriorityQueue<Integer> L = new PriorityQueue<>(Lin.length, Collections.reverseOrder());
        for (int e : Lin) {
            if (e > 0) {
                L.add(e);
            }
        }
        PriorityQueue<Integer> points = new PriorityQueue<>(L.size(), Collections.reverseOrder());
        points.add(0);
        points.add(L.poll());
        if (solveRecursive(L, points)) {
            int[] out = new int[points.size()];
            for (int i = out.length - 1; i >= 0; --i) {
                out[i] = points.poll();
            }
            return out;
        } else {
            return null;
        }
    }

    private static boolean solveRecursive(PriorityQueue<Integer> dist, PriorityQueue<Integer> points) {
        if (dist.isEmpty()) {
            return true;
        }
        int maxDist = dist.peek();
        int maxPoint = points.peek();
        return solveRecursive(dist, points, maxDist) || solveRecursive(dist, points, maxPoint - maxDist);
    }

    private static boolean solveRecursive(PriorityQueue<Integer> dist, PriorityQueue<Integer> points, int pointToAdd) {
        Iterator pit = points.iterator();
        LinkedList<Integer> distsToRemove = new LinkedList<>();
        while (pit.hasNext()) {
            int d = Math.abs((Integer) pit.next() - pointToAdd);
            if (dist.contains(d)) {
                distsToRemove.add(d);
            } else {
                return false;
            }
        }
        for (Integer e : distsToRemove) {
            dist.remove(e);
        }
        points.add(pointToAdd);
        if (solveRecursive(dist, points)) {
            return true;
        } else {
            points.remove(pointToAdd);
            dist.addAll(distsToRemove);
            return false;
        }
    }
}