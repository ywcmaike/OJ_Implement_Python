# -*- coding: utf-8 -*-

def select_sort(lists):
    count = len(lists)

    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists




def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    select_sort(lists)
    print(lists)

if __name__ == '__main__':
    main()