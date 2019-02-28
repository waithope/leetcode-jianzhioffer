# -*- coding:utf-8 -*-
'''
        替换空格
=======================
实现一个函数，把字符串中的每一个空格替换成"%20"。例如，输入"we are happy."，
则输出"we%20are%20happy."。
'''

def replaceSpace1(s):
    '''
    使用python自带的replace进行替换，由于str类型不可变，该函数会返回一个新的str
    worst-case: O(n*n)
    '''
    if not isinstance(s, str):
        return
    return s.replace(' ', '%20')

def replaceSpace2(s):
    '''
    书中的思路
    时间O(n)
    '''
    if not isinstance(s, str) or len(s) <= 0:
        return

    spaceNum = 0
    for c in s:
        if c == ' ':
            spaceNum += 1

    newStrLen = len(s) + spaceNum * 2
    newStr = [None] * newStrLen
    indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
    while indexOfOriginal >= 0 and indexOfNew >= indexOfOriginal:
        if s[indexOfOriginal] != ' ':
            newStr[indexOfNew] = s[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1
        else:
            newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
    return ''.join(newStr)


import unittest

class TestReplaceSpace(unittest.TestCase):
    def test_replace_space(self):
        self.assertEqual(replaceSpace2(' helloworld'), '%20helloworld')
        self.assertEqual(replaceSpace2('hello world'), 'hello%20world')
        self.assertEqual(replaceSpace2('helloworld '), 'helloworld%20')
        self.assertEqual(replaceSpace2('helloworld'), 'helloworld')
        self.assertEqual(replaceSpace2(' hello    world'), '%20hello%20%20%20%20world')

if __name__ == '__main__':
    unittest.main()