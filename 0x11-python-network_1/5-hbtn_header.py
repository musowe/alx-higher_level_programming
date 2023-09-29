#!/usr/bin/python3
"""This python script Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    page = requests.get(url)
    print(page.headers.get("X-Request-Id"))
