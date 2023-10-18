const fs = require("fs");
const buffer = require("buffer");
const { isNullOrUndefined } = require("util");

function printError(local, err){
    console.log(`\nError from ${local}`);
    console.log(err);
    console.log('\n');
}

async function writeFile(location, content){
    try{
        await fs.promises.writeFile(location, content);
    }
    catch(err){ 
        printError('write file', err);
    }
}

async function readFile(location, fileName, search, callback){
    try{
        let file = await fs.promises.readFile(`${location}${fileName}`, 'utf8');
        if(fileName != search && search != '*'){
            printError('read file', 'the file name is different');
            return;
        };
        return file;
    }
    catch(err){
        switch(err.errno){
            case -4068: printError('read file', 'this is directory'); break;
            case -21: printError('read file', 'you are trying to do something on the directory'); break;
            default: printError('read file', err);
        }
    }
}

async function readdir(location="./", search, callback=undefined){
    try{
        let files = await fs.promises.readdir(location);
        files.map((fileName) => readFile(location, fileName, search, callback));
    }
    catch(err){ printError('read directory', err); }
}

let filename = "path.txt";
let fileContent = readdir("./", filename);

/*
for(let i = 0;i < fileContent.length;i++){
    if(fileContent[i] === ':') fileContent[i] = '/n';
}

writeFile("./path.txt", fileContent);
*/