const express = require('express');
const path = require('path');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Route to render form
app.get('/', (req, res) => {
    const error = req.query.error;
    res.render('form', { error });
});

// Route to handle success page
app.get('/success', (req, res) => {
    res.render('success');
});

app.listen(3000, () => {
    console.log("Frontend running on http://localhost:3000");
});
