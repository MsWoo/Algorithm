import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p14888 {

    static int maxValue = Integer.MIN_VALUE;
    static int minValue = Integer.MAX_VALUE;
    static int n;
    static int[] number;
    static int[] operator = new int[4];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        number = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<4; i++) {
            operator[i] = Integer.parseInt(st.nextToken());
        }

        dfs(number[0], 1);

        System.out.println(maxValue);
        System.out.println(minValue);

    }

    public static void dfs(int sum, int index) {
        if (index == n) {
            maxValue = Math.max(maxValue, sum);
            minValue = Math.min(minValue, sum);
        }

        for (int i=0; i<4; i++) {
            if (operator[i] > 0) {
                operator[i]--;

                if (i == 0) {
                    dfs(sum + number[index], index + 1);
                } else if (i == 1) {
                    dfs(sum - number[index], index + 1);
                } else if (i == 2) {
                    dfs(sum * number[index], index + 1);
                } else {
                    dfs(sum / number[index], index + 1);
                }

                operator[i]++;
            }
        }
    }

}
