#!/usr/bin/env python
import requests
import re
import urlparse  ## this library print the full url of the website.

target_url = "https://www.manipal.edu"

def extract_link_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_link_from(target_url)
for link in href_links:   # this loop print links line by line.
    link = urlparse.urljoin(target_url, link)
    if target_url in link:   ## this is print only targt website urls.
         print(link)



