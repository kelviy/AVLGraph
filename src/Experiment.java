import java.io.*;
import java.util.ArrayList;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * Experiment class to run the experiment for the assignment. The main class is also included in this class. 
 */
public class Experiment{

    // AVL Tree data structure
    private AVLTree<GenericData> dataStructure = new AVLTree<>();

    // Sets to store the search and insert counts for each N
    private SortedMap<Integer, TreeSet<Integer>> searchCount = new TreeMap<>();
    private SortedMap<Integer, TreeSet<Integer>> insertCount = new TreeMap<>();

    /**
     * Main method to run the experiment. The experiment will run for each N in the range array. The experiment will load data from the GenericsKB.txt file and then run the experiment for each N. The experiment will then save the insert and search counts to the insertCount.txt and searchCount.txt files respectively. The experiment will then run part 1 of the assignment. The search and insert data would also be cleared prior to running the experiments. 
     * @param args
     */
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


        int[] range = {10, 100, 1000, 2000, 5000, 10000, 15000, 25000, 35000, 43000, 50000};
        Experiment theExperiment = new Experiment();
        
        for (int n : range) {
            theExperiment.experiment(n);
        }

        theExperiment.saveInsertCount();
        theExperiment.saveSearchCount();

        theExperiment.part1();
    }

    /**
     * Part 1 of the assignment. This method will load the data from the GenericsKB.txt file and then run the queries from the test-queries.txt file. The output will be printed to the console. test-queires.txt file can be replaced by GenericsKB-queries.txt file to test more queries. 
     */
    public void part1() {
        loadData("data/GenericsKB.txt", 50000);

        try {
            BufferedReader reader = new BufferedReader(new FileReader("data/test-queries.txt"));
            String line;

            while((line = reader.readLine()) != null) {
                GenericData query = new GenericData(line, null, 0);
                BinaryTreeNode<GenericData> searchResult = dataStructure.find(query);

                System.out.println("Searching for: " + line);
                System.out.print("Output: ");

                if (searchResult == null) {
                    System.out.println("Term not found: " + line);
                } else {
                    System.out.println(searchResult.getData());
                }

                System.out.println();
            }

            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    /**
     * Runs the experiment for a given N. The experiment will load data from the GenericsKB.txt file and then run the queries from the GenericsKB-queries.txt file. The search and insert counts will be stored in the searchCount and insertCount sets respectively.
     * @param n
     */
    public void experiment(int n) {
        loadData("data/GenericsKB.txt", n);
        try {
            BufferedReader reader = new BufferedReader(new FileReader("data/GenericsKB-queries.txt"));
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
    public void loadData(String fileName, int n) {
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

    /**
     * Saves the insert count to the insertCount.txt file.
     */
    public void saveInsertCount() {
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

    /**
     * Saves the search count to the searchCount.txt file.
     */
    public void saveSearchCount() {
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