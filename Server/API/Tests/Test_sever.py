import json
import allure

import requests
from Server.API.Constants.constants import ApiConstants


class TestTradoStore(ApiConstants):

    @allure.description("Check Api for phones categories")
    def test_api_for_contact_us(self):
        url = self.url
        data = self.valid_data
        res = requests.post(url, json=data)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

