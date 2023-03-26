from API.API import *


class TestApi:
    def test_banana_status_code(self):
        url = 'https://fruityvice.com/api/fruit/banana'
        res = send_http_request(url)
        assert check_status_code(res.status_code) == True

    def test_Mazda_status_code(self):
        url = 'https://fruityvice.com/api/fruit/Mazda'
        res = send_http_request(url)
        assert check_status_code(res.status_code) == True

