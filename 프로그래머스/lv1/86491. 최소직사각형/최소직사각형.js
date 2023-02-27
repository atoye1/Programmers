function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;
    for (let size of sizes) {
    	if (size[0] < size[1]) {
            [size[0], size[1]] = [size[1], size[0]];
        }
        if (size[0] > maxWidth) maxWidth = size[0];
        if (size[1] > maxHeight) maxHeight = size[1];
    }
    return maxWidth * maxHeight;
}