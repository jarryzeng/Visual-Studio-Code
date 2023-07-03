class game{
    constructor(width, height){
        this.grid = [];
        this.weight = 1.25;
        this.width = width;
        this.height = height;
        this.blank = "blank";
        this.statusBoom = "boom";
        this.statusMask = "mask";
        this.statusSpace = "space";
        this.statusNumber = "number";
        this.table = document.querySelector("#table");
        this.#createMap();
        this.#createBoom();
        this.#appendTdNeighbor();
        this.#makeNumber();
        this.#createMask();
        this.#checkGrid();
        this.#createEvent();
    }
    #createMap(){
        for(let i = 0;i < this.height;i++){
            let tr = document.createElement("tr");
            this.grid.push([]);
            for(let j = 0;j < this.width;j++){
                let td = document.createElement("td");
                td.classList.add("block");
                td.classList.add(this.statusSpace);
                this.grid[i].push(td);
                this.grid[i][j].status = this.statusSpace;
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
            else{
                this.grid[y][x].classList.remove(this.statusSpace);
                this.grid[y][x].classList.add(this.statusBoom);
                this.grid[y][x].status = this.statusBoom;
            }
            boomSize = document.querySelectorAll(`.${this.statusBoom}`).length;
        }
        while(boomSize < (this.width + this.height) * this.weight);
    }
    #appendTdNeighbor(){
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                let leftUp = -1;
                let rightUp = -1;
                let leftBottom = -1;
                let rightBottom = -1;
                if(i - 1 >= 0){
                    this.grid[i][j].up = this.grid[i - 1][j];
                    leftUp += 1;
                    rightUp += 1;
                }
                if(j - 1 >= 0){
                    this.grid[i][j].left = this.grid[i][j - 1];
                    leftUp += 1;
                    leftBottom += 1;
                }
                if(j + 1 < this.width){
                    this.grid[i][j].right = this.grid[i][j + 1];
                    rightUp += 1;
                    rightBottom += 1;
                }
                if(i + 1 < this.height){
                    this.grid[i][j].bottom = this.grid[i + 1][j];
                    leftBottom += 1;
                    rightBottom += 1;
                }
                if(leftUp == 1)this.grid[i][j].leftUp = this.grid[i - 1][j - 1];
                if(rightUp == 1)this.grid[i][j].rightUp = this.grid[i - 1][j + 1];
                if(leftBottom == 1)this.grid[i][j].leftBottom = this.grid[i + 1][j - 1];
                if(rightBottom == 1)this.grid[i][j].rightBottom = this.grid[i + 1][j + 1];
            }
        }
    }
    #makeNumber(){
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                if(this.grid[i][j].classList.contains(this.statusBoom)) continue;
                let total = 0;
                if(this.grid[i][j].up != undefined && this.grid[i][j].up.status == this.statusBoom) total += 1;
                if(this.grid[i][j].left != undefined && this.grid[i][j].left.status == this.statusBoom) total += 1;
                if(this.grid[i][j].right != undefined && this.grid[i][j].right.status == this.statusBoom) total += 1;
                if(this.grid[i][j].bottom != undefined && this.grid[i][j].bottom.status == this.statusBoom) total += 1;
                if(this.grid[i][j].leftUp != undefined && this.grid[i][j].leftUp.status == this.statusBoom) total += 1;
                if(this.grid[i][j].rightUp != undefined && this.grid[i][j].rightUp.status == this.statusBoom) total += 1;
                if(this.grid[i][j].leftBottom != undefined && this.grid[i][j].leftBottom.status == this.statusBoom) total += 1;
                if(this.grid[i][j].rightBottom != undefined && this.grid[i][j].rightBottom.status == this.statusBoom) total += 1;
                if(total){
                    this.grid[i][j].status = this.statusNumber;
                    this.grid[i][j].innerHTML = total;
                    this.grid[i][j].classList.add(this.statusNumber);
                    this.grid[i][j].classList.remove(this.statusSpace);
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
    #checkGrid(){
        this.register = [];
        this.nodeRegister = [];
        for(let i = 0;i < this.height;i++){
            this.register.push([]);
            let start = undefined;
            let end = undefined;
            for(let j = 0;j < this.width;j++){
                if(start == undefined && this.grid[i][j].status == this.statusSpace){
                    start = j;
                    end = undefined;
                }
                if(start != undefined && end == undefined && this.grid[i][j].status != this.statusSpace) end = j - 1;
                else if(start != undefined && end == undefined && j == this.width - 1) end = j;
                if(start != undefined && end != undefined){
                    this.register[i].push([start, end]);
                    start = undefined;
                }
            }
            if(this.register[i].length == 0) this.register[i] = this.blank;
            if(i) this.#makeGroup(i);
        }
    }
    #makeGroup(height){
        if(this.register[height - 1] == this.blank) return;
        for(let upLayer of this.register[height - 1]){
            for(let thisLayer of this.register[height]){
                if(thisLayer[0] <= upLayer[1] && thisLayer[1] >= upLayer[0]){
                    
                }
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
            }
        }
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                this.grid[i][j].onclick = event;
            }
        }
    }
}

new game(20,20);