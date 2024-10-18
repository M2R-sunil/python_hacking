#!/usr/bin/env python

import requests
try:
    url = "mail.google.com"
    get_response = requests.get("http://" + url)
    print(get_response)

except requests.exceptions.ConnectionError:
    pass


