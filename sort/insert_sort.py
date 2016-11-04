# -*- coding: utf-8 -*-
# 时间复杂度：O(n^2)  稳定
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def main():
    lists = [3, 5, 4, 2, 1, 6]
    insert_sort(lists)
    print lists

if __name__ == '__main__':
    main()