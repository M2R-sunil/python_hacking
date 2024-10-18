#!/usr/bin/env python

import requests
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.112.128/mutillidae/"
with open("/root/Downloads/files_dirs.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + word
        response = request(test_url)
        if response:
            print("[+] Discoverd directories ----> " + test_url)





