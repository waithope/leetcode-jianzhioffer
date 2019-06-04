

def anagram_detect_v1(l1, l2):
  pos1 = 0
  l2_cpy = list(l2)
  is_still_ok = True
  while pos1 < len(l1) and is_still_ok:
    pos2 = 0
    found = False
    while pos2 < len(l2_cpy) and not found:
      if l1[pos1] == l2_cpy[pos2]:
        found = True
      else:
        pos2 += 1
    if found:
      l2_cpy[pos2] = None
    else:
      is_still_ok = False
    pos1 += 1
  print(l2_cpy)
  return is_still_ok


def anagram_detect_v2(l1, l2):
  l1_cpy = list(l1)
  l2_cpy = list(l2)

  l1_cpy.sort()
  l2_cpy.sort()
  is_match = True
  pos1 = 0
  while pos1 < len(l1_cpy) and is_match:
    if l1_cpy[pos1] == l2_cpy[pos1]:
      pos1 += 1
    else:
      is_match = False
  return is_match

def anagram_detect_v3(l1, l2):
  l1_alpha_cnt = [0] * 26
  l2_alpha_cnt = [0] * 26

  for i in range(len(l1)):
    pos = ord(l1[i]) - ord('a')
    l1_alpha_cnt[pos] += 1
  for i in range(len(l2)):
    pos = ord(l2[i]) - ord('a')
    l2_alpha_cnt[pos] += 1

  is_match = True
  cnt = 0
  while cnt < len(l1_alpha_cnt) and is_match:
    if l1_alpha_cnt[cnt] == l2_alpha_cnt[cnt]:
      cnt += 1
    else:
      is_match = False
  return is_match




print(anagram_detect_v3('hello', 'ollhe'))
