class game{
    constructor(width, height){
        this.grid = [];
        this.width = width;
        this.height = height;
        this.statusBoom = "boom";
        this.statusMask = "mask";
        this.statusNumber = "number";
        this.table = document.querySelector("#table");
        this.#createMap();
        this.#createBoom();
        this.#makeNumber();
        this.#createMask();
        this.#createEvent();
    }
    #createMap(){
        for(let i = 0;i < this.height;i++){
            let tr = document.createElement("tr");
            this.grid.push([]);
            for(let j = 0;j < this.width;j++){
                let td = document.createElement("td");
                td.classList.add("block");
                this.grid[i].push(td);
                tr.appendChild(td);
            }
            this.table.appendChild(tr);
        }
    }
    #createBoom(){
        let boomSize = 0;
        do{
            let x = Math.floor(Math.random() * this.width);
            let y = Math.floor(Math.random() * this.height);
            
            if(this.grid[y][x].classList.contains(this.statusBoom)) continue;
            else this.grid[y][x].classList.add(this.statusBoom);
            boomSize = document.querySelectorAll(`.${this.statusBoom}`).length;
        }
        while(boomSize < this.width + this.height);
    }
    #makeNumber(){
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                if(this.grid[i][j].classList.contains(this.statusBoom)) continue;
                let total = 0;
                let leftUp = -1;
                let rightUp = -1;
                let leftBottom = -1;
                let rightBottom = -1;
                if(i - 1 >= 0){
                    if(this.grid[i - 1][j].classList.contains(this.statusBoom)) total += 1;
                    leftUp += 1;
                    rightUp += 1;
                }
                if(j - 1 >= 0){
                    if(this.grid[i][j - 1].classList.contains(this.statusBoom)) total += 1;
                    leftUp += 1;
                    leftBottom += 1;
                }
                if(j + 1 < this.width){
                    if(this.grid[i][j + 1].classList.contains(this.statusBoom)) total += 1;
                    rightUp += 1;
                    rightBottom += 1;
                }
                if(i + 1 < this.height){
                    if(this.grid[i + 1][j].classList.contains(this.statusBoom)) total += 1;
                    leftBottom += 1;
                    rightBottom += 1;
                }
                if(leftUp == 1 && this.grid[i - 1][j - 1].classList.contains(this.statusBoom)) total += 1;
                if(rightUp == 1 && this.grid[i - 1][j + 1].classList.contains(this.statusBoom)) total += 1;
                if(leftBottom == 1 && this.grid[i + 1][j - 1].classList.contains(this.statusBoom)) total += 1;
                if(rightBottom == 1 && this.grid[i + 1][j + 1].classList.contains(this.statusBoom)) total += 1;
                if(total){
                    this.grid[i][j].innerHTML = total;
                    this.grid[i][j].classList.add(this.statusNumber);
                }
            }
        }
    }
    #createMask(){
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                this.grid[i][j].classList.add(this.statusMask);
            }
        }
    }
    #createEvent(){
        let event = function(){
            let statusMask = "mask";
            let statusBoom = "boom";
            this.classList.remove(statusMask);
            if(this.classList.contains(statusBoom)){
                let boom = document.querySelectorAll(`.${statusBoom}`);
                for(let i of boom) i.classList.remove(statusMask);
                alert("Game Over");
            };
        }
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                this.grid[i][j].onclick = event;
            }
        }
    }
}

new game(20,20);