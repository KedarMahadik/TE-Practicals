import java.util.Scanner;

public class NextFit {


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

        int lastAllocatedBlock = 0; 

        for (int j = 0; j < jobno; j++) {
            boolean jobAllocated = false;
            for (int i = 0; i < blockno; i++) {
                int blockIndex = (lastAllocatedBlock + i) % blockno;

                if (jobs[j] <= blocks[blockIndex] && !flag[blockIndex]) {
                    flag[blockIndex] = true;
                    memoryUtilize += jobs[j];
                    internalFrag[j] = blocks[blockIndex] - jobs[j];
                    System.out.println("Job " + j + " is fitted in block no. " + blockIndex + " with internal fragmentation: " + internalFrag[j]);
                    lastAllocatedBlock = blockIndex;
                    jobAllocated = true;
                    break;
                }
            }
            if (!jobAllocated) {
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

 

    

