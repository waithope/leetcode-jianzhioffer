'''
    黑白棋盘
===============
有一块黑白棋盘，共有n行m列，任意相邻的两个格子都是不同的颜色，坐标（1，1）的格子
为白色。
问（1）：算出黑白格子数目
问（2）：在n行m列中选择一个左下角坐标（x0, y0），右上角坐标（x1, y1）的矩形，把这个
矩形内的方块全部涂白，算出黑白格子数目
问（3）：在以上基础上，选择一个左下角坐标（x2, y2），右上角坐标（x3, y3）的矩形，把这个
矩形内的方块全部涂白，算出黑白格子数目

输入输出描述
==========
输入：第一行棋盘大小，第二行涂白操作坐标(左上角,右上角)，第三行涂黑操作坐标(左上角，右上角)
输入：白块和黑块数目
'''


def blackAndWhite():
    '''
    提示：主要的难点是计算涂黑操作的矩形块和涂白操作的矩形块是否有重叠，
    以及如果有重叠，如何计算涂黑操作矩形块除重叠之外的黑白块数。
    我的直线思维是：先计算涂黑操作矩形块的黑白块数，再计算重叠矩形块的黑白块数，两者相减，
    就是涂黑操作矩形块除重叠之外的黑白块数，有了这个结果后面的计算就简单了。
    '''
    def calRectWhiteBlacks(rect):
        '''
        计算子矩形的黑白总数
        '''
        x0, y0, x1, y1 = rect
        subRectWBs = (x1 - x0 + 1) * (y1 - y0 + 1)    # 子矩形的黑白总数
        blacks, whites = 0, 0
        if (subRectWBs % 2) == 0:
            whites = blacks = subRectWBs // 2
        elif (x0 + y0) % 2 == 0:           #左下角位置奇数行奇数列或偶数行偶数列为白块
            whites = subRectWBs // 2 + 1
            blacks = subRectWBs // 2
        else:
            whites = subRectWBs // 2
            blacks = subRectWBs // 2 + 1
        return [whites, blacks]

    def intersection(rect1, rect2):
        '''
        计算矩形重叠区域
        '''
        x0, y0, x1, y1 = rect1
        x2, y2, x3, y3 = rect2
        leftX = max(x0, x2)
        rightX = min(x1, x3)
        topY = min(y1, y3)
        bottomY = max(y0, y2)
        if (leftX <= rightX) and (bottomY <= topY):
            return [leftX, bottomY, rightX, topY]
        else:
            return []

    input_str = input('请输入棋盘大小：')
    n, m = list(map(int, input_str.strip().split(' ')))
    input_str = input('请输入涂白操作的左下角右上角坐标：')
    rect1 = list(map(int, input_str.strip().split(' ')))
    input_str = input('请输入涂白操作的左下角右上角坐标：')
    rect2 = list(map(int, input_str.strip().split(' ')))

    whites, blacks = 0, 0
    res = []

    rectOrigin = [1, 1, m, n]            # 初始棋盘的左下角，右上角坐标
    whites, blacks = calRectWhiteBlacks(rectOrigin)
    res.append([whites, blacks])

    # 涂白操作
    whites_temp, blacks_temp = calRectWhiteBlacks(rect1)
    whites, blacks = whites + blacks_temp, blacks - blacks_temp
    res.append([whites, blacks])

    # 涂黑操作
    whites_temp, blacks_temp = calRectWhiteBlacks(rect2)
    rectIntersec = intersection(rect1, rect2)
    if not rectIntersec:
        whites, blacks = whites - whites_temp, blacks + whites_temp
        res.append([whites, blacks])
    else:
        temp = calRectWhiteBlacks(rectIntersec)
        # 子矩形2去除重叠区域后的黑白块数
        whites_temp, blacks_temp = whites_temp - temp[0], blacks_temp - temp[1]
        whites, blacks = whites - sum(temp) - whites_temp, blacks + sum(temp) + whites_temp
        res.append([whites, blacks])

    # 以每次操作结果一行输出
    for co in res:
        print(' '.join(map(str, co)))