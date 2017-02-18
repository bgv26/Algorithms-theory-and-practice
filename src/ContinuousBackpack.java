import java.util.Arrays;
import java.util.Scanner;

class Item implements Comparable<Item> {
    private double cost;
    private double size;
    private double price;

    Item(double cost, double size) {
        this.cost = cost;
        this.size = size;
        price = cost / size;
    }

    double getCost() {
        return cost;
    }

    double getPrice() {
        return price;
    }

    double getSize() {
        return size;
    }

    @Override
    public int compareTo(Item s) {
        if (this.price == s.price) {
            if (this.size == s.size) {
                return 0;
            }
            if (this.size > s.size) {
                return 1;
            }
            return -1;
        }
        if (this.price < s.price) {
            return 1;
        }
        return -1;
    }
}

public class ContinuousBackpack {
    private int capacity;
    private Item[] items;

    public static void main(String[] args) {
        ContinuousBackpack backpack = new ContinuousBackpack();
        backpack.getInput();
        System.out.printf("%.3f", backpack.getMaxCost());
    }

    private void getInput() {
        Scanner scanner = new Scanner(System.in);
        int numberOfItems = scanner.nextInt();
        capacity = scanner.nextInt();
        items = new Item[numberOfItems];
        for (int i = 0; i < numberOfItems; i++) {
            items[i] = new Item(scanner.nextInt(), scanner.nextInt());
        }
    }

    private double getMaxCost() {
        double maxCost = 0;
        Arrays.sort(items);
        for (Item item : items) {
            if (item.getSize() <= capacity) {
                maxCost += item.getCost();
                capacity -= item.getSize();
            } else {
                maxCost += capacity * item.getPrice();
                break;
            }
        }

        return maxCost;
    }
}
