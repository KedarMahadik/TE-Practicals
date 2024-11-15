import java.util.Scanner;

public class bankers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of processes: ");
        int p = sc.nextInt(); 
        
        System.out.print("Enter the number of resource types: ");
        int r = sc.nextInt(); 
        
        int[][] max = new int[p][r];
        int[][] allocation = new int[p][r];
        int[][] need = new int[p][r];
        int[] available = new int[r];
        boolean[] finished = new boolean[p];
        int[] safeSequence = new int[p];
        
        System.out.println("Enter MAX matrix: ");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                max[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter Allocation matrix: ");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                allocation[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter Available resources: ");
        for (int i = 0; i < r; i++) {
            available[i] = sc.nextInt();
        }

        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                need[i][j] = max[i][j] - allocation[i][j];
            }
        }

        System.out.println("\nMAX matrix:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                System.out.print(max[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nAllocation matrix:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                System.out.print(allocation[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nNeed matrix:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                System.out.print(need[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nAvailable resources:");
        for (int i = 0; i < r; i++) {
            System.out.print(available[i] + " ");
        }
        System.out.println();

        int count = 0;
        while (count < p) {
            boolean found = false;
            
            for (int i = 0; i < p; i++) {
                if (!finished[i]) {
                    int j;
                    for (j = 0; j < r; j++) {
                        if (need[i][j] > available[j]) {
                            break;
                        }
                    }
                    if (j == r) { 
                        for (int k = 0; k < r; k++) {
                            available[k] += allocation[i][k]; 
                        }
                        safeSequence[count++] = i;
                        finished[i] = true;
                        found = true;
                    }
                }
            }

            if (!found) {
                System.out.println("The system is in an unsafe state (deadlock).");
                return;
            }
        }

       
        System.out.print("Safe sequence: ");
        for (int i = 0; i < p; i++) {
            System.out.print("P" + safeSequence[i]);
            if (i != p - 1) {
                System.out.print(" -> ");
            }
        }
        System.out.println();
    sc.close();
    }
}
