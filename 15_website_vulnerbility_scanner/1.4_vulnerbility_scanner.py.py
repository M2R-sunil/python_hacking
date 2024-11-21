#!/usr/bin/env python
import scanner

target_url = "http://192.168.112.128/mutillidae/"
vuln_scanner = scanner.Scanner(target_url)
vuln_scanner.crawl(target_url)

