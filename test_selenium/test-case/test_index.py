from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        #首页-立即注册
        self.index.goto_register().register("欧阳国际")

    def test_login(self):
        # 首页-企业登录-立即注册
        register_page = self.index.gotp_login().goto_registry().register('欧阳伐木累')
        assert "组成" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()