var date = new Date();
var month = date.getMonth();
var year = date.getFullYear();
// var clockDate = date.getDate();
var day = date.getDay();
var hours = date.getHours();
var minutes = date.getMinutes();
if (minutes < 10) {
    minutes = "0" + minutes
}
var seconds = date.getSeconds();
if (seconds < 10) {
    seconds = "0" + seconds
}
var i = 1;
var time = 0;
var w_price = 15;
var c_price = 2;
var br_price = 11;
// (month + 1) + "/" + day + "/" + year + "  " + hours + ":" + minutes + ":" + seconds + "</td>" 

function bid_w() {
    var date_now = new Date();
    document.getElementById("bid_error").innerHTML = "";
    var b_price = Number(document.getElementById("mybid").value);
    var name = "Anonymous"
    if (b_price >= w_price + 0.5) {
        document.getElementById("result").innerHTML +=
            "<tr>" +
            "<td>" + i++ + "</td>" +
            "<td >" + name + "</td>" +
            "<td >" + "$" + b_price + "</td>" +
            "<td >" + date_now.toLocaleString() +
            "</tr>";
        w_price = b_price;
        time++;
        document.getElementById("rate").innerHTML = w_price;
        document.getElementById("mb").innerHTML = w_price + 0.5;
        document.getElementById("cp").innerHTML = w_price;
        document.getElementById("time").innerHTML = time;
        document.getElementById("rmb1").innerHTML = w_price + 0.5;
        document.getElementById("rcp1").innerHTML = w_price;
        document.getElementById("rcp11").innerHTML = w_price;
    } else {
        document.getElementById("bid_error").innerHTML = "Bid Higher Price"
    }

}

function bid_c() {
    var date_now = new Date();
    document.getElementById("bid_error").innerHTML = "";
    var b_price = Number(document.getElementById("mybid").value);
    var name = "Anonymous"
    if (b_price >= c_price + 0.5) {
        document.getElementById("result").innerHTML +=
            "<tr>" +
            "<td>" + i++ + "</td>" +
            "<td >" + name + "</td>" +
            "<td >" + "$" + b_price + "</td>" +
            "<td >" + date_now.toLocaleString() +
            "</tr>";
        c_price = b_price;
        time++;
        document.getElementById("rate").innerHTML = c_price;
        document.getElementById("mb").innerHTML = c_price + 0.5;
        document.getElementById("cp").innerHTML = c_price;
        document.getElementById("time").innerHTML = time;
        document.getElementById("rmb2").innerHTML = c_price + 0.5;
        document.getElementById("rcp2").innerHTML = c_price;
        document.getElementById("rcp22").innerHTML = c_price;
    } else {
        document.getElementById("bid_error").innerHTML = "Bid Higher Price"
    }
}

function bid_b() {
    var date_now = new Date();
    document.getElementById("bid_error").innerHTML = ""
    var b_price = Number(document.getElementById("mybid").value);
    var name = "Anonymous"
    if (b_price >= br_price + 0.5) {
        document.getElementById("result").innerHTML +=
            "<tr>" +
            "<td>" + i++ + "</td>" +
            "<td >" + name + "</td>" +
            "<td >" + "$" + b_price + "</td>" +
            "<td >" + date_now.toLocaleString() +
            "</tr>";
        br_price = b_price;
        time++;
        document.getElementById("rate").innerHTML = br_price;
        document.getElementById("mb").innerHTML = br_price + 0.5;
        document.getElementById("cp").innerHTML = br_price;
        document.getElementById("time").innerHTML = time;
        document.getElementById("rmb3").innerHTML = br_price + 0.5;
        document.getElementById("rcp3").innerHTML = br_price;
        document.getElementById("rcp33").innerHTML = br_price;
    } else {
        document.getElementById("bid_error").innerHTML = "Bid Higher Price"
    }
}