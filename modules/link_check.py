import json
import re
import tldextract

class LinkCheck:
    # TLDExtract extracts the top-level domain from the
    # registered domain and subdomains of a URL. For example,
    # you want just the 'google' part of 'http://www.google.com'.
    #
    # By default, when the module is first run, it updates
    # its TLD list with a live HTTP request. This updated TLD
    # set is cached indefinitely in /path/to/tldextract/.tld_set
    #
    # This is to set the call to not use cache.
    no_cache_extract = tldextract.TLDExtract(cache_file=False)

    # load set of links that are disallowed
    file = open("links.json", "r")
    links = json.load(file)

    def link_is_disallowed(self, url):
        # How to use TLDExtract
        # Usage: no_cache_extract('http://forums.news.cnn.com/')
        # Result: ExtractResult(subdomain='forums.news', domain='cnn', suffix='com')
        extracted = self.no_cache_extract(url)
        url_domain = extracted.domain + "." + extracted.suffix

        for disallowed_link in self.links["disallowed"]:
            # if url matches with disallowed domain
            if (re.match(disallowed_link, url_domain)): 
                return True