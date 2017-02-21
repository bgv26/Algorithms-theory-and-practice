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

class HuffmanTree {
    private HashMap<Character, String> codeMap = new HashMap<>();

    HuffmanTree(String encodedString) {
        HashMap<Character, Integer> charMap = new HashMap<>();
        for (char c : encodedString.toCharArray()) {
            int value = charMap.getOrDefault(c, 0);
            charMap.put(c, value + 1);
        }

        PriorityQueue<CharFrequency> frequencies = new PriorityQueue<>();
        for (char c : charMap.keySet()) {
            frequencies.add(new CharFrequency(c, charMap.get(c)));
        }

        ArrayList<CharFrequency> nodes = this.buildTree(frequencies);
        this.buildCodeMap(nodes.get(nodes.size() - 1), "");
    }

    private ArrayList<CharFrequency> buildTree(PriorityQueue<CharFrequency> frequencies) {
        ArrayList<CharFrequency> nodes = new ArrayList<>();
        CharFrequency parent = null;
        while (!frequencies.isEmpty()) {
            CharFrequency left = frequencies.poll();
            CharFrequency right = frequencies.poll();
            if (left != null && right != null) {
                int newFrequency = left.getFrequency() + right.getFrequency();
                parent = new CharFrequency(newFrequency);
                parent.setLeft(left);
                parent.setRight(right);
                frequencies.add(parent);
                nodes.add(left);
                nodes.add(right);
            } else if (left != null) {
                parent = left;
            }
        }
        nodes.add(parent);
        return nodes;
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
            codeMap.put(c, !path.equals("") ? path : "0");
        }
    }


    HashMap<Character, String> getCodeMap() {
        return codeMap;
    }
}

public class EncodeHuffman {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        HuffmanTree tree = new HuffmanTree(s);
        HashMap<Character, String> codeMap = tree.getCodeMap();
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
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
