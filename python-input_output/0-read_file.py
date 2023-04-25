#!/usr/bin/python3
""" Read a file """


def read_file(filename=""):
    """ read a file """
    with open(filename, encoding='utf-8') as f:
        fline = f.read()
        print(fline, end="")
