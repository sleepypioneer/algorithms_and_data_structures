import requests
import re


class WebCrawler:

    def __init__(self):
        # we want to avoid revisiting the same website over and over
        self.discovered_websites = []

    def crawl(self, start_url):
        """
        BFS implementation
        """

        queue = [start_url]

        self.discovered_websites.append(start_url)

        while queue:

            actual_url = queue.pop(0)
            print(actual_url)

            raw_html = self.read_raw_html(actual_url)

            for link in self.get_links_from_html(raw_html):
                if link not in self.discovered_websites:
                    self.discovered_websites.append(link)
                    queue.append(link)

    @staticmethod
    def read_raw_html(url):
        """
        return parsed HTML content
        """
        raw_html = ''

        try:
            raw_html = requests.get(url).text
        except Exception as e:
            print(f'couldn\'t reach website. {e}')  # we rint the exception when a url cannot be requested
            # we are not currently doing anything here and pass on the empty string

        return raw_html

    @staticmethod
    def get_links_from_html(raw_html):
        """
        return links found inside HTML
        """
        urls = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', raw_html)

        print(f'{len(urls)} urls found on in raw html')
        return urls


if __name__ == '__main__':
    crawler = WebCrawler()
    crawler.crawl('https://www.cnn.com')
