from app import TwitterScraper


def main() -> None:
    scraper = TwitterScraper()
    scraper.startup()
    scraper.search(
        query="stocks"
    )
    scraper.scrape_tweets()


if __name__ == "__main__":
    main()
