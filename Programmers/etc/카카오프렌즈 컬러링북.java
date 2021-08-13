class Solution {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int num = 0;
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        int[][] visited = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if ((picture[i][j] > 0) && visited[i][j] == 0) {
                    numberOfArea++;
                    check(picture, i, j, visited);
                    
                    if (maxSizeOfOneArea < num) {
                        maxSizeOfOneArea = num;
                    }
                    num = 0;
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
    
    public int check(int[][] picture, int x, int y, int[][] visited) {
        if (visited[x][y] == 1) return 0;
        visited[x][y] = 1;
        num++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (0 <= nx && nx < picture.length && 0 <= ny && ny < picture[0].length) {
                if (picture[x][y] == picture[nx][ny] && visited[nx][ny] == 0) {
                    check(picture, nx, ny, visited);
                }
            }
        }
        return 0;
    }
}