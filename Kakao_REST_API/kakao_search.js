const axios = require('axios');

axios({
        method: 'get',
        url: 'https://dapi.kakao.com/v2/search/web',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'KakaoAK key'
        },
        params: {
            query: '카카오'
        }
    })
    .then(response => {
        console.log(response.data)
    })
    .catch(error => {
        console.log(error);
    });