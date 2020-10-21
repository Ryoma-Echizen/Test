from test_selenium.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)
    def test_add_member(self):
        self.main.add_member().add_member('xxx')
        # main.import_users().get_message()
        # assert 'aaa' in self.main.import_users().get_message()

    def test_import_user(self):
        self.main.import_users('/Users/ouyangxiaofang/PycharmProjects/test/test_selenium/通讯录批量导入模板.xlsx')
        # assert "success" in self.main.get_message()

    def test_send_message(self):
        self.main.send_message().send(app="测试开发",group="阳小芳",content="content")
        # assert "" in self.main.get_message()