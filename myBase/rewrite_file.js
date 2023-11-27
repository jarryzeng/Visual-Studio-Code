const fs = require("fs");

let sys = process.platform;

function printSuccess(local){
    let successMessage = `${local} is success!`
    switch(sys){
        case "linux":
            console.log(`\x1B[32m${successMessage}`);
            break;
        default:console.log(successMessage);
    }
}

function printError(local, err){
    let errorMassage = `Error from ${local}.\n${err}`;
    switch(sys){
        case "linux":
            console.log(`\x1B[31m${errorMassage}`);
            break;
        default: console.log(errorMassage);
    }
}

function funcFinish(local){
    switch(sys){
        case "linux":
            console.log(`\x1B[0m${local} is finish work.\n`);
            break;
        default: console.log(`${local} is finish work.\n`);
    }
}

async function writeFile(location, content){
    try{
        await fs.promises.writeFile(location, content);
        printSuccess('write file');
    }
    catch(err){ 
        printError('write file', err);
    }
    finally{ funcFinish('write file'); }
}

async function searchFile(location, fileName, searchName, callback){
    try{
        let file = await fs.promises.readFile(`${location}${fileName}`, 'utf8');
        if(fileName != searchName && searchName != '*'){
            printError('read file', 'the file name is different.');
            return;
        };
        if(callback != undefined) callback(file);
        printSuccess('read file');
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

async function readdir(location="./", callback=undefined){
    try{
        let files = await fs.promises.readdir(location);
        if(callback != undefined) callback(files);
        printSuccess('read directory');
    }
    catch(err){ printError('read directory', err); }
    finally{ funcFinish('read directory'); }
}

let filename = "path.txt";
readdir("./", (files) => {
    files.map((file) => searchFile("./", filename, file, (file) => {
        file = file.split(':').join('\n');
        writeFile(filename, file);
    }));
});