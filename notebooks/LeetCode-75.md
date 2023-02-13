---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python tags=[]
%load_ext autoreload
%autoreload 2
```

```python tags=[]
from typing import Optional, List
```

# Leetcode-75

This notebook contains some solutions to problems in the [LeetCode 75 study plan](https://leetcode.com/study-plan/leetcode-75/).

```python tags=[]
from lcp.core.node import ListNode, create_linked_list
```

## 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

<!-- #region tags=[] -->
[1, 2] -> [2, 1]

[1] -> [1]

[2, 4, 6] -> [6, 4, 2]



brute force:
go to the end of the list and for each index create a hashmap of each node. Then afterwards go back through the hashmap and create the new linked list
<!-- #endregion -->

```python tags=[]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index_map = {}
        curr = head
        ix = 0

        # edgecases
        if not curr:
            return head

        # fill the map
        while curr:
            index_map[ix] = curr
            curr = curr.next
            ix +=1

        ix -= 1
        reversed_head = ListNode(index_map.get(ix).val)
        curr = reversed_head

        # fill the reversed
        while ix > 0:
            ix -= 1
            curr.next = ListNode(index_map.get(ix).val)
            curr = curr.next

        return reversed_head
```

```python tags=[]
head = create_linked_list([])
```

```python tags=[]
sol = Solution()

result = sol.reverseList(head)
print(result)
```

# 876. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

```python tags=[]
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index_map = {}
        curr = head
        ix = 0

        # edgecases
        if not curr:
            return head

        # fill the map
        while curr:
            index_map[ix] = curr
            curr = curr.next
            ix +=1

        ix -=1
        
        # ix is even (we have a middle with 0)
        if ix % 2 == 0:
            return index_map.get(ix/2)
        else:
            return index_map.get(int(ix/2)+1)
```

```python tags=[]
head = create_linked_list([])
```

```python tags=[]
sol = Solution()

result = sol.middleNode(head)
print(result)
```

# 142. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1)

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

```python tags=[]
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        node_set = {}
        ix = 0
        
        while curr:
            if node_set.get(curr):
                return curr
            
            node_set[curr] = True
            curr = curr.next

        return None
```

```python tags=[]
head = create_linked_list([1])
```

```python tags=[]
sol = Solution()

result = sol.detectCycle(head)
print(result)
```

# 121. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```python tags=[]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        left_ix = 0
        right_ix = 1
        
        while right_ix < len(prices):
            profit = prices[right_ix] - prices[left_ix]
            
            if profit > max_profit:
                max_profit = profit
            
            if prices[right_ix] < prices[left_ix]:
                left_ix = right_ix
            
            right_ix +=1
                
        return max_profit
```

trick is of course to buy low and sell high. Which probably means we have to find a pair of numbers where b-a is biggest. So I could loop once over the list and grab the minimum and maximum. 

We can loop over the array and keep track of the min and the max. 



```python tags=[]
prices = [7,1,5,3,6,4]
```

```python tags=[]
sol = Solution()

sol.maxProfit(prices)
```

# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

```python tags=[]
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = {}
        
        for char in s:
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1
                
        count = 0
        used_uneven = False
        
        for k,v in count_map.items():
            if v % 2 == 0:
                count += v
            else:
                count += v - 1
                
                if not used_uneven:
                    count += 1
                    used_uneven = True
        
        return count
```

How do we build a longest palidrome? Basically for each different letter we have we can build it on both sides.
If we have a single letter we can put it in the middle then all other single letters will fail. So from the set of all letters if even, we can use it for the palindrome, if uneven we cannot use it for the palindrome except for one (the one we put in the middle)

```python tags=[]
example = "abccccdd"
```

```python tags=[]
sol = Solution()

sol.longestPalindrome(example)
```

```python

```
