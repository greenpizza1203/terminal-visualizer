const express = require('express')
const path = require("path");
const app = express()
const port = 8080
app.get('/playground', (req, res) => {
    res.sendFile(path.join(__dirname, 'playground/index.html'))
})
app.get('/undefined', (req, res) => {
    res.send('3')
})
app.get('/api/*', (req, res) => {

    let path1 = path.join(__dirname, '/api/' + req.params[0] + '.json');
    res.sendFile(path1)
})
app.use(express.static('.'))

app.listen(port, () => {
    console.log(`listening on port ${port}`)
})