#!/usr/bin/python3

from subprocess import check_output
from glob import glob
from os.path import dirname, isdir, exists
from shutil import copyfile
import os

def main():
    bins = glob('./bin/*')
    for binary in bins:
        ldd = check_output(['ldd', binary]).split(b'\n')
        ldd = ldd[1:-1]
        ldd = list(map(lambda x:x.decode().strip(), ldd))
        print("==== {} ====".format(binary))
        for l in ldd:
            print(l.split()[-2])
            libPath = l.split()[-2]
            if not exists('.'+libPath):
                dirPath = dirname(libPath)
                os.system("mkdir -p .{}".format(dirPath))
                copyfile(libPath, '.'+libPath)
        print()

if __name__ == "__main__":
    main()

