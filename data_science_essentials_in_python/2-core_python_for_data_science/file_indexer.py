#!/usr/bin/env python

# program must index all words in all files in a given dir
# the product is a dictionary mapping a unique word to a list of files the
# word appears in
# unique words should be matched case insensitive
# dictionary should be pickled for later use

# TODO: enhancement: provide a filter to filter out markup and get actual
# content

import ipdb
from os import listdir
from os.path import isfile, join
import pickle
import re
import sys

def main():
    dir = sys.argv[1]
    assert dir is not None
    # files = [f for f in listdir(dir) if isfile(join(dir, f))]
    files = get_files_in_dir(dir)
    print('Files:\n%s' % files)
    index = {}
    for file_name in files:
        with open(join(dir, file_name)) as f:
            contents = f.read()
        file_words = re.findall('\w+', contents)
        for word in file_words:
            lword = word.lower()
            if lword not in index:
                index[lword] = []
            if file_name not in index[lword]:
                index[lword].append(file_name)

    # now pickle the index
    with open('index.pickle', 'wb') as oFile:
        pickle.dump(index, oFile)

    # enhancement dump the dict as text
    with open('index.txt', 'w') as oFile:
        for key, value in sorted(index.items()):
            oFile.write('%s: %s\n' % (key, value))




def get_files_in_dir(dir_path):
    items = listdir(dir_path)
    # ipdb.set_trace()
    files = []
    for item in items:
        if isfile(join(dir_path, item)):
            files.append(item)
    return files

if __name__ == '__main__':
    main()
