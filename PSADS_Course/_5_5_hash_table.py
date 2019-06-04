
def hash(str, table_size):
  sum = 0
  for pos in range(len(str)):
    sum += ord(str[pos])
  return sum % table_size

def hash_weight(str, table_size):
  sum = 0
  for pos in range(len(str)):
    sum += (pos + 1) * ord(str[pos])
  return sum % table_size

# print(hash_weight('cat', 11))

# class HashTable():
#   def __init__(self):
#     self.size = 11
#     self.slots = [None] * self.size
#     self.data = [None] * self.size
#   def hash_func(self, key, size):
#     return key % size
#   def rehash(self, pre_hash, size):
#     return (pre_hash + 1) % size
#   def put(self, key, data):
#     hash_val = self.hash_func(key, len(self.slots))
#     if self.slots[hash_val] == None:
#       self.slots[hash_val] = key
#       self.data[hash_val] = data
#     else:
#       if self.slots[hash_val] == key:
#         self.data[hash_val] == data   # replace
#       else:
#         next_slot = self.rehash(hash_val, self.size)
#         while self.slots[next_slot] != None and self.slots[next_slot] != key:
#           next_slot = self.rehash(next_slot, self.size)
#         if self.slots[next_slot] == None:
#           self.slots[next_slot] = key
#           self.data[next_slot] = data
#         else:
#           self.data[next_slot] = data
#   def get(self, key):
#     start_slot = self.hash_func(key, self.size)
#     data = None
#     stop = False
#     found = False
#     pos = start_slot
#     while self.slots[pos] != None and not found and not stop:
#       if self.slots[pos] == key:
#         found = True
#         data = self.data[pos]
#       else:
#         pos = self.rehash(pos, self.size)
#         if pos == start_slot:
#           stop = True
#     return data
#   def __setitem__(self, key, data):
#     self.put(key, data)
#   def __getitem__(self, key):
#     return self.get(key)

## Self Chech ##

class HashTable():
  def __init__(self, size):
    self.size = size
    self.slots = [None]*self.size
    self.data = [None]*self.size
  def hash_func(self, key):
    return key % self.size
  def rehash(self, key):
    return (key + 1) % self.size
  def put(self, key, val):
    slot_val = self.hash_func(key)
    if self.slots[slot_val] == None:
      self.slots[slot_val] = key
      self.data[slot_val] = val
    elif self.slots[slot_val] == key:
      self.data[slot_val] = val
    else:
      next_slot = self.rehash(key)
      is_ok = False
      while not is_ok:
        if self.slots[next_slot] == key:
          self.data[next_slot] = val
          is_ok = True
        elif self.slots[next_slot] == None:
          self.slots[next_slot] = key
          self.data[next_slot] = val
          is_ok = True
        elif next_slot == slot_val:
          is_ok = True
          raise IndexError('No more space')
        else:
          next_slot = self.rehash(next_slot)
  def get(self, key):
    start_slot = self.hash_func(key)
    data = None
    found = False
    stop = False
    pos = start_slot
    while self.slots[pos] != None and not found and not stop:
      if self.slots[pos] == key:
        found = True
        data = self.data[pos]
      else:
        pos = self.rehash(pos)
        if pos == start_slot:    # accomplish a round
          stop = True
    return data
  def delete(self, key):
    start_slot = self.hash_func(key)
    if self.slots[start_slot] == None:
      raise KeyError("No such key")
    found = False
    stop = False
    pos = start_slot
    while self.slots[pos] != None and not found and not stop:
      if self.slots[pos] == key:
        found = True
        self.data[pos] = None
        self.slots[pos] = None
      else:
        pos = self.rehash(pos)
        if pos == start_slot:
          stop = True
  def len(self):
    cnt = 0
    for i in self.slots:
      if i != None:
        cnt += 1
    return cnt
  def __setitem__(self, key, val):
    self.put(key, val)
  def __getitem__(self, key):
    return self.get(key)
  def __delitem__(self, key):
    self.delete(key)
  def __len__(self):
    return self.len()
  # def __contains__(self, key):



h = HashTable(11)
h[54] = 'cat'
h[26] = 'dog'
h[93] = 'lion'
h[17] = 'tiger'
h[77] = 'pig'
h[31] = 'cow'
h[44] = 'goat'
h[55] = 'monkey'
h[20] = 'duck'
h[7] = 'tan'
h[8] = 'can'
print(h.slots)
print(h.data)