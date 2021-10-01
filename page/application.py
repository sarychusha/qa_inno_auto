from page.login_page import LoginPage
from page.personal_data_page import (
    PersonalDataPage,
    PersonalDataPageMore,
    PersonalDataPageOptional,
    PersonalDataPageTag,
)
from page.sign_up_page import SignUp
from page.create_course_page import CreateCoursePage
from page.course_page import CoursePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.personal_data = PersonalDataPage(self)
        self.sign_up = SignUp(self)
        self.personal_data_more = PersonalDataPageMore(self)
        self.personal_data_optional = PersonalDataPageOptional(self)
        self.personal_data_tag = PersonalDataPageTag(self)
        self.course = CoursePage(self)
        self.create_course = CreateCoursePage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_course_page(self):
        self.driver.get(self.url + "/course/index.php")

    def open_create_course_page(self):
        self.driver.get(self.url + "/course/edit.php")
