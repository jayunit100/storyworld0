import unittest
import math
import random
import functools
import collections
from typing import List

comment = '''
Exploring the "flooded world" problem.

You are given an integer array h of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, h[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: h = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: h = [1,1]
Output: 1

v(x,y)=v(y,x) = min(h(a), h(b)) * abs(b - a)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = im = 0
        j = jm = len(height) - 1
        vm = 0

        while i < j:
            print(i,j)
            # calculate first ! otherwise we'll miss this I value...
            v = min(height[i], height[j]) * (abs(j-i)+1)
            if v > vm:
                vm=v
                im = i
                jm = j

            if height[i] > height[j]:
                j-=1
            #elif h[i] < h[j]:
            else:
                i+=1
        return vm



class TestFloodedWorld(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(6,sol.maxArea([3,3,1]))

if __name__ == "__main__":
    unittest.main()
    #array_except_self([9,8,7,5,0])