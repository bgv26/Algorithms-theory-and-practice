import java.util.HashMap;
import java.util.Scanner;

public class DecodeHuffman {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfLetters = scanner.nextInt();
        int lengthOfEncodedString = scanner.nextInt();
        HashMap<String, Character> codeMap = new HashMap<>();
        for (int i = 0; i < numberOfLetters; i++) {
            char value = scanner.next().charAt(0);
            String key = scanner.next();
            codeMap.put(key, value);
        }
        String encodedString = scanner.next();
        StringBuilder sb = new StringBuilder();
        while (lengthOfEncodedString > 0) {
            for (String code : codeMap.keySet()) {
                if (encodedString.startsWith(code)) {
                    sb.append(codeMap.get(code));
                    encodedString = encodedString.substring(code.length());
                    lengthOfEncodedString -= code.length();
                }
            }
        }
        System.out.println(sb.toString());
    }
}
