const download = require('download-file');
const fs = require('fs');

let html = "xxxx.html";
const content = fs.readFileSync(html, 'utf8');

function getGifUrls(content) {
    let gifUrls = [];
    let gifUrls2 = [];
    let match;
    const regex = /\S*\.gif/gi;
    const regex2 = /^.*(?=http)/;

    while ((match = regex.exec(content)) !== null) {
        gifUrls.push(match[0]);
    }

    gifUrls.forEach((url) => {
        let index = url.indexOf("http");
        gifUrls2.push(url.substring(index));
    })

    return gifUrls2;
}

let urls = getGifUrls(content)
urls.forEach((url) => {
    console.log(url);
    download(url, "download3", (err) => {
        console.log(err);
    })
})




    // download(url, options, function (err) {
    //     if (err) throw err
    //     console.log("meow")
    // })