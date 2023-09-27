import unittest
import math
import random

comment = '''
Sliding Window Problem
Input: A continual stream of stock prices.
Ouptut: 
- Calls to the "next(price)" add a new stock
- Calling "buyOrSell" returns wether to sell (-1) or buy (+1)
'''

def median(values):
    if values == None or len(values) < 1:
        return None
    if len(values)==1:
        return values[0]

    vv = sorted(values)
    # [0,1,2,3] median is 1.5
    # start --> 1,2 <--- end
    if len(vv) % 2 == 0:
        left_index = round(len(vv)/2)
        right_index = left_index+1 
        return (left_index + right_index)/2
    else:
        right_ish = len(vv)/2
        return round(right_ish)

class Predictor:
    def __init__(self, values=[]):
        self.window_size = 5
        self.values=values

    def next(self, incoming):
        """next reads the next stock value"""
        if len(self.values) >= self.window_size:
            self.values = self.values[1:]
        self.values.append(incoming)

    def buy_or_sell(self):
        """buyOrSell returns +1 to sell, -1 to buy"""

        # If the NEWEST value is greater than median, buy
        if self.values[-1] >= median(self.values):
            return 1
        else:
            return -1

def feed():
    predictor = Predictor([])
    for i in range([1,2,3,1,1,1,10,1]):
        predictor.next(i)

class TestPredictor(unittest.TestCase):
    def test_median(self):
        """Test the increment method."""
        obj = Predictor()
        self.assertEqual(median(obj.values), None)
        obj.next(1)
        self.assertEqual(median(obj.values), 1)
        obj.next(2)
        obj.next(3)
        ### Confirm it works for odds
        self.assertEqual(median(obj.values), 2)
        ### Confirm it works for evens
        obj.next(4)
        self.assertEqual(median(obj.values), 2.5)

    def test_prediction_to_buy_enormous_jump(self):
        """Test the increment method."""
        obj = Predictor()
        obj.next(1)
        obj.next(2)
        obj.next(3)
        ### Most obvious test case - massive jump = buy buy buy !!!
        obj.next(4000)
        self.assertGreater(obj.buy_or_sell(), 0)

    def test_scale(self):
        obj = Predictor()
        valuesAdded = 0
        for i in range(0,1000,2):
            obj.next(1000*(random.random()))
            valuesAdded += 1
            self.assertLessEqual(len(obj.values), obj.window_size)

        # Make sure that the above loop added LOTS of new values...
        # but that the # of values added was < the # of values in the total list
        self.assertGreater(valuesAdded, 100)
        self.assertGreater(valuesAdded, obj.window_size)
        self.assertGreater(valuesAdded, len(obj.values))

if __name__ == "__main__":
    unittest.main()