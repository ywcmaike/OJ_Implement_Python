# -*- coding: utf-8 -*-

def bubble_sort(lists):
    count = len(lists)

    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists



def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    bubble_sort(lists)
    print(lists)

if __name__ == '__main__':
    main()