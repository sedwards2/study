#!/usr/bin/env python

# show the ten most popular words from a given web page
# definition of a word is the regex r'\w+'

from collections import Counter
import re
import requests
import sys
import urllib.request

def main():
    assert sys.argv[1] is not None
    url = sys.argv[1]
    # One could use either urllib or requests
    # the book shows how to use urllib here, but requests is better
    # (ie more concise)
    # r = requests.get(url)
    with urllib.request.urlopen(url) as doc:
        html = doc.read().decode().lower()
    word_list = re.findall('\w+', html)
    counter = Counter(word_list)
    most_common = counter.most_common(10)
    for word in most_common:
        print(word)

if __name__ == '__main__':
    main()
