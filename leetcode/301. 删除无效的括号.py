# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/16 上午1:21

# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
#
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
#
# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 示例 3:
#
# 输入: ")("
# 输出: [""]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
if __name__ == "__main__":
	pass