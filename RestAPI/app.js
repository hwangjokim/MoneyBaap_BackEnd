var express = require('express')
var mongoose = require('mongoose');
var cors = require("cors");
var app = express();
var port = 5921;

var port = app.listen(5921);
app.use(cors());
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
var Natl = mongoose.model('seoulnatl',contactSchema);
var Cau = mongoose.model('cau',contactSchema);
app.get('/contacts', (req, res) => {
    Contact.find({}, function(err, foods) {
        if(err) return res.json(err);
        res.json({food:foods});
    });
});

app.get('/seouls', (req, res) => {
    Natl.find({}, function(err, seoulnatls) {
        if(err) return res.json(err);
        res.json({SeoulNatl:seoulnatls});
    });
});

app.get('/caus', (req, res) => {
    Cau.find({}, function(err, caus) {
        if(err) return res.json(err);
        res.json({cau:caus});
    });
});

app.listen(port, () => {
    console.log('start! express server');
})