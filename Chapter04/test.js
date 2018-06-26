function f () {
    console.log(x);
}
function g () {
    console.log(x);
    let x = 3;
}

let x = 5;
f();
x = 6;
g();
