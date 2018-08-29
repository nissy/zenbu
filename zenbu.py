#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import sys
import itertools

def main():
    args = sys.argv[1:]

    for i in range(1, len(args)):
        for v in list(itertools.combinations(args, i)):
            print v

    return 0

if __name__ == "__main__":
    sys.exit(main())
