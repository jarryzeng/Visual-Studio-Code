let cancel = document.querySelector("#cancel");
let photos = document.querySelector("#img");
let prev = document.querySelector("#prev");
let photos_left = photos.offsetLeft;
let photos_top = photos.offsetTop;

let get = [];

photos.addEventListener("mousedown",(event) => {
    let x = event.pageX - photos_left;
    let y = event.pageY - photos_top;
    get.push(`${x},${y}`);
    console.log(`get:${get}`);
})

cancel.addEventListener("click",function(){
    get = [];
    console.log(`get:${get}`);
})

prev.addEventListener("click",function(){
    get = get.slice(0,get.length-1);
    console.log(`get:${get}`);
})