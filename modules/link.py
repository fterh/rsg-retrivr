import re
import tldextract

def link_is_blocked(blocked_links, url):

    # TLDExtract extracts the top-level domain from the
    # registered domain and subdomains of a URL. For example,
    # to get just the 'google' part of 'http://www.google.com'
    # or 'http://google.com.sg'.
    #
    # By default, when the module is first run, it updates
    # its TLD list with a live HTTP request. This updated TLD
    # list is cached indefinitely in /path/to/tldextract/.tld_set
    #
    # This is to set the call to not use cache.
    no_cache_extract = tldextract.TLDExtract(cache_file=False)

    # How to use TLDExtract
    # Usage: no_cache_extract('http://forums.news.cnn.com/')
    # Result: ExtractResult(subdomain='forums.news', domain='cnn', suffix='com')
    extracted = no_cache_extract(url)
    url_domain = extracted.domain + "." + extracted.suffix

    for site in blocked_links:
        # if url matches with blocked domain
        if (re.match(site, url_domain)):
            return True
