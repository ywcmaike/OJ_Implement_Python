# -*- coding: utf-8 -*-
# 不稳定


def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step

    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group;
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k  + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists




def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    shell_sort(lists)
    print lists

if __name__ == '__main__':
    main()