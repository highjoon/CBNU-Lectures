let cnt = 0;
const id = setInterval(() => {
    console.log("Hello!");
    cnt++;
    if (cnt >= 3) {
        clearInterval(id);
    }
}, 3000);