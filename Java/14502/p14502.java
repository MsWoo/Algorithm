import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class p14502 {

    // 0 빈칸, 1 벽, 2 바이러스
    // dfs로 벽을 세우는 모든 경우의 수
    // bfs로 바이러스를 퍼트린다.

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] originGraph;
    static int maxValue = Integer.MIN_VALUE;
    static int n, m;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        originGraph = new int[n][m];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                originGraph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);

        System.out.println(maxValue);

    }

    private static void dfs(int count) {
        if (count == 3) {
            bfs();
            return;
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (originGraph[i][j] == 0) {
                    originGraph[i][j] = 1;
                    dfs(count+1);
                    originGraph[i][j] =0;
                }
            }
        }
    }

    private static void bfs() {
        Queue<int[]> queue = new LinkedList<>();

        int graph[][] = new int[n][m];

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                graph[i][j] = originGraph[i][j];
                if (graph[i][j] == 2) {
                    queue.add(new int[] {i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            int x = xy[0];
            int y = xy[1];

            for (int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (graph[nx][ny] == 0) {
                        graph[nx][ny] = 2;
                        queue.add(new int[]{nx,ny});
                    }
                }
            }
        }

        checkMaxValue(graph);
    }

    private static void checkMaxValue(int[][] graph) {
        int safe = 0;
        for (int i=0; i< graph.length; i++) {
            for (int j=0; j<graph[0].length; j++) {
                if (graph[i][j] == 0) {
                    safe++;
                }
            }
        }
        maxValue = Math.max(maxValue, safe);
    }

}
