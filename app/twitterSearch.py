from selenium.webdriver import Chrome


class TwitterSearch():
    _BASE_URL: str = "https://twitter.com/search"
    _query: str
    _field: str

    def __init__(self, query: str, field: str) -> None:
        self._query = query
        self._field = field

    def search(self, driver: Chrome) -> None:
        search_url = self._BASE_URL + "?q=" + self._query
        if self._field:
            search_url += f"&f={self._field}"
        driver.get(search_url)
