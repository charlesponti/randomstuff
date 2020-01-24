import sys
import io
from os import listdir
from os.path import isfile, isdir
import os
import re

cwd = listdir(".")

for entry in cwd:
    path = f"./{entry}"

    if isfile(path):
        print(f"{path} is a file")
