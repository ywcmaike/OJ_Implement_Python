# -*- coding: utf-8 -*-

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    # print result
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)



def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 8,7, 9, 0, 11, 14, 12]
    print merge_sort(lists)

if __name__ == '__main__':
    main()
