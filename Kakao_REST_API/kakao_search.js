const axios = require('axios');

const METHOD = 'get';
const URL = 'https://dapi.kakao.com/v2/search/web';
const HEADERS = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'KakaoAK key'
}
const QUERY = ['카카오','kakao'];

const connectSearch = QUERY => {
    axios({
            method: METHOD,
            url: URL,
            headers: HEADERS,
            params: {
                query: QUERY
            }
        })
        .then(response => {
            console.log(response.data)
        })
        .catch(error => {
            console.log(error);
        });
};

for (let i = 0; i < QUERY.length; i++) {
    connectSearch(QUERY[i]);
}