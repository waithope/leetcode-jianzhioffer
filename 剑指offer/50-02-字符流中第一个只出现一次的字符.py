# -*- coding:utf-8 -*-
'''
    字符流中第一个只出现一次的字符
===================================
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出
前两个字符"go"时，第一个只出现一次的字符是'g'。当从该字符流中读出前六个字符
"google"时，第一个只出现一次的字符是'l'。
'''

def fisrtNotReaptingCharFromStream():
    char2index = {}
    index = 0

    while True:
        ch = input()
        if not isinstance(ch, str) or ch == '':
            break
        if ch not in char2index:
            char2index[ch] = index
        else:
            char2index[ch] = -1
        index += 1

        res = index
        ch = ''
        for c, ind in char2index.items():
            if char2index[c] != -1:
                if ind < res:
                    res = ind
                    ch = c

        if ch == '':
            print(None)
        else:
            print(ch)



if __name__ == '__main__':
    print(fisrtNotReaptingCharFromStream())