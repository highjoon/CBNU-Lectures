const { Router } = require('express');

const router = Router();

router.get('/', (req, res) => {
    res.render('index', {
        title: 'Express Example',
        username: '홍길동'
    });
});

router.get('/additional', (req, res)=> {
    res.render('additional', {
        title: 'Express Example',
        username: '홍길동'
    });
});

module.exports = router;