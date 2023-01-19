const download = require('download-file');
const fs = require('fs');
const content = fs.readFileSync('全网最全【一二布布】动态表情包！！！持续更新中··· - 知乎.html', 'utf8');

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
    download(url, "/download2", (err) => {
        console.log(err);
    })
})




    // download(url, options, function (err) {
    //     if (err) throw err
    //     console.log("meow")
    // })