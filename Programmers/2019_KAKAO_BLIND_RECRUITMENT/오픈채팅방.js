function solution(record) {
    var answer = [];
    const nickname = new Map();
    record.map((r) => {
        let arr = r.split(' ');
        if (arr[0] == 'Enter' || arr[0] == 'Change') {
            if (nickname.has(arr[1])) {
                nickname.set(arr[1], arr[2]);
            } else {
                nickname.set(arr[1], arr[2]);
            }
        }
    });

    record.map((r) => {
        let arr = r.split(' ');
        if (arr[0] == 'Enter') {
            answer.push(`${nickname.get(arr[1])}님이 들어왔습니다.`);
        } else if (arr[0] == 'Leave') {
            answer.push(`${nickname.get(arr[1])}님이 나갔습니다.`);
        }
    });

    return answer;
}