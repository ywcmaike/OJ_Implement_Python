# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/16 上午1:26

from typing import List

# https://blog.csdn.net/qq_26440803/article/details/83795122

#
#
# if __name__ == "__main__":
# 	if
# 	pass

# LRU的设计原理就是，当数据在最近一段时间经常被访问，那么它在以后也会经常被访问。这就意味着，如果经常访问的数据，我们需要然其能够快速命中，而不常访问的数据，我们在容量超出限制内，要将其淘汰。
# 当我们的数据按照如下顺序进行访问时，LRU的工作原理如下 每次访问的数据都会放在栈顶，当访问的数据不在内存中，且栈内数据存储满了，我们就要选择移除栈底的元素，因为在栈底部的数据访问的频率是比较低的。所以要将其淘汰

# 差异对比：
#
# 数组 查询比较快，但是对于增删来说是一个不是一个好的选择
# 链表 查询比较慢，但是对于增删来说十分方便O(1)时间复杂度内搞定
# 有没有办法既能够让其搜索快，又能够快速进行增删操作。
# 我们可以选择链表+hash表，hash表的搜索可以达到0(1)时间复杂度，这样就完美的解决我们搜索时间慢的问题
# 链表，Node一个双向链表的实现，Node中存放的是数结构
# class Node<K,V>{
# 	private K key;
# 	private V value;
# 	private Node<K,V> prev;
# 	private Node<K,V> next;
# }