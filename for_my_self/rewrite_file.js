const fs = require("fs");

let sys = process.platform;

function printSuccess(message){
    switch(sys){
        case "linux": console.log(`\x1B[32m${message}`); break;
        default:console.log(message);
    }
}

function printError(local, err){
    let errorMassage = `Error from ${local}.\n${err}`;
    switch(sys){
        case "linux": console.log(`\x1B[31m${errorMassage}`); break;
        default: console.log(errorMassage);
    }
}

function funcFinish(local){
    console.log(`${local} is finish work.\n`)
}

async function writeFile(location, content){
    try{
        await fs.promises.writeFile(location, content);
    }
    catch(err){ 
        printError('write file', err);
    }
    finally{ funcFinish('write file'); }
}

async function readFile(location, fileName, search, callback){
    try{
        let file = await fs.promises.readFile(`${location}${fileName}`, 'utf8');
        if(fileName != search && search != '*'){
            printError('read file', 'the file name is different.');
            return;
        };
        if(callback != undefined) callback(file);
    }
    catch(err){
        switch(err.errno){
            case -4068: printError('read file', 'this is directory.'); break;
            case -21: printError('read file', 'you are trying to do something on the directory.'); break;
            default: printError('read file', err);
        }
    }
    finally{ funcFinish('read file'); }
}

async function readdir(location="./", search, callback=undefined){
    try{
        let files = await fs.promises.readdir(location);
        files.map((fileName) => readFile(location, fileName, search, callback));
    }
    catch(err){ printError('read directory', err); }
    finally{ funcFinish('read directory'); }
}

let filename = "path.txt";
readdir("./", filename, function(file){
    file = file.split(':').join('\n');
    writeFile(filename, file);
    readdir("./", filename, callback=(file) => {
        printSuccess("file is change.");
    })
});