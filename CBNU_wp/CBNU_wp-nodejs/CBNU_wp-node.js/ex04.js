let cnt = 0;
setInterval(() => {
    cnt++;
    console.log(cnt)
    if (cnt >= 3) process.exit(0);
}, 2000)