'''
A 国的手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 K 位数字相同则被定义为靓号。A 国的手机号可以有前导零，比如 000123456 是一个合法的手机号。
小多想花钱将自己的手机号码修改为一个靓号。修改号码中的一个数字需要花费的金额为新数字与旧数字之间的差值。比如将 1 修改为 6 或 6 修改为 1 都需要花 5 块钱。
给出小多现在的手机号码，问将其修改成一个靓号，最少需要多少钱？

输入描述：
第一行包含2个整数 N、K，分别表示手机号码数字个数以及靓号至少有 K 个数字相同。
第二行包含 N 个字符，每个字符都是一个数字('0'-'9')，数字之间没有任何其他空白符。表示小多的手机号码。
数据范围：
2 <= K <= N <= 10000

输出描述：
第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
第二行包含 N 个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。

输入例子:
6 5
787585

输出例子：
4
777577
'''

from collections import Counter

def compute_cost(dic, k, num):
    cost = 0
    if dic[num] >= k:
        return cost
    k -= dic[num]
    for increment in range(1, 10):
        if num + increment < 10:
            if dic[num + increment] >= k:
                cost += increment * k
                return cost
            else:
                k -= dic[num + increment]
                cost += increment * dic[num + increment]
        if num - increment >= 0:
            if dic[num - increment] >= k:
                cost += increment * k
                return cost
            else:
                k -= dic[num - increment]
                cost += increment * dic[num - increment]

def modify(s, dic, k, num):
    if dic[num] >= k:
        return
    k -= dic[num]
    for increment in range(1, 10):
        # 保证修改后的手机号是字典序最小的那个
        if num + increment < 10:
            for i in range(len(s)):
                if k == 0: return
                if s[i] == num + increment:
                    s[i] = num
                    k -= 1
        if num - increment >= 0:
            for i in range(len(s) - 1, -1, -1):
                if k == 0: return
                if s[i] == num - increment:
                    s[i] = num
                    k -= 1

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    s = list(map(int, input().strip()))
    # key为元素，value为在s中出现的次数
    dic = Counter(s)
    for i in range(10):
        if i not in dic:
            dic[i] = 0
    minCost = 2 ** 32
    ans = -1
    for i in range(10):
        cost = compute_cost(dic, k, i)
        if cost < minCost:
            minCost = cost
            ans = i
    modify(s, dic, k, ans)
    print(minCost)
    print(''.join(map(str, s)))