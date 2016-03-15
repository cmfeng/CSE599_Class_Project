"""Unit tests for regression.py"""

import unittest
import pandas as pd

from regression import user_model
from regression import correl
from regression import random_model


class TestRegression(unittest.TestCase):

    def test_correl(self):
        test_data = pd.DataFrame({'x': [1,2,3], 'y': [3,2,1]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == -1)

        test_data = pd.DataFrame({'x': [3,2,1], 'y': [1,2,3]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == -1)

        test_data = pd.DataFrame({'x': [100,200,300], 'y': [1,2,3]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == 1)

        test_data = pd.DataFrame({'x': [1,1,3], 'y': [1,2,3]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == 0.866)

        test_data = pd.DataFrame({'x': [9,11,23], 'y': [1,2,3]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == 0.924)

        test_data = pd.DataFrame({'x': [1,2,3], 'y': [-9,-11,-23]})
        result = round(correl(test_data['x'],test_data['y']),3)
        self.assertTrue(result == -0.924)
