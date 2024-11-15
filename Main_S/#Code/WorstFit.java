import java.util.Scanner;

public class WorstFit {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int memoryUtilize = 0;

        System.out.println("Enter the number of jobs: ");
        int jobno = scanner.nextInt();

        System.out.println("Enter the number of blocks: ");
        int blockno = scanner.nextInt();

        int[] jobs = new int[jobno];
        int[] blocks = new int[blockno];
        boolean[] flag = new boolean[blockno];
        int[] internalFrag = new int[jobno];

        System.out.println("Enter the sizes of jobs: ");
        for (int j = 0; j < jobno; j++) {
            jobs[j] = scanner.nextInt();
        }

        System.out.println("Enter the sizes of blocks: ");
        for (int i = 0; i < blockno; i++) {
            blocks[i] = scanner.nextInt();
        }

        for (int j = 0; j < jobno; j++) {
            int worstIndex = -1;
            for (int i = 0; i < blockno; i++) {
                if (jobs[j] <= blocks[i] && !flag[i]) {
                    if (worstIndex == -1 || blocks[i] > blocks[worstIndex]) {
                        worstIndex = i; 
                    }
                }
            }
            if (worstIndex != -1) {
                flag[worstIndex] = true; 
                memoryUtilize += jobs[j];
                internalFrag[j] = blocks[worstIndex] - jobs[j];
                System.out.println("Job " + j + " is fitted in block no. " + worstIndex + " with internal fragmentation: " + internalFrag[j]);
            } else {
                System.out.println("Job " + j + " cannot be allocated.");
            }
        }

        System.out.println("Total memory utilized: " + memoryUtilize);
        System.out.println("Internal Fragmentation for each job: ");
        for (int j = 0; j < jobno; j++) {
            System.out.println("Job " + j + ": " + internalFrag[j]);
        }
    }
}

 
