#!/usr/bin/python3
"""Catches HTTP errors"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        tmp = ""
    else:
        tmp = sys.argv[1]

    payload = {'q': tmp}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        jsn = r.json()
        if len(r) == 0:
            print("No result")
    except:
        print("Not a valid JSON")
