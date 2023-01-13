// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, Y, D) {
    let width = Y - X
    let step = parseInt(width / D) + (width % D > 0 ? 1:0)
    return step
}
-->
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, Y, D) {
    let width = Y-X
    if (width < 0) return 1;
    return parseInt(width/D) + (width%D>0?1:0)
}
function solution(X, Y, D) {
    let width = Y - X
﻿    if (width == 0) return 0
    else if (D > width) return 1
    return parseInt(width/D) + (width%D>0?1:0)
}
