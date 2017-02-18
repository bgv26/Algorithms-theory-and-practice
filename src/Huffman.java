import java.util.*;

class CharFrequency implements Comparable<CharFrequency> {
    private Character symbol;
    private int frequency;


    public CharFrequency(int frequency) {
        this.frequency = frequency;
    }

    public CharFrequency(char symbol, int frequency) {
        this.symbol = symbol;
        this.frequency = frequency;
    }

    public Character getSymbol() {
        return symbol;
    }

    public int getFrequency() {
        return frequency;
    }

    @Override
    public int compareTo(CharFrequency o) {
        if (frequency == o.frequency) {
            return 0;
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

    public static CharFrequenciesList getInstance(String charSequence) {
        if (instance == null) {
            instance = new CharFrequenciesList(charSequence);
        }
        return instance;
    }

    public CharFrequency extractMin() {
        return queue.poll();
    }

    public void insert(CharFrequency cf) {
        queue.add(cf);
    }

    public boolean isEmptyQueue() {
        return queue.isEmpty();
    }
}

class HuffmanTreeNode {
    private HuffmanTreeNode left = null;
    private HuffmanTreeNode right = null;
    private HuffmanTreeNode parent = null;
    private CharFrequency data = null;

    public HuffmanTreeNode(CharFrequency data) {
        this.data = data;
    }

    public HuffmanTreeNode(CharFrequency data, HuffmanTreeNode parent) {
        this.data = data;
        this.parent = parent;
    }

    public HuffmanTreeNode getLeft() {
        return left;
    }

    public HuffmanTreeNode getRight() {
        return right;
    }

    public HuffmanTreeNode getParent() {
        return parent;
    }

    public CharFrequency getData() {
        return data;
    }

    public void setLeft(HuffmanTreeNode left) {
        this.left = left;
    }

    public void setRight(HuffmanTreeNode right) {
        this.right = right;
    }

    public void setParent(HuffmanTreeNode parent) {
        this.parent = parent;
    }

    public void setData(CharFrequency data) {
        this.data = data;
    }
}

class HuffmanTree {
    private CharFrequenciesList frequenciesTree;
    private ArrayList<HuffmanTreeNode> nodes = new ArrayList<>();
    private HashMap<Character, String> codeMap;

    public HuffmanTree(String encodedString) {
        this.frequenciesTree = CharFrequenciesList.getInstance(encodedString);
        this.buildTree();
    }

    private void buildTree() {
        HuffmanTreeNode parent = null;
        while (!frequenciesTree.isEmptyQueue()) {
            HuffmanTreeNode left = new HuffmanTreeNode(frequenciesTree.extractMin());
            HuffmanTreeNode right = new HuffmanTreeNode(frequenciesTree.extractMin());
            if (left.getData() != null && right.getData() != null) {
                int newFrequency = left.getData().getFrequency() + right.getData().getFrequency();
                CharFrequency newElement = new CharFrequency(newFrequency);
                frequenciesTree.insert(newElement);
                parent = new HuffmanTreeNode(newElement);
                parent.setLeft(left);
                parent.setRight(right);
                left.setParent(parent);
                right.setParent(parent);
                nodes.add(left);
                nodes.add(right);
            } else if (left.getData() != null) {
                parent = left;
            }
        }
        nodes.add(parent);
        Collections.reverse(nodes);
        this.buildCodeMap();
    }

    private void buildCodeMap() {
        codeMap = new HashMap<>();
        StringBuilder code = new StringBuilder();
        if (nodes.size() == 1) {
            codeMap.put(nodes.get(0).getData().getSymbol(), "0");
            return;
        }
        for (HuffmanTreeNode node : nodes) {
            HuffmanTreeNode parent = node.getParent();
            if (parent != null) {
                if (node == parent.getLeft()) {
                    code.append('0');
                }
                if (node == parent.getRight()) {
                    code.append('1');
                }
            }
            Character c = node.getData().getSymbol();
            if (c != null) {
                codeMap.put(c, code.toString());
                code = new StringBuilder();
            }
        }
    }

    public String getCode(char symbol) {
        return codeMap.get(symbol);
    }
}

public class Huffman {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        HuffmanTree tree = new HuffmanTree(s);
        for (char c : s.toCharArray()) {
            System.out.println(tree.getCode(c));
        }
    }
}
