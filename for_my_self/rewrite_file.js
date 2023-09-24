const fs = require("fs");
let path;

async function writeFile(location, content){
    try{
        await fs.writeFile(location, content);
    }
    catch(err){
        console.log("Error from write file:");
        console.log(err);
    }
}

async function readFile(location, fileName){
    try{
        await fs.readFile(`${location}${fileName}`);
    }
    catch(err){
        console.log("Error from read file:");
        console.log(err);
    }
}

async function readdir(location){
    try{
        let files = await fs.readdir(location);
        files.map((fileName) => readFile(location, fileName));
    }
    catch(err){
        console.log("Error from read directory:");
        console.log(err);
    }
}

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