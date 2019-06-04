from _3_5_stack import Stack

def infix_to_postfix(exp_str):
  s = Stack()
  exp_str = list(exp_str)
  postfix_str = ''
  precedence = {}
  precedence['*'] = 3
  precedence['/'] = 3
  precedence['+'] = 2
  precedence['-'] = 2
  precedence['('] = 1

  for token in exp_str:
    if token in "+-*/":
      while not s.is_empty() and precedence[s.peek()] >= precedence[token]:
        postfix_str += s.pop()
      s.push(token)
    elif token == '(':
      s.push(token)
    elif token == ')':
      postfix_str += s.pop()
      s.pop()
    else:
      postfix_str += token

  while not s.is_empty():
    postfix_str += s.pop()

  return postfix_str

# print(infix_to_postfix("((15/(7-(1+1)))*3)-(2+(1+1))"))

# 15 7 1 1 + − ÷ 3 × 2 1 1 + + −


## Postfix Evaluation##

def eval_postfix(exp_str):
  s = Stack()
  exp_str = list(exp_str)
  results = 0
  for token in exp_str:
    if token in '+-*/':
      operand1 = s.pop()
      operand2 = s.pop()
      results = do_math(token, operand1, operand2)
      s.push(results)
    else:
      s.push(int(token))
  return s.pop()


def do_math(op, operand1, operand2):
  if op == '*':
    return operand1 * operand2
  elif op == '/':
    return operand2 / operand1
  elif op == '+':
    return operand1 + operand2
  else:
    return operand2 - operand1

print(eval_postfix('15711+-/3*211++-'))
