#!/usr/bin/env python
import requests
import re
import  urlparse  ## this library print the full url of the website.

target_url = "https://ruj-bsdu.in"
target_links = []

def extract_link_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)
def crawl(url):
    href_links = extract_link_from(url)
    for link in href_links:   # this loop print links line by line.
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:   ## this is print only targt website urls.
            target_links.append(link)
            print(link)
            crawl(link)
crawl(target_url)


