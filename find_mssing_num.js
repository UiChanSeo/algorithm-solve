// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    A.sort()
    console.log(A)
    const length = A.length
    let last = A[length-1]
    let mid = A[parseInt(length/2)]
    while (mid>0) {}
        if (A[mid] == (last - mid)) {
         mid = parseInt((last - mid) /2)
        } 
        let last = A[length-1]
        let mid = A[parseInt(length/2)]

    }
}
