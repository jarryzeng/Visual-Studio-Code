const fs = require("fs");
const path = "D:\\Visual studio code\\project\\petStore\\member\\member_data\\";

fs.readdir(`${path}`, (err, files) => {
    if(err) console.log(err);
    else{
        files.map((fname)=>{
            fs.readFile(`${path}${fname}`, (err, detail) => {
                if(err) console.log(err);
                else{
                    let file = JSON.parse(detail);
                    if(file["contact-data-number-2"] != undefined){
                        let value = file["contact-data-number-2"];
                        delete file["contact-data-number-2"];
                        file["contact-data-phone_number-2"] = value;
                        fs.writeFile(`${path}${fname}`, JSON.stringify(file), (err) => {
                            if(err) console.log(err);
                        });
                    }
                }
            });
        });
    }
});