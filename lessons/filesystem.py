import sys
import io
from os import listdir
from os.path import isfile, isdir
import os
import re

# file = open('./.gitignore')
# for line in file:
#     print(line)

documents_dir = '../../Documents'
cwd = listdir(documents_dir)

for entry in cwd:
    path = f"{documents_dir}/{entry}"

    if isfile(path):
        print(f"{path} is a file")
