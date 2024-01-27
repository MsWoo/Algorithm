import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class p1920 {

    static int n, m;
    static int[] A;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        A = new int[n];
        for (int i=0; i<n; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);

        m = sc.nextInt();
        for (int i=0; i<m; i++) {
            boolean find = false;
            int target = sc.nextInt();

            int start = 0;
            int end = A.length-1;

            while (start <= end) {
                int mid = (start+end) / 2;
                int midValue = A[mid];

                if (midValue > target) {
                    end = mid - 1;
                } else if (midValue < target) {
                    start = mid + 1;
                } else {
                    find = true;
                    break;
                }

            }
            if (find) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }

        }
    }
}
