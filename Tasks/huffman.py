#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Алгоритм Хаффмана
"""

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, z):
        self.left.walk(code, z + "0")
        self.right.walk(code, z + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, z):
        code[self.char] = z or "0"


def huffman(s):
    k = []
    for ch, freq in Counter(s).items():
        k.append((freq, len(k), Leaf(ch)))
    heapq.heapify(k)
    count = len(k)
    while len(k) > 1:
        freq1, count1, left = heapq.heappop(k)
        freq2, count2, right = heapq.heappop(k)
        heapq.heappush(k, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if k:
        [(freq, count, root)] = k
        root.walk(code, "")
    return code


def main():
    s = input("Введите строку: ")
    code = huffman(s)
    encoded = "".join(code[ch] for ch in s)
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print("Сжатая строка:", encoded)


if __name__ == "__main__":
    main()
