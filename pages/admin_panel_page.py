from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPanelPage:
    add_project_button = (By.XPATH, "//a[contains(text(),'Dodaj projekt')]")
    search_field = (By.ID, "search")
    search_button = (By.CLASS_NAME, "icon_search")
    projects_list = (By.CSS_SELECTOR, "table")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def click_add_project_button(self):
        from pages.projects_page import ProjectPage
        self.browser.find_element(*self.add_project_button).click()
        return ProjectPage(self.browser)

    def search_project(self, project_name):
        self.browser.find_element(*self.search_field).send_keys(project_name)
        self.browser.find_element(*self.search_button).click()

    def verify_project_exist(self, project_name):
        project_elements = self.wait.until(EC.presence_of_all_elements_located(self.projects_list))
        for element in project_elements:
            if project_name in element.text:
                return True
        return False
