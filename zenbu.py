#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import sys
import itertools

def main():
    kind = '- kind: Sample\n  properties:'
    name = '\n  - name: '
    args = sys.argv[1:]

    for i in range(2, len(args)):
        for v in list(itertools.combinations(args, i)):
            print(kind + name + name.join(v) + '\n')

    if len(args) > 1:
        print(kind + name + name.join(args))

    return 0

if __name__ == "__main__":
    sys.exit(main())
