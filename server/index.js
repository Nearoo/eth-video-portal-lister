var express = require('express');
var request = require("request");
var app = express();
const port = process.env.PORT | 5000;

app.get("/", (req, res)=>{
    res.sendFile(__dirname + "/index.html");
});

app.get("/expl1", (req, res)=>{
    res.sendFile(__dirname + "/expl1.png");
})
app.get("/expl2", (req, res)=>{
    res.sendFile(__dirname + "/expl2.png");
})

app.get("/external.m3u", (req, res)=>{
    res.set("Content-Type", "application/mpegurl")
    res.send("#EXTM3U\n" + req.query.url);
});

app.get("/proxy", (req, res)=> {
    // Pipe express request parameters to request object, then pipe response back to express response
    req.pipe(request(req.query.url)).pipe(res);
});

app.listen(port, ()=>{
    console.log(`Listening on Port ${port}`);
});