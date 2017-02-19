import java.util.*;

import static java.lang.String.format;

class CharFrequency implements Comparable<CharFrequency> {
    private Character symbol;
    private int frequency;
    private CharFrequency left;
    private CharFrequency right;


    CharFrequency(int frequency) {
        this.frequency = frequency;
    }

    CharFrequency(char symbol, int frequency) {
        this.symbol = symbol;
        this.frequency = frequency;

    }

    Character getSymbol() {
        return symbol;
    }

    int getFrequency() {
        return frequency;
    }

    CharFrequency getLeft() {
        return left;
    }

    CharFrequency getRight() {
        return right;
    }

    void setLeft(CharFrequency left) {
        this.left = left;
    }

    void setRight(CharFrequency right) {
        this.right = right;
    }

    @Override
    public int compareTo(CharFrequency o) {
        if (frequency == o.frequency) {
            if (symbol == null) {
                return 1;
            } else if (o.symbol == null) {
                return -1;
            } else {
                return symbol.compareTo(o.symbol);
            }
        }
        if (frequency > o.frequency) {
            return 1;
        }
        return -1;
    }
}

class CharFrequenciesList {
    private PriorityQueue<CharFrequency> queue;
    private static CharFrequenciesList instance;

    private CharFrequenciesList(String charSequence) {
        queue = new PriorityQueue<>();
        HashMap<Character, Integer> charMap = new HashMap<>();
        for (char c : charSequence.toCharArray()) {
            int value = charMap.getOrDefault(c, 0);
            charMap.put(c, ++value);
        }

        for (char c : charMap.keySet()) {
            queue.add(new CharFrequency(c, charMap.get(c)));
        }
    }

    static CharFrequenciesList getInstance(String charSequence) {
        if (instance == null) {
            instance = new CharFrequenciesList(charSequence);
        }
        return instance;
    }

    CharFrequency extractMin() {
        return queue.poll();
    }

    void insert(CharFrequency cf) {
        queue.add(cf);
    }

    boolean isEmptyQueue() {
        return queue.isEmpty();
    }
}

class HuffmanTree {
    private CharFrequenciesList frequenciesTree;
    private ArrayList<CharFrequency> nodes = new ArrayList<>();
    private HashMap<Character, String> codeMap = new HashMap<>();

    HuffmanTree(String encodedString) {
        this.frequenciesTree = CharFrequenciesList.getInstance(encodedString);
        this.buildTree();
    }

    private void buildTree() {
        CharFrequency parent = null;
        while (!frequenciesTree.isEmptyQueue()) {
            CharFrequency left = frequenciesTree.extractMin();
            CharFrequency right = frequenciesTree.extractMin();
            if (left != null && right != null) {
                int newFrequency = left.getFrequency() + right.getFrequency();
                parent = new CharFrequency(newFrequency);
                parent.setLeft(left);
                parent.setRight(right);
                frequenciesTree.insert(parent);
                nodes.add(left);
                nodes.add(right);
            } else if (left != null) {
                parent = left;
            }
        }
        nodes.add(parent);
        this.buildCodeMap(nodes.get(nodes.size() - 1), "");
    }

    private void buildCodeMap(CharFrequency node, String path) {
        CharFrequency left = node.getLeft();
        CharFrequency right = node.getRight();
        if (left != null) {
            buildCodeMap(left, path + "0");
        }
        if (right != null) {
            buildCodeMap(right, path + "1");
        }
        Character c = node.getSymbol();
        if (c != null) {
            codeMap.put(c, ! path.equals("") ? path: "0");
        }
    }


    HashMap<Character, String> getCodeMap() {
        return codeMap;
    }
}

public class Huffman {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        HuffmanTree tree = new HuffmanTree(s);
        HashMap<Character, String> codeMap = tree.getCodeMap();
        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            sb.append(codeMap.get(c));
        }
        String encodedString = sb.toString();
        System.out.println(format("%d %d", codeMap.size(), encodedString.length()));
        for (Map.Entry<Character, String> entry : codeMap.entrySet()) {
            System.out.println(format("%s: %s", entry.getKey(), entry.getValue()));
        }
        System.out.println(encodedString);
    }
}
