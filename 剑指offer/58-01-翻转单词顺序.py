# -*- coding:utf-8 -*-
'''
        翻转单词顺序
============================
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，
标点符号和普通字母一样处理。例如输入字符串"I am a student."，则输出
"student. a am I"。
'''

def reverseWordsInSentence(sentence):
    '''
    思路：以句子"I am a student."为例， 先将整个句子进行翻转，包括单词内
    字母的顺序得到".tneduts a ma I", 接着翻转每个单词内的字母循序，得到
    "students. a am I"。最后通过两次翻转得到题目要求的输出。
    '''
    def reverse(string, begin, end):
        while begin < end:
            string[begin], string[end] = string[end], string[begin]
            begin += 1
            end -= 1

    if not isinstance(sentence, str):
        return

    chars = list(sentence)
    begin, end = 0, len(chars) - 1
    reverse(chars, begin, end)
    begin = end = 0
    while begin < len(chars) - 1:
        if chars[begin] == ' ':
            begin += 1
            end += 1
        elif end == len(chars) or chars[end] == ' ':
            reverse(chars, begin, end - 1)
            begin = end
        else:
            end += 1
    return ''.join(chars)


import unittest

class TestReverseWordsInSentence(unittest.TestCase):
    def test_reverse_words_in_sentence(self):
        self.assertEqual(reverseWordsInSentence(None), None)
        self.assertEqual(reverseWordsInSentence(''), '')
        self.assertEqual(reverseWordsInSentence(' '), ' ')
        self.assertEqual(reverseWordsInSentence('I am a student.'), 'student. a am I')
        self.assertEqual(reverseWordsInSentence('Wonderful'), 'Wonderful')
        self.assertEqual(reverseWordsInSentence('Plato is my dear, but dearer still is truth'),                                        'truth is still dearer but dear, my is Plato')


if __name__ == '__main__':
    unittest.main()
