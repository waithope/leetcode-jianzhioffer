

class Queue():
  def __init__(self):
    self.items = []
  def is_empty(self):
    return self.items == []
  def enqueue(self, item):
    self.items.insert(0, item)
  def dequeue(self):
    return self.items.pop()
  def size(self):
    return len(self.items)

# test = Queue()
# for i in range(5):
#   test.enqueue(i)

# print(test.items)
# test.enqueue('dog')
# test.enqueue('8.4')
# print(test.items)

### every round name_list[name_queue.size()-1 - (rounds % name_queue.size())] was removed ###
# def hot_potato(name_list, rounds):
#   name_queue = Queue()
#   for name in name_list:
#     name_queue.enqueue(name)

#   while name_queue.size() > 1:
#     for cnt in range(rounds):
#       name_queue.enqueue(name_queue.dequeue())
#     name_queue.dequeue()
#     return name_queue.dequeue()

# name_list = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
# print(hot_potato(name_list, 7))


### Printing Task ###
# class Printer():
#   def __init__(self, ppm):
#     self.page_rate = ppm
#     self.current_task = None
#     self.time_remain = 0
#   def tick(self):
#     if self.current_task != None:
#       self.time_remain -= 1
#       if self.time_remain <= 0:
#         self.current_task = None
#   def busy(self):
#     if self.current_task != None:
#       return True
#     else:
#       return False
#   def start_next(self, new_task):
#     self.current_task = new_task
#     self.time_remain = new_task.get_pages() * (60 / self.page_rate)

# import random

# class Task():
#   def __init__(self, time):
#     self.time_stamp = time
#     self.pages = random.randrange(1, 21)
#   def get_stamp(self):
#     return self.time_stamp
#   def get_pages(self):
#     return self.pages
#   def wait_time(self, current_time):
#     return current_time - self.time_stamp


# def simulation(num_seconds, pages_per_minute):
#   printer = Printer(pages_per_minute)
#   print_queue = Queue()
#   waiting_time = []

#   for current_second in range(num_seconds):
#     if create_new_task():
#       task = Task(current_second)
#       print_queue.enqueue(task)
#     if (not printer.busy()) and (not print_queue.is_empty()):
#       next_task = print_queue.dequeue()
#       waiting_time.append(next_task.wait_time(current_second))
#       printer.start_next(next_task)
#     printer.tick()

#   average_wait = sum(waiting_time) / len(waiting_time)
#   print("Average waiting time %.2f secs %d task remaining" % (average_wait, print_queue.size()))

# def create_new_task():
#   num = random.randrange(1, 181)
#   if num == 180:
#     return True
#   else:
#     return False

# for i in range(10):
#   simulation(3600, 10)


### SELF CHECK ###

## TODO implement Printer Class
##  1. set print pages rate
##  2. start new task
##  3. hold state and time remainning
class Printer():
  def __init__(self, ppm):
    self.pages_rate = ppm
    self.current_task = None
    self.time_remaining = 0
  def tick(self):
    if self.current_task != None:
      self.time_remaining -= 1
      if self.time_remaining <= 0:
        self.current_task = None
  def busy(self):
    if self.current_task:
      return True
    else:
      return False
  def start_next_task(self, next_task):
      self.current_task = next_task
      self.time_remaining = self.current_task.get_pages() * 60 / self.pages_rate

## TODO implement Task class
## 1. create arbitrary pages
## 2. set timestamp
import random
class Task():
  def __init__(self, curr_secs):
    self.pages = random.randrange(1, 21)
    self.time_stamp = curr_secs
  def get_pages(self):
    return self.pages
  def get_time_stamp(self):
    return self.time_stamp


def simulation(time_segment, pages_per_minute):
  printer = Printer(pages_per_minute)
  print_queue = Queue()
  wait_time_table = []

  for curr_secs in range(time_segment):
    if create_new_task():
      new_task = Task(curr_secs)
      print_queue.enqueue(new_task)
    if not printer.busy() and not print_queue.is_empty():
      task = print_queue.dequeue()
      printer.start_next_task(task)
      wait_time_table.append(curr_secs - task.get_time_stamp())

    printer.tick()

  print("Average waiting time %.2f secs %d task remaning" % (sum(wait_time_table)/len(wait_time_table), print_queue.size()))

def create_new_task():
  num = random.randrange(1, 181)
  if num == 180:
    return True
  else:
    return False

for i in range(10):
  simulation(3600, 5)
