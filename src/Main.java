import java.io.*;
import java.util.ArrayList;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.TreeSet;
public class Main{

    private static AVLTree<GenericData> dataStructure = new AVLTree<>();
    private static SortedMap<Integer, TreeSet<Integer>> searchCount = new TreeMap<>();
    private static SortedMap<Integer, TreeSet<Integer>> insertCount = new TreeMap<>();

    public static void main(String[] args) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("data/insertCount.txt", false));
            writer.write("");
            writer.close();
            writer = new BufferedWriter(new FileWriter("data/searchCount.txt", false));
            writer.write("");
            writer.close();
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }


        int[] range = {10, 100, 1000, 2000, 5000, 10000, 15000, 25000, 43000, 50000};
        
        for (int n : range) {
            experiment(n);
        }

        saveInsertCount(insertCount);
        saveSearchCount(searchCount);
    }

    public static void experiment(int n) {
        loadData("GenericsKB.txt", n);
        try {
            BufferedReader reader = new BufferedReader(new FileReader("GenericsKB-queries.txt"));
            String line;

            while((line = reader.readLine()) != null) {
                GenericData query = new GenericData(line, null, 0);
                BinaryTreeNode<GenericData> searchResult = dataStructure.find(query);

                if (searchCount.containsKey(n)) {
                    searchCount.get(n).add(dataStructure.getSearchCount());
                } else {
                    searchCount.put(n, new TreeSet<>());
                    searchCount.get(n).add(dataStructure.getSearchCount());
                }
                
                if (searchResult == null) {
                    dataStructure.insert(query);
                    if (insertCount.containsKey(n)) {
                        int count = dataStructure.getInsertCount();
                        insertCount.get(n).add(count);
                    } else {
                        insertCount.put(n, new TreeSet<>());
                        int count = dataStructure.getInsertCount();
                        insertCount.get(n).add(count);
                    }
                    dataStructure.delete(query);
                }

            }

            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    
    /**
     * Makes randomised subsets of size N from data supplied by user. The textfile supplied by the user must be seperated by \t.
     * @param fileName
     * @param n
     */
    public static void loadData(String fileName, int n) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            ArrayList<GenericData> list = new ArrayList<>();
            int start;
            int count = 0;

            String line;

            while ((line = reader.readLine()) != null) {
                count++;
                String[] data = line.split("\t");
                list.add(new GenericData(data[0], data[1], Double.parseDouble(data[2])));
            }

            start = (int)(Math.random() * (count-n));

            if (start < 0) {
                reader.close();
                throw new IllegalArgumentException("N is too large for the data set");
            }

            for (int i = start; i < start + n; i++) {
                dataStructure.insert(list.get(i));
            }

            dataStructure.clearCount();

            reader.close();
        }
        catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public static void saveInsertCount(SortedMap<Integer, TreeSet<Integer>> insertCount) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("data/insertCount.txt", true));
            for (int i : insertCount.keySet()) {
                for (int j : insertCount.get(i)) {
                    writer.write(i + "\t" + j);
                    writer.newLine();
                }
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }

    public static void saveSearchCount(SortedMap<Integer, TreeSet<Integer>> searchCount) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("data/searchCount.txt", true));
            for (int i : searchCount.keySet()) {
                for (int j : searchCount.get(i)) {
                    writer.write(i + "\t" + j);
                    writer.newLine();
                }
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }
}