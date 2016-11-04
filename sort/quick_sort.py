# -*- coding: utf-8 -*-
def quick_sort(lists, left, right):

    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:

        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key

    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)

    return lists



def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    n = len(lists)
    quick_sort(lists, 0, n - 1)
    print lists

if __name__ == '__main__':
    main()