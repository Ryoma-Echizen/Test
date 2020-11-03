import pytest

from test_appium.page.app import App


class TestSearch:
    def test_search01(self):
        self.main = App().main().goto_search().search('alibaba').get_price('BABA')
        assert self.main > 200
    @pytest.mark.parametrize("key,stock_type,price",[
        ('alibaba','BABA',200),
        ('JD','JD',20)
    ])
    def test_search01(self):
        self.main = App().main().goto_search().get_price()
        assert self.main > 200