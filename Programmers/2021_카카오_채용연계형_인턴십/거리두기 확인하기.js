function solution(places) {
    var answer = [];
    for (const p of places) {
        let flag = 1;

        for (let i = 0; i < 5; i++) {
            for (let j = 0; j < 5; j++) {
                if (flag) {
                    if (p[i][j] == 'P') {
                        let result = bfs(p, i, j, 0);
                        if (!result) {
                            flag = 0;
                        }
                    }
                }
            }
        }
        answer.push(flag);
    }


    return answer;
}

function bfs(p, x, y, d) {

    const di = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const visited = Array.from({ length: 5 }, () => Array(5).fill(0));

    const q = [[x, y, d]];

    while (q.length > 0) {
        const [x, y, d] = q.shift();
        visited[x][y] = 1;

        for (let i = 0; i < 4; i++) {
            const nx = x + di[i][0];
            const ny = y + di[i][1];
            const nd = d + 1;

            if (0 <= nx && nx < 5 && 0 <= ny && ny < 5 && visited[nx][ny] == 0) {
                visited[nx][ny] = 1;

                if (p[nx][ny] == 'P') {
                    if (nd <= 2) {
                        return false;
                    }
                } else if (p[nx][ny] == 'O') {
                    if (nd < 2) {
                        q.push([nx, ny, nd]);
                    }
                }
            }
        }
    }
    return true;


}