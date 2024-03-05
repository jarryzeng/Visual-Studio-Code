class link{
    constructor(input, status = 0){
        this.input = input;
        this.status = status;
        this.next = undefined;
    }
    makeNext(input){
        if(this.next == undefined) this.next = new link(input, this.status + 1);
        else{
            this.next.makeNext(input);
        }
    }
    show(serialNumber){
        let register = this;
        for(let i = 0;i < serialNumber;i++){
            register = register.next;
        }
        console.log(register.input);
    }
}