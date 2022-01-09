https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript

function solution(progresses, speeds) {
    var answer = [];

    let remain = [];
    for (let i = 0; i < progresses.length; i++) {
        remain.push(Math.ceil((100 - progresses[i]) / speeds[i]));
    }

    let idx = 0;
    for (let i = 0; i < progresses.length; i++) {
        if (remain[i] > remain[idx]) {
            answer.push(i - idx);
            idx = i;
        }
    }
    answer.push(remain.length - idx);

    return answer;
}