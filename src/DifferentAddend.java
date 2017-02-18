import java.util.Scanner;

public class DifferentAddend {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int count = 1;
        StringBuilder addends = new StringBuilder();
        while (2 * count < number) {
            addends.append(String.format("%d ", count));
            number -= count;
            count++;
        }
        addends.append(number);
        System.out.println(count);
        System.out.println(addends.toString());
    }
}
