import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class p4963 {
    static int[] dx = {1, -1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, 1, -1, -1, 1, -1, 1};
    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            if (n == 0 & m == 0) break;

            graph = new int[m][n];
            visited = new boolean[m][n];
            count = 0;

            for (int i=0; i<m; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int p=0; p<m; p++) {
                for (int q=0; q<n; q++) {
                    if (graph[p][q] == 1 && !visited[p][q]) {
                        bfs(p, q);
                        count++;
                    }
                }
            }

            System.out.println(count);

        }
    }

    private static void bfs(int p, int q) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{p, q});
        visited[p][q] = true;

        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            int x = xy[0];
            int y = xy[1];
            for (int k=0; k<8; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx>=0 && ny >=0 && nx < n && ny < m) {
                    if (graph[ny][nx] == 1 && !visited[ny][nx]) {
                        queue.add(new int[] {ny, nx});
                        visited[ny][nx] = true;
                    }
                }
            }
        }
    }
}
