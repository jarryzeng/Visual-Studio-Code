class game{
    constructor(width, height, weight){
        this.grid = [];
        this.weight = weight;
        this.width = width;
        this.height = height;
        this.blank = "blank";
        this.firstOfblock = true;
        this.statusBoom = "boom";
        this.statusMask = "mask";
        this.statusSpace = "space";
        this.statusNumber = "number";
        this.table = document.querySelector("#table");
        this.#createMap();
        this.#appendTdNeighbor();
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
                td.classList.add(this.statusSpace);
                this.grid[i].push(td);
                this.grid[i][j].status = this.statusSpace;
                this.grid[i][j].position = [i, j];
                tr.appendChild(td);
            }
            this.table.appendChild(tr);
        }
    }
    #createBoom(position){
        let boomSize = 0;
        do{
            let x = Math.floor(Math.random() * this.width);
            let y = Math.floor(Math.random() * this.height);

            if(this.grid[y][x].classList.contains(this.statusBoom) || (y == position[0] && x == position[1])) continue;
            else{
                this.grid[y][x].classList.remove(this.statusSpace);
                this.grid[y][x].classList.add(this.statusBoom);
                this.grid[y][x].status = this.statusBoom;
            }
            boomSize = document.querySelectorAll(`.${this.statusBoom}`).length;
        }
        while(boomSize < (this.width * this.height / Math.abs(this.width - this.height)) * this.weight);
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
    static contains(list, object){
        for(let i of list){
            if(i == object) return true;
        }
        return false;
    }
    static makeGroup(point){
        let localUpList = [];
        let localLeftList = [];
        let localRightList = [];
        let localBottomList = [];
        let check = function(registerPoint, status){
            if(registerPoint != undefined) return registerPoint.classList.contains(status);
            else return false;
        }

        // 若point的class中不包含space則回傳
        if(!point.classList.contains("space")) return;
        
        // 檢查上下左右 是否存在、被遮住且為 number 或 space，如果都為 true 則去除 mask
        if(point.leftUp != undefined && check(point.leftUp, "mask") && check(point.leftUp, "number")) point.leftUp.classList.remove("mask");
        if(point.right != undefined && check(point.rightUp, "mask") && check(point.rightUp, "number")) point.rightUp.classList.remove("mask");
        if(point.up != undefined && check(point.up, "mask") && (check(point.up, "number") || check(point.up, "space"))) point.up.classList.remove("mask");
        if(point.leftBottom != undefined && check(point.leftBottom, "mask") && check(point.leftBottom, "number")) point.leftBottom.classList.remove("mask");
        if(point.rightBottom != undefined && check(point.rightBottom, "mask") && check(point.rightBottom, "number")) point.rightBottom.classList.remove("mask");
        if(point.left != undefined && check(point.left, "mask") && (check(point.left, "number") || check(point.left, "space"))) point.left.classList.remove("mask");
        if(point.right != undefined && check(point.right, "mask") && (check(point.right, "number") || check(point.right, "space"))) point.right.classList.remove("mask");
        if(point.bottom != undefined && check(point.bottom, "mask") && (check(point.bottom, "number") || check(point.bottom, "space"))) point.bottom.classList.remove("mask");
        // 把四周所有是空白的區塊都放進 localList 裡
        while(point.up != undefined && check(point.up, "space")){ if(!game.contains(localUpList, point.up)) localUpList.push(point.up); point.up = point.up.up; }
        while(point.left != undefined && check(point.left, "space")){ if(!game.contains(localLeftList, point.left)) localLeftList.push(point.left); point.left = point.left.left; }
        while(point.right != undefined && check(point.right, "space")){ if(!game.contains(localRightList, point.right)) localRightList.push(point.right); point.right = point.right.right; }
        while(point.bottom != undefined && check(point.bottom, "space")){ if(!game.contains(localBottomList, point.bottom)) localBottomList.push(point.bottom); point.bottom = point.bottom.bottom; }
        // 遍歷某一個方向的list 並且遞迴
        for(let i of localUpList) game.makeGroup(i);
        for(let i of localLeftList) game.makeGroup(i);
        for(let i of localRightList) game.makeGroup(i);
        for(let i of localBottomList) game.makeGroup(i);
    }
    #event(ignoreThis, event){
        if(this.firstOfblock){
            this.#createBoom(event.srcElement.position);
            this.#makeNumber();
            this.firstOfblock = false;
        }
        let statusMask = "mask";
        let statusBoom = "boom";
        let statusSpace = "space";
        event.target.classList.remove(statusMask);
        if(event.target.classList.contains(statusBoom)){
            let boom = document.querySelectorAll(`.${statusBoom}`);
            for(let i of boom) i.classList.remove(statusMask);
            alert("Game Over");
            return;
        }
        else if(event.target.classList.contains(statusSpace)) game.makeGroup(event.target);
        
        let maskSize = document.querySelectorAll(".mask").length;
        let boomSize = document.querySelectorAll(".boom").length;
        if(maskSize == boomSize){
            alert("You Win This Game"); 
            return;
        }
    }
    #createEvent(){
        for(let i = 0;i < this.height;i++){
            for(let j = 0;j < this.width;j++){
                this.grid[i][j].onclick = this.#event.bind(this,event);
            }
        }
    }
}

new game(49, 33, 0);