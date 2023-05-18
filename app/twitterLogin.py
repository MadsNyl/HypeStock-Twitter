from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
from settings import (
    TWITTER_USERNAME,
    TWITTER_NAME,
    TWITTER_PASSWORD,
    WAIT_TIME
)


class TwitterLogin():
    _LOGIN_URL: str = "https://twitter.com/i/flow/login"
    _driver: Chrome
    _wait: WebDriverWait

    def __init__(self, driver: Chrome) -> None:
        self._driver = driver
        self._wait = WebDriverWait(self._driver, WAIT_TIME)
        self._driver.get(self._LOGIN_URL)

    def login(self) -> None:
        input_class = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"
        self.__fill_input(f"//input[@class='{input_class}']", TWITTER_USERNAME)
        self.__too_many_logins(input_class)
        self.__fill_input(f"//input[@class='{input_class}']", TWITTER_PASSWORD)

    def __fill_input(self, search: str, input_text: str) -> None:
        input = self._wait.until(EC.presence_of_element_located((By.XPATH, search)))
        input.send_keys(input_text)
        input.send_keys(Keys.ENTER)

    def __too_many_logins(self, class_name: str) -> bool:
        try:
            # class_name = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"
            self.__fill_input(f"//input[@class='{class_name}']", TWITTER_NAME)
        except NoSuchWindowException:
            print("There is no need for username confirmation.")