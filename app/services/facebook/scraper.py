import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.schemas.group import ApiGroupCreateRequest, ApiGroupResponse


class FacebookScraper:
    FACEBOOK_URL = "https://www.facebook.com/"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, email: str, password: str):
        self.driver.get(self.FACEBOOK_URL)
        email_element = self.driver.find_element(By.ID, "email")
        email_element.send_keys(email)

        password_element = self.driver.find_element(By.ID, "pass")
        password_element.send_keys(password)

        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

        time.sleep(5)

    def get_groups(self) -> list[ApiGroupCreateRequest]:
        self.driver.get(self.FACEBOOK_URL + "groups/joins")
        time.sleep(5)

        groups_wrapper = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[3]",
        )

        group_elements = groups_wrapper.find_elements(
            By.XPATH, ".//div/div/div/div/div/div/span/span/div/a"
        )

        groups: list[ApiGroupCreateRequest] = []
        for element in group_elements:
            group_name = element.text
            group_url = element.get_attribute("href")
            group_id = group_url.split("/")[-2]

            groups.append(
                ApiGroupCreateRequest(name=group_name, url=group_url, group_id=group_id)
            )

        return groups

    def get_posts(self, group_url):
        self.driver.get(group_url)
        time.sleep(5)

        posts = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-ad-preview='message']"
        )
        post_contents = [post.text for post in posts]

        return post_contents

    def close(self):
        self.driver.quit()
