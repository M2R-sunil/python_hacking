#!/usr/bin/env python
import scanner

target_url = "http://192.168.112.128/dvwa/"
links_to_ignore = "http://192.168.112.128/dvwa/logout.php"  # This ignores logout links.
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://192.168.112.128/dvwa/login.php", data=data_dict)
forms = vuln_scanner.extract_forms("http://192.168.112.128/dvwa/vulnerabilities/xss_r/")
print(forms)
response = vuln_scanner.submit_form(forms[0], "testtest", "http://192.168.112.128/dvwa/vulnerabilities/xss_r/")
print(response.content)
