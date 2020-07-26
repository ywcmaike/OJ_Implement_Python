# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/16 上午1:37

from typing import List
# https://blog.csdn.net/single_wolf_wolf/article/details/52854015
# if __name__ == "__main__":
# 	pass


# C++ STL 的实现：
#
# 1.vector      底层数据结构为数组 ，支持快速随机访问
#
# 2.list            底层数据结构为双向链表，支持快速增删
#
# 3.deque       底层数据结构为一个中央控制器和多个缓冲区，详细见STL源码剖析P146，支持首尾（中间不能）快速增删，也支持随机访问
# deque是一个双端队列(double-ended queue)，也是在堆中保存内容的.它的保存形式如下:
# [堆1] --> [堆2] -->[堆3] --> ...
# 每个堆保存好几个元素,然后堆和堆之间有指针指向,看起来像是list和vector的结合品.
#
# 4.stack        底层一般用list或deque实现，封闭头部即可，不用vector的原因应该是容量大小有限制，扩容耗时
#
# 5.queue     底层一般用list或deque实现，封闭头部即可，不用vector的原因应该是容量大小有限制，扩容耗时
#
# （stack和queue其实是适配器,而不叫容器，因为是对容器的再封装）
#
# 6.priority_queue     的底层数据结构一般为vector为底层容器，堆heap为处理规则来管理底层容器实现
#
# 7.set                   底层数据结构为红黑树，有序，不重复
#
# 8.multiset         底层数据结构为红黑树，有序，可重复
#
# 9.map                底层数据结构为红黑树，有序，不重复
#
# 10.multimap    底层数据结构为红黑树，有序，可重复
#
# 11.hash_set     底层数据结构为hash表，无序，不重复
#
# 12.hash_multiset 底层数据结构为hash表，无序，可重复
#
# 13.hash_map    底层数据结构为hash表，无序，不重复
#
# 14.hash_multimap 底层数据结构为hash表，无序，可重复
# http://www.cnblogs.com/hustlijian/p/3611424.html
# ------------------------------------------------------------------------------------------------------------------------------------------
# stl容器区别: vector list deque set map-底层实现
# stl容器区别: vector list deque set map （转）
#
# 在STL中基本容器有: vector、list、deque、set、map
#
# set 和map都是无序的保存元素,只能通过它提供的接口对里面的元素进行访问
#
# set:集合, 用来判断某一个元素是不是在一个组里面,使用的比较少
# map:映射,相当于字典,把一个值映射成另一个值,如果想创建字典的话使用它好了
# 底层采用的是树型结构,多数使用平衡二叉树实现,查找某一值是常数时间,遍历起来效果也不错, 只是每次插入值的时候,会重新构成底层的平衡二叉树,效率有一定影响.
#
# vector、list、deque是有序容器
# 1.vector
# vector就是动态数组.它也是在堆中分配内存,元素连续存放,有保留内存,如果减少大小后，内存也不会释放.如果新值>当前大小时才会再分配内存.
#
# 它拥有一段连续的内存空间，并且起始地址不变，因此它能非常好的支持随即存取，即[]操作符，但由于它的内存空间是连续的，所以在中间进行插入和删除会造成内存块的拷贝，另外，当该数组后的内存空间不够时，需要重新申请一块足够大的内存并进行内存的拷贝。这些都大大影响了vector的效率。
#
# 对最后元素操作最快(在后面添加删除最快 ), 此时一般不需要移动内存,只有保留内存不够时才需要
#
#
#
# 对中间和开始处进行添加删除元素操作需要移动内存,如果你的元素是结构或是类,那么移动的同时还会进行构造和析构操作，所以性能不高 （最好将结构或类的指针放入vector中，而不是结构或类本身，这样可以避免移动时的构造与析构)。
# 访问方面,对任何元素的访问都是O(1),也就是是常数的,所以vector常用来保存需要经常进行随机访问的内容,并且不需要经常对中间元素进行添加删除操作.
#
# 相比较可以看到vector的属性与string差不多,同样可以使用capacity看当前保留的内存,使用swap来减少它使用的内存.
#
# capacity()返回vector所能容纳的元素数量(在不重新分配内存的情况下）      测试push_back  1000个数据  capacity返回16384
#
#
# 总结
# 需要经常随机访问请用vector
#
# 2.list
# list就是双向链表,元素也是在堆中存放,每个元素都是放在一块内存中,它的内存空间可以是不连续的，通过指针来进行数据的访问，这个特点使得它的随机存取变的非常没有效率，因此它没有提供[]操作符的重载。但由于链表的特点，它可以以很好的效率支持任意地方的删除和插入。
#
# list没有空间预留习惯,所以每分配一个元素都会从内存中分配,每删除一个元素都会释放它占用的内存.
#
# list在哪里添加删除元素性能都很高,不需要移动内存,当然也不需要对每个元素都进行构造与析构了,所以常用来做随机操作容器.
# 但是访问list里面的元素时就开始和最后访问最快
# 访问其它元素都是O(n) ,所以如果需要经常随机访问的话,还是使用其它的好
#
# 总结
# 如果你喜欢经常添加删除大对象的话,那么请使用list
# 要保存的对象不大,构造与析构操作不复杂,那么可以使用vector代替
# list<指针>完全是性能最低的做法,这种情况下还是使用vector<指针>好,因为指针没有构造与析构,也不占用很大内存
#
# 3.deque
# deque是一个双端队列(double-ended queue)，也是在堆中保存内容的.它的保存形式如下:
# [堆1]
# ...
# [堆2]
# ...
# [堆3]
# 每个堆保存好几个元素,然后堆和堆之间有指针指向,看起来像是list和vector的结合品.
#
# 它支持[]操作符，也就是支持随即存取，可以让你在前面快速地添加删除元素,或是在后面快速地添加删除元素,然后还可以有比较高的随机访问速度,和vector的效率相差无几，它支持在两端的操作：push_back,push_front,pop_back,pop_front等，并且在两端操作上与list的效率也差不多。
# 在标准库中vector和deque提供几乎相同的接口,在结构上它们的区别主要在于这两种容器在组织内存上不一样,deque是按页或块来分配存储器的,每页包含固定数目的元素.相反vector分配一段连续的内存,vector只是在序列的尾段插入元素时才有效率,而deque的分页组织方式即使在容器的前端也可以提供常数时间的insert和erase操作,而且在体积增长方面也比vector更具有效率
#
# 总结：
# vector是可以快速地在最后添加删除元素,并可以快速地访问任意元素
# list是可以快速地在所有地方添加删除元素,但是只能快速地访问最开始与最后的元素
# deque在开始和最后添加元素都一样快,并提供了随机访问方法,像vector一样使用[]访问任意元素,但是随机访问速度比不上vector快,因为它要内部处理堆跳转
# deque也有保留空间.另外,由于deque不要求连续空间,所以可以保存的元素比vector更大,这点也要注意一下.还有就是在前面和后面添加元素时都不需要移动其它块的元素,所以性能也很高。
#
# 因此在实际使用时，如何选择这三个容器中哪一个，应根据你的需要而定，一般应遵循下面
# 的原则：
# 1、如果你需要高效的随即存取，而不在乎插入和删除的效率，使用vector
# 2、如果你需要大量的插入和删除，而不关心随即存取，则应使用list
# 3、如果你需要随即存取，而且关心两端数据的插入和删除，则应使用deque