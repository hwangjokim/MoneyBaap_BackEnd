var express = require('express')
var mongoose = require('mongoose');
var app = express();
var port = 5921;

var port = app.listen(5921);

mongoose.connect('');
var db = mongoose.connection;
db.once('open', function() {
    console.log('DB connected');
});
db.on('error', function(err) {
    console.log('DB ERROR : ', err);
});

var contactSchema = mongoose.Schema( {
    name:{type:String, required:true, unique:true},
});
var Contact = mongoose.model('contact', contactSchema);

app.get('/contacts', (req, res) => {
    //res.json(contacts:contacts);
})

app.listen(port, () => {
    console.log('start! express server');
})