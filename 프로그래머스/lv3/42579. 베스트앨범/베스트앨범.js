function solution(genres, plays) {
    const counter = {};
    for (let i = 0; i < genres.length; i++) {
        let currentGenre = genres[i];
        let currentPlay = plays[i];
        if (counter.hasOwnProperty(currentGenre)) {
            let currentTop2Value = counter[currentGenre][2];
            let currentTop2Index = counter[currentGenre][1];
            let genreTotal = counter[currentGenre][0] + currentPlay;
            if (currentPlay > currentTop2Value[0]) {
                counter[currentGenre] = [genreTotal, [i, currentTop2Index[0]], [currentPlay, currentTop2Value[0]]]
            } else if (currentPlay === currentTop2Value[0]) {
                // 첫번째 원소와 같은데, 두 번째 원소와도 같다면 인덱스 비교를 세개를 놓고 새로 해야한다.
                if (currentPlay === currentTop2Value[1]) {
                    currentTop2Index.push(i)
                    const newIdx = currentTop2Index.sort().slice(0,2);
                    counter[currentGenre] = [genreTotal, newIdx, [currentPlay, currentTop2Value[0]]]
                } else {
                    counter[currentGenre] = [genreTotal, [i, currentTop2Index[0]].sort(), [currentPlay, currentTop2Value[0]]]
                }
            } else if (currentPlay > currentTop2Value[1]) {
                counter[currentGenre] = [genreTotal, [currentTop2Index[0], i], [currentTop2Value[0], currentPlay]]
            } else if (currentPlay === currentTop2Value[1]) {
                const lowerIdx = currentTop2Index[1] > i ? i : currentTop2Index[1];
                counter[currentGenre] = [genreTotal, [currentTop2Index[0], lowerIdx], [currentTop2Value[0], currentPlay]]
            } else {
                counter[currentGenre] = [genreTotal, currentTop2Index, currentTop2Value];
            }
        } else { // 카운터에 새로운 장르를 등록, 합계, 고유번호, 고유번호에 해당하는 재생수를 넣는다.
            counter[currentGenre] = [currentPlay, [i], [currentPlay, -1]];
        }
    }
    return Object.entries(counter).sort((a,b) => b[1][0] - a[1][0]).reduce((acc, cur) => {
        return [...acc, ...cur[1][1]]
    },[])
}