// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    let left = A[0]
    let right = 0
    let min = 100000    
    if (A.length == 2) {
        min = Math.abs(A[1] - A[0])
    } else {
        A.forEach(a=>right+=a)
        right -=left
        for(let i = 1; i<=A.length;i++)
        {
            var tmin = Math.abs(left - right)
            if (min > tmin) min = tmin
            left += A[i]
            right -= A[i]
        }
    }
    return min
}
