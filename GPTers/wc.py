from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
font_path = "C:/Users/LoewllZoe/Downloads/NanumGothicBold.ttf"
img = Image.open(
    "C:/Users/LoewllZoe/Documents/GitHub/Python/GPTers/1200px-Python_icon_(black_and_white).jpeg")
img_array = np.array(img)

# Input your article text here
article = """
package P18405번_경쟁적_전염;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
package P11758번_CCW;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
  public static int x[] = new int[3];
  public static int y[] = new int[3];

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = null;

    for (int i = 0; i < 3; i++) {
      st = new StringTokenizer(br.readLine());
      x[i] = Integer.parseInt(st.nextToken());
      y[i] = Integer.parseInt(st.nextToken());
    }
    System.out.println(CCW());
  }
package P10026번_적록;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };

	static char[][] arr;
	static boolean[][] visited;

	static int N;
	static int count;
	static int count2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		arr = new char[N][N];
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = line.charAt(j);
			}
		}
		Queue<int[]> q = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					q.offer(new int[] { i, j });
					char prev_color = arr[i][j];
					BFS(q, prev_color);
					count++;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == 'G') {
					arr[i][j] = 'R';
				}
			}
		}
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					q.offer(new int[] { i, j });
					char prev_color = arr[i][j];
					BFS(q, prev_color);
					count2++;
				}
			}
		}
		System.out.println(count);
		System.out.println(count2);
	}

	public static void BFS(Queue<int[]> q, char color) {
		Queue<int[]> temp = new LinkedList<>();
		while (!q.isEmpty()) {
			int[] now = q.poll();
			visited[now[0]][now[1]] = true;

			// 상하좌우로 탐색
			for (int k = 0; k < 4; k++) {
				int x = now[0] + dx[k];
				int y = now[1] + dy[k];
				// 해당 인덱스가 배열을 넘어가면 안됨
				if (x >= 0 && y >= 0 && x < N && y < N) {
					// 색이 처음 BFS값과 같아야하고 방문한적 없어야함
					if (arr[x][y] == color && !visited[x][y]) {
						visited[x][y] = true;
						temp.add(new int[] { x, y });
					}
				}
			}
		}
		if (!temp.isEmpty()) {
			BFS(temp, color);
		}
	}
}
  public static int CCW() {
    // (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1) = (x1y2 + x2y3 + x3y1) - (x2y1 + x3y2
    // + x1y3)
    int CCW_result = ((x[1] - x[0]) * (y[2] - y[0])) - ((x[2] - x[0]) * (y[1] - y[0]));
    if (CCW_result < 0)
      return -1;
    else if (CCW_result > 0)
      return 1;
    else
      return 0;
  }
}
public class Main {
  private static int[][] arr;
  private static boolean[][] visited;
  // 상, 하, 좌, 우
  private static int[] dx = { -1, 1, 0, 0 };
  private static int[] dy = { 0, 0, -1, 1 };

  private static int N, K, time;
  private static int S, X, Y;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = null;

    st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    PriorityQueue<Point> pq = new PriorityQueue<>();
    arr = new int[N][N];
    visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        int num = Integer.parseInt(st.nextToken());
        arr[i][j] = num;
        if (num != 0) {
          pq.add(new Point(i, j));
          visited[i][j] = true;
        }
      }
    }

    st = new StringTokenizer(br.readLine());
    S = Integer.parseInt(st.nextToken());
    X = Integer.parseInt(st.nextToken());
    Y = Integer.parseInt(st.nextToken());

    if (S != 0) {
      BFS(pq);
    }
    System.out.println(arr[X - 1][Y - 1]);
  }

  public static void BFS(PriorityQueue<Point> pq) {
    PriorityQueue<Point> temp = new PriorityQueue<>();
    while (!pq.isEmpty()) {
      Point now = pq.poll();
      // System.out.println("cordinates | " + now.x + ", " + now.y + " | " +
      // arr[now.x][now.y]);
      for (int k = 0; k < 4; k++) {
        int x = now.x + dx[k];
        int y = now.y + dy[k];
        if (x >= 0 && y >= 0 && x < N && y < N) {
          if (arr[x][y] == 0 && !visited[x][y]) {
            visited[x][y] = true;
            arr[x][y] = arr[now.x][now.y];
            temp.add(new Point(x, y));
          }
        }
      }
    }
    if (!temp.isEmpty()) {
      // System.out.println("out | T = " + (time + 1));
      // for (int i = 0; i < N; i++) {
      // for (int j = 0; j < N; j++) {
      // System.out.print(arr[i][j] + " ");
      // }
      // System.out.println();
      // }
      if (++time != S) {
        BFS(temp);
      }
    }
  }

  private static class Point implements Comparable<Point> {
    int x;
    int y;

    public Point(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public int compareTo(Point o) {
      return arr[this.x][this.y] - arr[o.x][o.y];
    }
  }
}
"""

# Create a WordCloud object
wordcloud = WordCloud(width=400, height=400, scale=2.0, background_color='white',
                      font_path=font_path, mask=img_array).generate(article)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
