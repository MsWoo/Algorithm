import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class p18405 {

    public static class Node {
        int x;
        int y;
        int value;
        int time;
        public Node(int x, int y, int value, int time) {
            this.x = x;
            this.y = y;
            this.value = value;
            this.time = time;
        }
    }
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int n, k, s, x, y;
    static int graph[][];
    static int count = 0;
    static Queue<Node> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        ArrayList<Node> list = new ArrayList<>();

        graph = new int[n][n];
        for (int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] != 0) {
                    list.add(new Node(i, j, graph[i][j], 0));
                }
            }
        }

        Collections.sort(list, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.value - o2.value;
            }
        });
        q = new LinkedList<>();
        for (Node node : list) {
            q.add(node);
        }

        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        bfs();
        System.out.println(graph[x-1][y-1]);

    }

    private static void bfs() {
        while (!q.isEmpty()) {
            Node node = q.poll();
            if (node.time == s) {
                break;
            }
            int x = node.x;
            int y = node.y;
            int val = node.value;
            for (int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx >= 0 && ny >= 0 && nx <n&&ny<n) {
                    if (graph[nx][ny] == 0) {
                        graph[nx][ny] = val;
                        q.add(new Node(nx, ny, val, node.time+1));
                    }
                }
            }
        }

    }
}
