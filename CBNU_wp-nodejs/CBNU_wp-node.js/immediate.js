let cnt = 0;
const id = setImmediate(() => {
    console.log("Hello!");
});

console.log("Hello Node!");
clearImmediate(id);