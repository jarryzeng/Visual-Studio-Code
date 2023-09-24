const fs = require("fs");
const buffer = require("buffer");

function printError(local, err){
    console.log(`\nError from ${local}`);
    console.log(err);
    console.log('\n');
}

async function writeFile(location, content){
    try{
        await fs.promises.writeFile(location, content);
    }
    catch(err){ printError('write file', err); }
}

async function readFile(location, fileName, search){
    try{
        let file = await fs.promises.readFile(`${location}${fileName}`, 'utf8');
        if(fileName != search && search != '*'){
            printError('read file', 'the file name is different');
            return;
        };
        writeFile(`${location}${fileName}`, file);
    }
    catch(err){
        switch(err.errno){
            case -4068: printError('read file', 'this is directory'); break;
            default: printError('read file', err);
        }
    }
}

async function readdir(location, search){
    try{
        let files = await fs.promises.readdir(location);
        files.map((fileName) => readFile(location, fileName, search));
    }
    catch(err){ printError('read directory', err); }
}

readdir("./", "rewrite_file.js");

// fs.readdir(`${path}`, (err, files) => {
//     if(err) console.log(err);
//     else{
//         files.map((fname)=>{
//             fs.readFile(`${path}${fname}`, (err, detail) => {
//                 if(err) console.log(err);
//                 else{
//                     let file = JSON.parse(detail);
//                     if(file["contact-data-number-2"] != undefined){
//                         let value = file["contact-data-number-2"];
//                         delete file["contact-data-number-2"];
//                         file["contact-data-phone_number-2"] = value;
//                         fs.writeFile(`${path}${fname}`, JSON.stringify(file), (err) => {
//                             if(err) console.log(err);
//                         });
//                     }
//                 }
//             });
//         });
//     }
// });