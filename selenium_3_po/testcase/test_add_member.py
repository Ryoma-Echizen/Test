from selenium_3_po.page.main_page import MainPage


class TestMember:
    def test_member(self):
        mainPage = MainPage()
        mainPage.add_member().add_member2()
