# -*- coding:utf-8 -*-
'''
    把IP地址保存到32位Int变量中
================================
ip: 111.112.113.114.
ip --> int: 1869640050
int --> ip: 111.112.113.114.
'''

def ipToInt(s):
    '''
    思路：将32位int型变量分成四个区间，每一个区间存储IP地址中的某一段，
    具体计算方法，IP地址'111.112.113.114'，以最高位的区间2^24~2^32举例，
    temp = 111 * 2 **(8 * 3)
    '''
    if not isinstance(s, str):
        return
    numOfBytes = 4
    ip = s.split('.')
    result = 0
    for i in range(numOfBytes - 1, -1, -1):
        result += (256 ** i) * int(ip[numOfBytes - i - 1])
    return result


def intToIP(num):
    if not isinstance(num, int) or num <= 0:
        return

    numOfBytes = 4
    result = []
    for i in range(numOfBytes - 1, -1, -1):
        result.append(str((num >> 8 * i) % 256))
    return '.'.join(result)


if __name__ == '__main__':
    print('Test 1: IP to Int, result = 1869640050')
    print(ipToInt('111.112.113.114'))
    print('Test 2: Int to IP, result = 111.112.113.114')
    print(intToIP(1869640050))