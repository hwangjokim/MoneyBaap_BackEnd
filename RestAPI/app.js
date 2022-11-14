var express = require('express')
var mongoose = require('mongoose');
var app = express();
var port = 5921;

var port = app.listen(5921);

// var link;
// const fs = require('fs')
// fs.readFile('/RestAPI/mongoPW.txt','utf8', (err, d) => {
//     if (err) {
//         console.errror(err)
//         return
//     }
//     return link = d;
// })
// mongoose.connect(link);
mongoose.connect('');
var db = mongoose.connection;
db.once('open', function(err,a) {
    console.log('DB connected');
});
db.on('error', function(err) {
    console.log('DB ERROR : ', err);
});

var contactSchema = mongoose.Schema( {
    link:{type:String, required:true, unique:true},
    name:{type:String, required:true, unique:true},
    star:{type:String, required:true, unique:false},
    locate:{type:String, required:true, unique:true},
    menus:{type:Array, required:true, unique:true}

});//유후~
var Contact = mongoose.model('food', contactSchema);

app.get('/contacts', (req, res) => {
    Contact.find({}, function(err, foods) {
        if(err) return res.json(err);
        res.json({food:foods});
    });
});

app.listen(port, () => {
    console.log('start! express server');
})