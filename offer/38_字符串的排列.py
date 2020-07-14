# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 上午1:19

# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#  
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#  
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# idea
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
# 递归解析：
# 终止条件： 当 x = len(c) - 1x=len(c)−1 时，代表所有位已固定（最后一位只有 11 种情况），则将当前组合 c 转化为字符串并加入 res，并返回；
# 递推参数： 当前固定位 xx ；
# 递推工作： 初始化一个 Set ，用于排除重复的字符；将第 xx 位字符与 i \in [x, len(c)]i∈[x,len(c)] 字符分别交换，并进入下层递归；
# 剪枝： 若 c[i]c[i] 在 Set​ 中，代表其是重复字符，因此“剪枝”；
# 将 c[i]c[i] 加入 Set​ ，以便之后遇到重复字符时剪枝；
# 固定字符： 将字符 c[i]c[i] 和 c[x]c[x] 交换，即固定 c[i]c[i] 为当前位字符；
# 开启下层递归： 调用 dfs(x + 1)dfs(x+1) ，即开始固定第 x + 1x+1 个字符；
# 还原交换： 将字符 c[i]c[i] 和 c[x]c[x] 交换（还原之前的交换）；
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res


if __name__ == "__main__":
	s = "abc"
	print(Solution().permutation(s))
	pass