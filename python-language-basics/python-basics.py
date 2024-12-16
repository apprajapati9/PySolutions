#### Math ####

print()
print("##### math #####")
#division is demical by default
print(5/2)

#double slash rounds down
print(5//2)

# Most language round towards 0 by default, so negative numbers will round down
print (-3//2)
print(int(-3/2)) #workaround for above

#modding except for negatives
print(10%3)
print(-10%3)

#to be consistent with other langauge module
import math
from multiprocessing import heap

print("Floor -> {}".format(math.floor(3/2)))
print("Ceil -> {}".format(math.ceil(3/2)))
print("Sqrt -> {}".format(math.sqrt(2)))
print("Pow -> {}".format(math.pow(2,3)))

float("inf")
float("-inf")

#python numbers are infinite so they never overflow
print("2 power 200 -> {}".format(math.pow(2,200)))

print()
print("##### Arrays #####")

arr = [1,2,3]
print(arr)

print("appending new elements")
arr.append(4)
arr.append(5)
print(arr)

print("pop to delete last")
arr.pop()
print(arr)

print("insert(index, element)")
arr.insert(1,7)
print(arr)

print("access index using arr[index]")
arr[0]= 0
print(arr)

print("init arr of size n with default val of 1")
arr = [1] * 5
print(arr)
print(len(arr))


#print("{}".format())
print("ajay {}".format(arr))

# With index
for i, n in enumerate(arr):
    arr[i] = i
    print(i, n)
    
for i in arr:
    print(arr[i])

arr2 = []

for i in range(1,5):
    arr2.append(2*i)

    
print("arr2 ")   
for i in arr2:
    print(i)

#Loop through multiple arrays simultaneously with unpacking
print("zip -> going through multiple arrays fzip ya snippet in pythond mode")

arr3 = [1,2,3]
for n1, n2, n3 in zip(arr, arr2, arr3):
    print(n1, n2, n3)

for n1 in zip(arr,arr2,arr3):
    print(n1)
    

print()
    
print("arr.reverse")
arr.reverse()
print(arr)

print()
print("sorting - arr.sort()")
arr.sort()
print(arr)

print("arr.sort(reverse=True)")
arr.sort(reverse=True)
print(arr)


print()
print("sort based on length of string")
strs = ["122","12","1"]
strs.sort(key=lambda x: len(x))
print(strs)

print("2d lists")
arr = [[0]*4 for i in range(4)]
print(arr)

print("==== strings ===")
s = "abc"
print(s[0:2]) #start (inclusive):end (non-inclusive)


s+="def"
print(s)

print("Convert num to strings and vice versa")
print(int("123"))
print(str(123))

print("Get ASCII value of a char using ord(\"a\")")
print(ord("a"))

print("=== QUEUE ===")

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)

q.popleft()

print("popleft() {}".format(q))

q.appendleft(1)
print("appendleft() {}".format(q))

q.pop()
print("pop() {}".format(q))

print("== Hash sets ===")

mSet = set()
arr = []

print("Hashset vs arr: allows only unique elements unlike arr")
for i in range(1,10):
    arr.append(i//2)
    mSet.add(i//2)

print(mSet)
print(arr)

print("=== HashMaps ===")

mapp = {}
mapp["ajay"] = 88
mapp["ajay2"] = 33

print(mapp)

print(mapp["ajay"])

for key in mapp:
    print(key, mapp[key])

for val in mapp.values():
    print(val)

for key in mapp.items():
    print(key)

#extract each
for key,val in mapp.items():
    print(key,val)

print()

print("=== Tuples ===")
print("Tuples are like arrays but immutable")
tup = (1,2,3)
print(tup)

print("=== Heaps ===")

import heapq
heap = []
heapq.heappush(heap,4)
heapq.heappush(heap,3)
heapq.heappush(heap,2)

# Min is always at index 0
print(heap[0])

#print all heap values
while len(heap):
    print(heapq.heappop(heap))

#build heap from init values
print("Build heap from init values")

arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

print("=== Functions ===")

def sum(a,b):
    return a+b

print(sum(12,12))

print()
print("Nested functions")
def outer(a,b):
    c = "c"
    def inner():
        return a+b+c
    return inner()

print(outer("a","b"))

print()
print("Can modify objects but no reassign")
def double(arr, val):
    def helper():
        for i,n in enumerate(arr):
            arr[i] *=2

        #will only modify val in the helper scope

        nonlocal val
        val *= 2

    helper()
    print(arr, val)

arr = [1,2]
double(arr, val)
print(arr)

print("=== Classes ====")

class Ajay:
    def __init__(self):
      	self.name = "aaaajay"

ajay = Ajay()

print(ajay.name)

def ajay(num1, num2):
    return num1*num2

