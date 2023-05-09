let cancel = document.querySelector("#cancel");
let photos = document.querySelector("#img");
let prev = document.querySelector("#prev");
let photos_left = photos.offsetLeft;
let photos_top = photos.offsetTop;

let x_point = [];
let y_point = [];
let get = [];

let canvas = document.querySelector("#canvas");
let act = canvas.getContext('2d');
act.beginPath();

function draw(){
    canvas.height = canvas.height;

    act.moveTo(x_point[0], y_point[0]);
    for(let i = 1;i < get.length;i++){
        act.lineTo(x_point[i], y_point[i]);
    }

    act.strokeStyle = "#ff0000";
    act.lineWidth = 3;
    act.stroke();
}

canvas.addEventListener("mousedown",(event) => {
    let x = event.pageX - photos_left;
    let y = event.pageY - photos_top;
    x_point.push(x);
    y_point.push(y);
    get.push(`${x},${y}`);
    draw();
    console.log(`get:${get}`);
})

cancel.addEventListener("click",function(){
    get = [];
    x_point = [];
    y_point = [];
    canvas.height = canvas.height;
    console.log(`get:${get}`);
})

prev.addEventListener("click", function(){
    x_point = x_point.slice(0, x_point.length - 1);
    y_point = y_point.slice(0, y_point.length - 1);
    get = get.slice(0, get.length - 1);
    draw();
    console.log(`get:${get}`);
})

window.onload = function(){
    canvas.width = photos.clientWidth;
    canvas.height = photos.clientHeight;
}