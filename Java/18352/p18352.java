import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class p18352 {

    static int n,m,k,x;
    static int[] visited;
    static ArrayList<Integer>[] graph;
    static List<Integer> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n+1];
        answer = new ArrayList<>();

        for (int i=1; i<=n; i++) {
            graph[i] = new ArrayList();
        }

        for (int i=1; i<=m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            graph[s].add(e);
        }

        visited = new int[n+1];
        for (int i=0; i<=n; i++) {
            visited[i] = -1;
        }

        //

        bfs(x);

        for (int i=0; i<=n; i++) {
            if (visited[i] == k) {
                answer.add(i);
            }
        }

        if (answer.isEmpty()) {
            System.out.println("-1");
        }
        else {
            Collections.sort(answer);
            for (int ans : answer) {
                System.out.println(ans);
            }
        }

    }

    private static void bfs(int x) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        visited[x]++;

        while (!queue.isEmpty()) {
            int nowCur = queue.poll();

            for (int target : graph[nowCur]) {
                if (visited[target] == -1) {
                    visited[target] = visited[nowCur] + 1;
                    queue.add(target);
                }
            }
        }
    }
}
