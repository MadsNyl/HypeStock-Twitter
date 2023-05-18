from settings import CHROME_OPTIONS, WAIT_TIME
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from app.twitterLogin import TwitterLogin
from app.twitterSearch import TwitterSearch


class TwitterScraper():
    _driver: Chrome
    _login: TwitterLogin
    _wait: WebDriverWait

    def __init__(self) -> None:
        self._set_driver()
        self._wait = WebDriverWait(self._driver, WAIT_TIME)
        self._login = TwitterLogin(self._driver)

    def _set_driver(self) -> None:
        self._driver = Chrome(
            ChromeDriverManager().install(),
            options=CHROME_OPTIONS
        )

    def startup(self) -> None:
        self._login.login()
        self.__close_account_security_popup()

    def search(self, **kwargs) -> None:
        search_engine = TwitterSearch(
            query=kwargs.get("query"),
            field=kwargs.get("field") if kwargs.get("field") else None
        )
        search_engine.search(self._driver)
    
    def scrape_tweets(self) -> None:
        tweets = self._wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article")))
        
        for tweet in tweets:
            print("new tweet \n")
            self.__scrape_tweet(tweet)

    def __scrape_tweet(self, tweet: WebElement) -> None:
        user_wrapper_class = "css-1dbjc4n r-1wbh5a2 r-dnmrzs"
        user_class = "css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l"
        user = tweet.find_elements(By.XPATH, f".//div[@class='{user_wrapper_class}']/a[@class='{user_class}']")
        
        twitter_name = user[0].text
        username = user[1].text

        body_class = "css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"
        body = tweet.find_element(By.XPATH, f".//div[@class='{body_class}']")

        text = body.text

        print(twitter_name)
        print(username)
        print(text)

    def __close_account_security_popup(self) -> None:
        try:
            close_button_class_name = "r-4qtqp9 r-yyyyoo r-z80fyv r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-19wmn03"
            close_button = self._wait.until(EC.presence_of_element_located((By.XPATH, f"//svg[@class='{close_button_class_name}']")))
            close_button.click()
        except TimeoutException:
            print("There is no popup for account security.")
