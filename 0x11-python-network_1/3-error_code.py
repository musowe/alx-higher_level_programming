#!/usr/bin/python3
"""This python script Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    page = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(page) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))