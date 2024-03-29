---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
%load_ext autoreload
%autoreload 2
```

```python
from typing import Optional, List
```

# Leetcode-75

This notebook contains some solutions to problems in the [LeetCode 75 study plan](https://leetcode.com/study-plan/leetcode-75/).


```python
from lcp.core.node import ListNode, create_linked_list, Node, TreeNode
```

## 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

<!-- #region -->
[1, 2] -> [2, 1]

[1] -> [1]

[2, 4, 6] -> [6, 4, 2]



brute force:
go to the end of the list and for each index create a hashmap of each node. Then afterwards go back through the hashmap and create the new linked list
<!-- #endregion -->

```python
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

```python
head = create_linked_list([4, 7, 1, 4])
```

```python
sol = Solution()

result = sol.reverseList(head)
print(result)
```

# 876. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

```python
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

```python
head = create_linked_list([])
```

```python
sol = Solution()

result = sol.middleNode(head)
print(result)
```

# 142. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1)

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

```python
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

```python
head = create_linked_list([1])
```

```python
sol = Solution()

result = sol.detectCycle(head)
print(result)
```

# 121. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```python
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



```python
prices = [7,1,5,3,6,4]
```

```python
sol = Solution()

sol.maxProfit(prices)
```

# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

```python
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

```python
example = "abccccdd"
```

```python
sol = Solution()

sol.longestPalindrome(example)
```

# [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

```python
class Solution:
    def __init__(self):
        self.result = []
    
    def preorder(self, root: Node) -> List[int]:
        self.dfs(root)
        return self.result
        
    def dfs(self, node):
        if not node:
            return
        
        self.result.append(node.val)

        if node.children:
            for child in node.children:
                self.dfs(child)
        return 
    
```

```python
n5, n6 = Node(5), Node(6)
n4 = Node(4)
n3 = Node(3, [n5, n6])
n2 = Node(2)
n1 = Node(1, [n3, n2, n4])
```

```python
sol = Solution()

sol.preorder(n1)
```

# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

```python
t15 = TreeNode(15)
t7 = TreeNode(7)
t20 = TreeNode(20, t15, t7)
t9 = TreeNode(9)
t3 = TreeNode(3, t9, t20)
```

```python
class Solution:
    def __init__(self):
        self.result = []
        
    def levelOrder(self, root):
        level = [root]

        while root and level:
            current_nodes = []
            next_level = []
            for node in level:
                current_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            self.result.append(current_nodes)
            level = next_level


        return self.result
```

```python
sol = Solution()

sol.levelOrder(t3)
```

# [704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

```python
class Solution:
    def __init__(self):
        self.ix = 0
        
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        self.remove(nums, target)
        return self.ix
        
    def remove(self, nums: List[int], target: int):
        # go to the middel of the list.
        
        mid_ix = int(len(nums) / 2)
        y = nums[mid_ix]
        # print(len(nums), mid_ix, y)
        
        if not nums:
            self.ix = -1
            return
        
        if (len(nums) == 1) & (nums[0] != target):
            self.ix = -1
            return
        
        if y == target:
            self.ix += mid_ix
            return
        
        elif y < target:
            self.ix += mid_ix
            self.remove(nums[mid_ix:], target)
        
        elif y > target:
            self.remove(nums[:mid_ix], target)
```

```python
example = [-1,0,3,5,9,12]

sol = Solution()


sol.search(example, 3)
```

# [278. First Bad Version](https://leetcode.com/problems/first-bad-version)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

```python
import random
from functools import partial

def foo(version: int, bad_n: int):
    return version >= bad_n

isBadVersion = partial(foo, bad_n=random.randint(1, 500))


isBadVersion
```

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left


sol = Solution()

sol.firstBadVersion(500)
```

# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_is_shortest = len(word1) < len(word2)
        min_len = len(word1) if word1_is_shortest else len(word2)

        result = ""
        for i in range(min_len):
            result = result + word1[i] + word2[i]

        if word1_is_shortest:
            result = result + word2[i+1:]

        else:
            result = result + word1[i+1:]
        
        return result
```

```python
sol = Solution()

sol.mergeAlternately("foo", "barrr")
```

# [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

```python
"ab" * 2
```

```python
class Solution:

    def is_divisor(self, str1: str, sub_str1: str):
        res = len(str1) % len(sub_str1)
        if res != 0:
            return False
        div = int(len(str1) / len(sub_str1))

        return sub_str1 * div == str1
        
    
    
    def get_divisors(self, str1: str):
        divisors = []
        substr = ""
        for i in range(1, len(str1)+1):
            if self.is_divisor(str1, str1[:i]):
                divisors.append(str1[:i])
        return divisors

    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        divs1 = self.get_divisors(str1)
        divs2 = self.get_divisors(str2)

        intersection = list(set(divs1).intersection(set(divs2)))

        gcd = max(intersection, key=len)

        return gcd
```

```python
sol = Solution()

sol.gcdOfStrings("ABAABAABA", "ABA")
```

## [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75)

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.



```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = max(candies)

        return [(candy + extraCandies) >= maxC for candy in candies]
```

```python
sol = Solution()

candies = [2,3,5,1,3]; extraCandies = 3

sol.kidsWithCandies(candies, extraCandies)
```

## [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # a spot is surrounded by zeros.
        flowerbed = [0] + flowerbed + [0]
        current_ix = 1
        spot_count = 0

        while current_ix < len(flowerbed)-1:
            current = flowerbed[current_ix]
            next = flowerbed[current_ix + 1]
            previous = flowerbed[current_ix -1]

            if current == 0 and next == 0 and previous == 0:
                spot_count += 1
                flowerbed[current_ix] = 1

            current_ix += 1

        return n <= spot_count
```

```python
sol = Solution()

flowerbed = [0,0,0]
n = 2

sol.canPlaceFlowers(flowerbed, n)
```

## [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = {"a", "e", "i", "o", "u"}

        letters = []
        vowels = []

        for l in s:
            if l.lower() in vowelSet:
                vowels.append(l)

        print(vowels)
        
        for l in s:
            if l.lower() in vowelSet:
                reversed_vowel = vowels.pop(-1)
                letters.append(reversed_vowel)
            else:
                letters.append(l)
        
        return "".join(letters)
```

```python
sol = Solution()

string1 = "aA"

sol.reverseVowels(string1)
```

## [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        sentence_list = s.split(" ")
        stripped_sentence_list = [w for w in sentence_list if w != ""]

        return " ".join(stripped_sentence_list[-1::-1])
```

```python
sentence = "   this     is a nice sentence   "

sol = Solution()

sol.reverseWords(sentence)
```

```python

```
