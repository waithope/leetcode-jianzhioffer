# -*- coding:utf-8 -*-
'''
    字符串的排列
===================
输入一个字符串，打印出该字符串中字符的所有排列。例如，输入字符串abc，则打印出
由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
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
