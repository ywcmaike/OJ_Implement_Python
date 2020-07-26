# -*- coding: utf-8 -*-

# 大顶堆

# def adjust_heap(lists, i, size):
#     lchild = 2 * i + 1
#     rchild = 2 * i + 2
#     max = i
#     if i < size / 2:
#         if lchild < size and lists[lchild] > lists[max]:
#             max = lchild
#         if rchild < size and lists[rchild] > lists[max]:
#             max = rchild
#         if max != i:
#             lists[max], lists[i] = lists[i], lists[max]
#             adjust_heap(lists, max, size)

# 小顶堆
def  adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    min = i
    if i < size // 2 :
        if lchild < size and lists[lchild] < lists[min]:
            min = lchild
        if rchild < size and lists[rchild] < lists[min]:
            min = rchild
        if min != i:
            lists[min], lists[i] = lists[i], lists[min]
            adjust_heap(lists, min, size)

def build_heap(lists, size):
    for i in range(0, (size//2))[:: -1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[:: -1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


def main():
    lists = [3, 5, 4, 2, 1, 6, 8, 7, 9, 0, 11, 14, 12]
    heap_sort(lists)
    print(lists)

if __name__ == '__main__':
    main()
