import unittest
import math
import random

comment = '''
Exploring the 'array except self' problem.

    [1,2,3,4] --> [24,12,8,6]

    ### Implementation 1
    left [1,   1,  2, 6  ]
    right[24, 12,  4, 1 ]
    output_array = 
    
    ### Implementation 2
    [1, 2, 3, 4]
    [24, 12, 4, 1]

    ### Implementation 3
    Same, but eliminate the right array.

    output_array = [  ]
'''

import functools

def mult(x,y):
    return x*y

def left_of(array, i):
    if i <= 0:
        return 1
    return array[i-1]
def right_of(array, i):
    if i >= len(array)-1:
        return 1
    return array[i+1]

def array_except_self3(array):
    left = [1]*len(array)

    ### Use "left" as the output array...
    curr_left = 1
    for i in range(0, len(array), 1):
        left [i] = left_of(array,i)*curr_left
        curr_left = left[i]

    ## 1 2 3 4
    ## 1 1 2 6 <-- left

    ## 24 12 8 6
    right_neigbors = 1
    # 3, 2, 1, 0
    for i in range(len(array)-1,-1,-1):
        # left[3] = 
        #   1 <--- running 
        #   * 6 <-- left[3]
        left[i] = right_neigbors * left[i]
        right_neigbors *= array[i]

    return left


def array_except_self2(array):
    new_array = [1]*len(array)
    left = [1]*len(array)
    right = [1]*len(array)
    curr_left = 1
    # 0, 1, 2, 3
    ### I forgot that array indices were [0, 3)
    for i in range(0, len(array), 1):
        left [i] = left_of(array,i)*curr_left
        curr_left = left[i]

    curr_right = 1
    # [3, 0)
    # 3,2,1,0
    for i in range(len(array)-1,-1,-1):
        right [i] = right_of(array,i)*curr_right
        curr_right = right[i]

    for i in range(0, len(array), 1):
        new_array[i] = left[i] * right[i]

    print("\n LEFT = ",left)
    print("\n RIGHT = ", right)
    print("==>",new_array)
    return new_array

def array_except_self(array):
    new_array = []
    for i in range(0,len(array),1):
        mult = 1
        for ii,vv in enumerate(array):
            if ii!=i:
                mult=mult*vv
        new_array.append(mult)
    print(new_array)
    return new_array

class TestArrayExceptSelf(unittest.TestCase):
    def test_1(self):
        self.assertEqual(array_except_self([1,2,3,4]), [24,12,8,6])
    def test_2(self):
        self.assertEqual(array_except_self2([1,2,3,4]), array_except_self([1,2,3,4]))
    def test_3(self):
        self.assertEqual(array_except_self3([1,2,3,4]), array_except_self([1,2,3,4]))

if __name__ == "__main__":
    unittest.main()
    #array_except_self([9,8,7,5,0])