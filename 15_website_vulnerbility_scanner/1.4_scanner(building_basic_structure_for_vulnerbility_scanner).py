#!/usr/bin/env python
import requests
import re
import urlparse

class Scanner:
    def __init__(self, url):  # Added 'self' as the first parameter
        self.target_url = url
        self.target_links = []  # Fixed the variable name from 'targets_links' to 'target_links'
        
    def extract_links_from(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url):
        href_links = self.extract_links_from(url)  # Fixed the method name here
        for link in href_links:  # this loop print links line by line.
            link = urlparse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            if self.target_url in link and link not in self.target_links:  # Fixed the variable name here
                self.target_links.append(link)
                print(link)
                self.crawl(link)