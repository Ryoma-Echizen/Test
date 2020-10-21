from zuoye2.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)
    def test_add_member(self):
        self.main.add_member().add_member()
