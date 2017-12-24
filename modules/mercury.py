import requests
import json

import modules.link as linkcheck

from bs4 import BeautifulSoup as bs

class Mercury:

    def __init__(self, submission_url, mercury_api_key, blocked_links):
        url = "https://mercury.postlight.com/parser?url=" + submission_url
        headers = {
            "x-api-key": mercury_api_key,
            "Content-Type": "application/json"
        }

        r = requests.get(url, headers=headers)
        j = json.loads(r.text)

        self.title = j["title"]
        self.author = j["author"]
        self.content = j["content"]
        self.date_published = j["date_published"]
        self.lead_image_url = j["lead_image_url"]
        self.dek = j["dek"]
        self.url = j["url"]
        self.domain = j["domain"]
        self.excerpt = j["excerpt"]
        self.word_count = j["word_count"]
        self.direction = j["direction"]
        self.total_pages = j["total_pages"]
        self.rendered_pages = j["rendered_pages"]
        self.next_page_url = j["next_page_url"]

        self.body = self.get_body(blocked_links)

    def get_body(self, blocked_links):
        # cooking the soup
        soup = bs(self.content, "html.parser")
        body = ""

        # content to markdown
        for paragraph in soup.select("p"): # working assumption: <p> tags

            # hyperlinks to markdown
            if paragraph.a:
                gen = (a for a in paragraph.select("a") if a.string is not None)
                for a in gen:
                    # remove link if it is blocked
                    if (linkcheck.link_is_blocked(blocked_links, a.get("href"))):
                        a.string = "[link is removed]"

                    else:
                        a.string = "[" + a.string + "](" + a.get("href") + ")"

            body += "> " + paragraph.get_text() + "\n\n"

        return body
