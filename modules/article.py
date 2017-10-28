import requests
from bs4 import BeautifulSoup as bs

class article:

    def __init__(self, url, site):
        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 \
        Safari/537.36"}

        r = requests.get(url, header=header)

        if (r.status_code != 200): # if GET request fails
            print("Error: " + str(r.status_code))

        else: # if GET request is successful
            self.soup = bs(r.text, "html.parser")
            self.title = self.get_title(site)
            self.body = self.get_body(site)

    def get_title(self, site):
        return self.soup.select_one(site["title_selector"]).string

    def get_body(self, site):
        body = ""
        for paragraph in self.soup.select(site["body_selector"]):
            body += "> " + paragraph.get_text() + "\n\n"
        return body
