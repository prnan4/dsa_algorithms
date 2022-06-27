# DSA Notes

## Lists

### Iterate through a list
``` 
for item in arr:
```

### Iterate through a list with index
```
for i, item in enumerate (arr)
```

### Check if list is empty
Returns True if arr is empty
```
if not arr:
```

### Iterate through portion of list 
Starts iterating from element at index 1.
```
for i in arr[1:]
```

### Remove element from list
Object is modified
```
arr.remove(9)
```

### Remove last element from list
Object is not modified.
```
arr = arr[:-1]
```

### Append elements of list a to list b
```
b.extend(a)
```

### Reverse list 
Object is modified. In place operation, does not return anything. Variable gets updates
```
b.reverse()
```

Object is not modified
```
c = b[::-1]
```

### Sort list
Object is modified
```
b.sort()
```

## Set

Like a list but with lookup time complexity O(1).
```
a = {1, 2}

# Return True
1 in a
```

## Matrix

Object is not modified.
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Remove first row and return
matrix = matrix[1:]

# Remove last row and return
matrix = matrix[: -1]

# Remove first column and return
matrix = [row [1:] for row in matrix]

# Remove last column and return
matrix = [row [:-1] for row in matrix]

```

Perform operations in place. In place operations do not return any result. Object is modified.

```
# Remove first row
matrix.pop(0)

# Remove last row
matrix.pop(-1)

# Remove first column
[r.pop(0) for r in matrix]

# Remove last column
[r.pop(-1) for r in matrix]
```

## Hashmap

### Create hashmap
```
dict = {}
```

### Append to hashmap
```
dict[1] = ‘a’
dict[2] = ‘b’
```

### Get hashmap keys
Stores hashmap keys in a list
```
all_keys = dict.keys()
```

### Look up
```
# Return True
1 in a
```

### Delete key value pair
```
del a[1]
```

## Strings

### Check if character exists in string

```
chars = [0] * 128
chars[ord[ch]] += 1
if chars[ord[ch]] > 1: ch already exists
```

In this case, indstead of searching through the whole list (time complexity O(N)), we only searching at particular index (time complexity O(1)).

## Stack 

BFS is done by stack. 

### Push

```
stack = []
stack.append('a')
```

### Pop 
Removes last element from list. Object is modified.
```
stack.pop()
```


## Queue

DFS is done by stack

## Linked List

Each node has a value and a pointer to the next node.

### Definition of a node
```
class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

a = ListNode(1)
b = ListNode(2, a)
```


### Linked list to array
```
def linked_list_to_arr(head):
   arr = []
   while head:
       arr.append(head.val)
       head = head.next
   return arr
```


### Array to linked list 
```
def arr_to_linked_list(arr):
   curr = None
   for ele in arr[::-1]:
       temp = ListNode(ele, curr)
       curr = temp
   return curr
```

### Reverse linked list
```
def reverseList(head):
   curr = None
   temp = head
   while temp:
       prev = temp.next
       temp.next = curr
       curr = temp
       temp = prev
   return curr
```

Check if the linked list is palindrome: https://www.youtube.com/watch?v=yOzXms1J6Nk


## Binary search

### Recursive approach: 

```
def binary_search(self, start_index, end_index, nums, target):
      if start_index <= end_index:
            mid = (start_index + end_index)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return self.binary_search(start_index, mid -1, nums, target)
            elif target > nums[mid]:
                return self.binary_search(mid + 1, end_index, nums, target)
      else:
            return -1

```
Time complexity: https://www.geeksforgeeks.org/complexity-analysis-of-binary-search/









