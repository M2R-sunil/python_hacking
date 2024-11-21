#!/usr/bin/env python
import scanner

target_url = "http://192.168.112.128/dvwa/"
links_to_ignore = "http://192.168.112.128/dvwa/logout.php" ## this is ignore logout links. 
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
response = vuln_scanner.session.post( "http://192.168.112.128/dvwa/login.php", data=data_dict)


vuln_scanner.crawl()

