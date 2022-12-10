function solution(nums) {
    const monsterSet = new Set(nums);
    if (monsterSet.size >= parseInt(nums.length / 2)) {
        return (nums.length / 2)
    } else {
        return monsterSet.size;
    }
}