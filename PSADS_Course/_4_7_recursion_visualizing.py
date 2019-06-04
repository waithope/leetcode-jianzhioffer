
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#   forward(200)
#   left(170)
#   if abs(pos()) < 1:
#     break
# end_fill()

# import turtle

# my_turtle = turtle.Turtle()
# my_window = turtle.Screen()

# def draw_spiral(my_turtle, line_len):
#   if line_len > 0:
#     my_turtle.forward(line_len)
#     my_turtle.right(90)
#     draw_spiral(my_turtle, line_len - 5)

# draw_spiral(my_turtle, 100)
# my_window.exitonclick()

# def tree(branch_len, t):
#   if branch_len > 5:
#     t.forward(branch_len)
#     t.right(20)
#     tree(branch_len - 10, t)
#     t.left(40)
#     tree(branch_len - 10, t)
#     t.right(20)
#     t.backward(branch_len)

# def main():
#   t = turtle.Turtle()
#   t.speed('slowest')
#   my_window = turtle.Screen()
#   t.left(90)
#   t.backward(30)
#   t.down()
#   t.color('red')
#   tree(30, t)
#   my_window.exitonclick()

# main()


import turtle

def draw_triangle(coor, color, t):
  t.fillcolor(color)
  t.up()
  t.goto(coor[0][0], coor[0][1])
  t.down()
  t.begin_fill()
  t.goto(coor[1][0], coor[1][1])
  t.goto(coor[2][0], coor[2][1])
  t.goto(coor[0][0], coor[0][1])
  t.end_fill()

def sierpinski(coor, base, tur):
  color_pan = ['blue', 'green', 'red', 'violet']
  draw_triangle(coor, color_pan[base], tur)
  if base > 0:
    sierpinski([coor[0],
    cal_mid_coor(coor[0], coor[1]),
    cal_mid_coor(coor[0], coor[2])
      ],base - 1, tur)

    sierpinski([coor[1],
    cal_mid_coor(coor[0], coor[1]),
    cal_mid_coor(coor[1], coor[2])
      ],base - 1, tur)

    sierpinski([coor[2],
    cal_mid_coor(coor[0], coor[2]),
    cal_mid_coor(coor[1], coor[2])
      ],base - 1, tur)

def cal_mid_coor(p1, p2):
  return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

# my_turtle = turtle.Turtle()
# my_window = turtle.Screen()
# my_turtle.speed('slowest')
# my_turtle.hideturtle()
# coordinate = [[-100, -50], [0, 100], [100, -50]]
# sierpinski(coordinate, 3, my_turtle)
# my_window.exitonclick()

                  #    'A'      'B'     'C'
# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)

# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)

# moveTower(2,"A","B","C")



# def search_from(maze, start_row, start_col):



##  it is extremely inefficient. In fact, it takes 67,716,925 recursive calls to find the optimal solution
def change_recur(coin_list, change):
  min_coins = change
  if change in coin_list:
    return 1
  else:
    for i in [c for c in coin_list if c <= change]:
      num_coins = 1 + change_recur(coin_list, change - i)
      if num_coins < min_coins:
        min_coins = num_coins
    return min_coins

# print(change_recur([1, 5, 10, 21, 25], 63))

##  remember some of the past results so we can avoid recomputing results we already know
##  it only takes 221 calls compared to early recursive function
def change_recur_memo(coin_list, change, memo_list):
  min_coins = change
  if change in coin_list:
    memo_list[change] = 1
    return 1
  elif memo_list[change] > 0:
    return memo_list[change]
  else:
    for i in [c for c in coin_list if c <= change]:
      # record = change_recur_memo(coin_list, change - i, memo_list)
      num_coins = 1 + change_recur_memo(coin_list, change - i, memo_list)
      if num_coins < min_coins:
        min_coins = num_coins
        # memo_list[change] = min_coins # memorize past result
    if memo_list[change] == 0:
      memo_list[change] = min_coins # memorize past result in order to decrease computation
    return min_coins

# print(change_recur_memo([1, 5, 10, 21, 25], 11, [0]*12))
# print(change_recur_memo([1, 5, 10, 21, 25], 63, [0]*64))
# import time
# start = time.time()
# print(change_recur_memo([1, 5, 10, 21, 25], 63, [0]*64))
# end = time.time()
# print('It takes %.7f secs' % (end-start))
# import timeit
# print('First method')
# print(timeit.timeit("change_recur_memo([1, 5, 10, 21, 25], 63, [0]*64)", "from __main__ import change_recur_memo", number=100))

## Dynamic Programming solution
def dp_change(coin_list, change, min_coins, coin_used):
  for cents in range(change + 1):
    coin_cnt = cents
    new_coin = 1
    for i in [c for c in coin_list if c <= cents]:
      if min_coins[cents - i] + 1 < coin_cnt:
        coin_cnt = min_coins[cents - i] + 1
        new_coin = i
    min_coins[cents] = coin_cnt
    coin_used[cents] = new_coin
  return min_coins[change]

def print_coins(coin_used, change):
  coin = change
  while coin > 0:
    this_coin = coin_used[coin]
    print(this_coin)
    coin = coin - this_coin

print(dp_change([1, 5, 10, 21, 25], 63, [0]*64, [0]*64))