# -*- coding: utf-8 -*-
# 稳定
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k + 1):
        for j in lists:
            bucket[j/(radix**(i - 1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists



def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    radix_sort(lists)
    print lists

if __name__ == '__main__':
    main()
