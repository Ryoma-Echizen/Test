from selenium_3_po.page.add_member import AddMember
from selenium_3_po.page.base_page import BasePage


class MainPage(BasePage):
    def add_member(self):
        #click 添加成员
        return AddMember(self.driver)

    def import_member_book(self):
        pass

    def join_member(self):
        pass
