import java.util.*;

class StackItem {
    private Character value;
    private Integer index;

    StackItem(Character value, Integer index) {
        this.value = value;
        this.index = index;
    }

    Character getValue() {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(index);
    }
}

public class CheckBraces {
    private static final Map<Character, Character> braces;

    static {
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        braces = Collections.unmodifiableMap(map);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        System.out.println(checkBraces(input));
    }

    private static String checkBraces(String input) {
        Stack<StackItem> stack = new Stack<>();
        for (int i = 0; i < input.length(); i++) {
            Character c = input.charAt(i);
            if (braces.containsValue(c)) {
                stack.push(new StackItem(c, i + 1));
            }
            if (braces.containsKey(c) && (stack.isEmpty() || !braces.get(c).equals(stack.pop().getValue()))) {
                return String.valueOf(i + 1);
            }
        }
        return stack.isEmpty() ? "Success" : stack.pop().toString();
    }
}
