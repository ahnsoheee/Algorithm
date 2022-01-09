https://programmers.co.kr/learn/courses/30/lessons/43162?language=javascript

function solution(n, computers) {
    var answer = 0;

    let check = Array.from({ length: n }, () => 0);

    for (let i = 0; i < n; i++) {
        if (check[i] == 0) {
            dfs(i, computers, check);
            answer += 1;
        }
    }

    return answer;
}

function dfs(v, computers, check) {
    check[v] = 1;
    for (let i = 0; i < check.length; i++) {
        if (check[i] == 0 & computers[v][i] == 1) {
            dfs(i, computers, check);

        }
    }
}