from test_selenium.page.management import Management


class TestManegement:
    def setup(self):
        self.man = Management(reuse=True)
    def test_addpic(self):
        self.man.library().add_pic('/Users/ouyangxiaofang/PycharmProjects/test/test_selenium/茶饮系列.png')

