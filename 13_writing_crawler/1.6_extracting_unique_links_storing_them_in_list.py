#!/usr/bin/env python
import requests
import re
import urlparse  ## this library print the full url of the website.

target_url = "https://zsecurity.org/product/alfa-awus036ach-2-4-5-ghz-usb-wireless-adapter"
target_links = []

def extract_link_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_link_from(target_url)
for link in href_links:   # this loop print links line by line.
    link = urlparse.urljoin(target_url, link)
    if "#" in link:
        link = link.split("#")[0]
    if target_url in link and link not in target_links:   ## this is print only targt website urls.
        target_links.append(link)
        print(link)



