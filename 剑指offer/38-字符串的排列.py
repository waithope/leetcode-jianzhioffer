# -*- coding:utf-8 -*-
'''
    字符串的排列
===================
输入一个字符串，打印出该字符串中字符的所有排列。例如，输入字符串abc，则打印出
由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

举一反三：
1) 输入一个含有8个数字的数组，判断有没有可能把这8个数字分别放到正方体的8个顶点上，
使得正方体三组相对的面上的4个顶点的和都相等。
这道题本质是全排列，对每一种排列计算a1+a2+a3+a4=a5+a6+a7+a8, a1+a3+a5+a7=
a2+a4+a6+a8, a1+a2+a5+a6=a3+a4+a7+a8

2) 在8x8的国际象棋上摆放8个皇后，使得任意两个皇后不得处于同一行、同一列或者同一条
对角线上。请问总共有多少种摆法？
我们可以定义一个长度为8的数组colIdx，数组中的第i个元素表示皇后在第i行的列号，接下来
我们对数组中的元素进行全排列，并对每一个排列进行判断是否在同一条对角线上(因为数组的
定义保证了不同行不同列)。判断条件：i-j = colIdx[i] - colIdx[j], j-i=colIdx[j]-
colIdx[i]
'''

def permutation(s):
    '''
    解法一：利用深度优先遍历（DFS）回溯的思想对字符串内的所有字符进行全排列。
    例如，字符串"abc"，首先固定a，对剩余部分"bc"进行全排列；接着交换a,b，
    字符串'bac'，固定b，对剩余部分'ac'进行全排列；接着交换a,c，字符串cba，
    固定c，对剩余部分'ba'进行全排列。深度优先遍历的思想就是一条路走到黑，当
    这条路无路可走的时候，就回溯到上一个位置继续走。
    '''
    def permutation(chars, idx):
        if (not isinstance(chars, list)
            or not isinstance(idx, int)
            or idx > len(chars)):
            return

        if idx == len(chars):
            print(''.join(chars))

        for i in range(idx, len(chars)):
            chars[i], chars[idx] = chars[idx], chars[i]
            permutation(chars, idx + 1)
            chars[i], chars[idx] = chars[idx], chars[i]

    if not isinstance(s, str) or len(s) <= 0:
        return
    permutation(list(s), 0)


if __name__ == '__main__':
    print('Test1: ')
    permutation('')
    print('Test2: ')
    permutation('a')
    print('Test3: ')
    permutation('ab')
    print('Test4: ')
    permutation('abc')
