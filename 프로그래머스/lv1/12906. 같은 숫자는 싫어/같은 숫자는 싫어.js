function solution(arr)
{
   return arr.reduce((acc, cur) => {
       if (acc[acc.length - 1] === cur) return acc;
       acc.push(cur);
       return acc;
   }, []) 
}